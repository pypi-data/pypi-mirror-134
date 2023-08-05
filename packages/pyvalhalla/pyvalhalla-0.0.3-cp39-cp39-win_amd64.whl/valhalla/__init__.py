

""""""  # start delvewheel patch
def _delvewheel_init_patch_0_0_17():
    import os
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'pyvalhalla.libs'))
    if sys.version_info[:2] >= (3, 8):
        if os.path.exists(os.path.join(sys.base_prefix, 'conda-meta')):
            # backup the state of the environment variable CONDA_DLL_SEARCH_MODIFICATION_ENABLE
            conda_dll_search_modification_enable = os.environ.get("CONDA_DLL_SEARCH_MODIFICATION_ENABLE")
            os.environ['CONDA_DLL_SEARCH_MODIFICATION_ENABLE']='1'

        os.add_dll_directory(libs_dir)

        if os.path.exists(os.path.join(sys.base_prefix, 'conda-meta')):
            # restore the state of the environment variable CONDA_DLL_SEARCH_MODIFICATION_ENABLE
            if conda_dll_search_modification_enable is None:
                os.environ.pop("CONDA_DLL_SEARCH_MODIFICATION_ENABLE", None)
            else:
                os.environ["CONDA_DLL_SEARCH_MODIFICATION_ENABLE"] = conda_dll_search_modification_enable
    else:
        from ctypes import WinDLL
        with open(os.path.join(libs_dir, '.load-order-pyvalhalla-0.0.3')) as file:
            load_order = file.read().split()
        for lib in load_order:
            WinDLL(os.path.join(libs_dir, lib))


_delvewheel_init_patch_0_0_17()
del _delvewheel_init_patch_0_0_17
# end delvewheel patch

from ._valhalla import *

from .actor import Actor
from .config import get_config

__version__ = "0.0.3"
__valhalla_commit__ = "b8ffa47e1945fd2d70705ad475a5e2185e1bcf72"
