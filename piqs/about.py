
###############################################################################
"""
Command line output of information on QuTiP and dependencies.
"""
__all__ = ['about']

import sys
import os
import platform
import numpy
import scipy
import inspect
from qutip.utilities import _blas_info
import qutip.settings
from qutip.hardware_info import hardware_info


def about():
    """
    About box for PIQS. 
    """
    print("")
    print("PIQS: Permutational Invariant Quantum Solver")
    print("N. Shammah and S. Ahmed")
    print("PIQS Version:      %s" % piqs.__version__)
    print("QuTiP Version:      %s" % qutip.__version__)
    print("Numpy Version:      %s" % numpy.__version__)
    print("Scipy Version:      %s" % scipy.__version__)
    try:
        import Cython
        cython_ver = Cython.__version__
    except:
        cython_ver = 'None'
    print("Cython Version:     %s" % cython_ver)
    try:
        import matplotlib
        matplotlib_ver = matplotlib.__version__
    except:
        matplotlib_ver = 'None'
    print("Matplotlib Version: %s" % matplotlib_ver)
    print("Python Version:     %d.%d.%d" % sys.version_info[0:3])
    print("Number of CPUs:     %s" % hardware_info()['cpus'])
    print("Platform Info:      %s (%s)" % (platform.system(),
                                           platform.machine()))
    # citation
    longbar = "=============================================================="
    longbar += "================"
    cite_msg = "For your convenience a bibtex file can be easily generated"
    cite_msg += " using `piqs.cite()`"
    print(longbar)
    print("Please cite PIQS in your publication.")
    print(longbar)
    print(cite_msg)


if __name__ == "__main__":
    about()