# -*- coding: utf-8 -*-

from simmate.workflow_engine.workflow import (
    Workflow,
    Parameter,
    ModuleStorage,
)

from simmate.workflows.common_tasks.all import (
    LoadNestedCalculationTask,
    SaveNestedCalculationTask,
)

from simmate.calculators.vasp.workflows.relaxation.quality_00 import (
    workflow as relaxation_quality00,
)
from simmate.calculators.vasp.workflows.relaxation.quality_01 import (
    workflow as relaxation_quality01,
)
from simmate.calculators.vasp.workflows.relaxation.quality_02 import (
    workflow as relaxation_quality02,
)
from simmate.calculators.vasp.workflows.relaxation.quality_03 import (
    workflow as relaxation_quality03,
)
from simmate.calculators.vasp.workflows.relaxation.quality_04 import (
    workflow as relaxation_quality04,
)
from simmate.calculators.vasp.workflows.energy.quality_04 import (
    workflow as energy_quality04,
)

from simmate.calculators.vasp.database.relaxation import StagedRelaxation
from simmate.calculators.vasp.database.energy import Quality04StaticEnergy

# init common tasks
setup_calculation = LoadNestedCalculationTask(StagedRelaxation)
save_calculation = SaveNestedCalculationTask(StagedRelaxation)

# init workflow tasks
# OPTIMIZE: Make this a for-loop in Prefect 2.0! We can use a for-loop in the
# workflow context below too.
relax_task_00 = relaxation_quality00.to_workflow_task()
relax_task_01 = relaxation_quality01.to_workflow_task()
relax_task_02 = relaxation_quality02.to_workflow_task()
relax_task_03 = relaxation_quality03.to_workflow_task()
relax_task_04 = relaxation_quality04.to_workflow_task()
static_task_04 = energy_quality04.to_workflow_task()

with Workflow("Staged Relaxation") as workflow:

    structure = Parameter("structure")
    command = Parameter("command", default="vasp_std > vasp.out")
    directory = Parameter("directory", default=None)

    # Rather than letting our first relaxation handle the directory and structure
    # loading, we do this up front because we want to pass the directory to all
    # other tasks.
    directory_cleaned = setup_calculation(directory)

    # Our first relaxation is directly from our inputs. The remaining one
    # pass along results and the working directory
    run_id_00 = relax_task_00(
        structure=structure,
        command=command,
        directory=directory_cleaned,
    )

    # TODO: Use a for-loop in Prefect 2.0!

    # relaxation 01
    run_id_01 = relax_task_01(
        structure={
            "calculation_table": "Quality00Relaxation",
            "directory": directory_cleaned,
            "structure_field": "structure_final",
        },
        command=command,
        use_previous_directory=True,
        upstream_tasks=[run_id_00],
    )

    # relaxation 02
    run_id_02 = relax_task_02(
        structure={
            "calculation_table": "Quality01Relaxation",
            "directory": directory_cleaned,
            "structure_field": "structure_final",
        },
        command=command,
        use_previous_directory=True,
        upstream_tasks=[run_id_01],
    )

    # relaxation 03
    run_id_03 = relax_task_03(
        structure={
            "calculation_table": "Quality02Relaxation",
            "directory": directory_cleaned,
            "structure_field": "structure_final",
        },
        command=command,
        use_previous_directory=True,
        upstream_tasks=[run_id_02],
    )

    # relaxation 04
    run_id_04 = relax_task_04(
        structure={
            "calculation_table": "Quality03Relaxation",
            "directory": directory_cleaned,
            "structure_field": "structure_final",
        },
        command=command,
        use_previous_directory=True,
        upstream_tasks=[run_id_03],
    )

    # Static Energy (MIT)
    run_id_05 = static_task_04(
        structure={
            "calculation_table": "Quality04Relaxation",
            "directory": directory_cleaned,
            "structure_field": "structure_final",
        },
        command=command,
        use_previous_directory=True,
        upstream_tasks=[run_id_04],
    )

    # save calculation metadata
    save_calculation(upstream_tasks=[run_id_05])

workflow.storage = ModuleStorage(__name__)
workflow.project_name = "Simmate-Relaxation"
workflow.calculation_table = StagedRelaxation
workflow.result_table = Quality04StaticEnergy
workflow.register_kwargs = ["prefect_flow_run_id"]
