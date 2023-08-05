from .proxy import *
from .climate import *
from .psm import *
from .visual import (
    set_style,
    showfig,
    closefig,
    savefig,
)
set_style()

# get the version
from importlib.metadata import version
__version__ = version('p2k')