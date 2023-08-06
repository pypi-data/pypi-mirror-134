# -*- coding: utf-8 -*-

# This file sets up a shortcut for importing so that you can do...
#   from simmate.workflows.relaxation.all import mit_relaxation, mp_relaxation, ...
# instead of what's written below. You should only use this shortcut if you are
# using ALL of the classes below or if you are running some quick interactive test.

from simmate.calculators.vasp.workflows.energy.materials_project import (
    workflow as energy_matproj,
)
from simmate.calculators.vasp.workflows.energy.mit import workflow as energy_mit
from simmate.calculators.vasp.workflows.energy.quality_04 import (
    workflow as energy_quality04,
)
