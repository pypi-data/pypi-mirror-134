

""""""  # start delvewheel patch
def _delvewheel_init_patch_0_0_17():
    import os
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, '.'))
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
        with open(os.path.join(libs_dir, '.load-order-scs-3.1.0')) as file:
            load_order = file.read().split()
        for lib in load_order:
            WinDLL(os.path.join(libs_dir, lib))


_delvewheel_init_patch_0_0_17()
del _delvewheel_init_patch_0_0_17
# end delvewheel patch

#!/usr/bin/env python
from warnings import warn
from scipy import sparse
import _scs_direct

__version__ = _scs_direct.version()
__sizeof_int__ = _scs_direct.sizeof_int()
__sizeof_float__ = _scs_direct.sizeof_float()

_USE_INDIRECT_DEFAULT = False


# SCS return integers correspond to one of these flags: (copied from scs/include/glbopts.h)
INFEASIBLE_INACCURATE = -7  # SCS best guess infeasible
UNBOUNDED_INACCURATE = -6   # SCS best guess unbounded
SIGINT = -5                 # interrupted by sig int
FAILED = -4                 # SCS failed
INDETERMINATE = -3          # indeterminate (norm too small)
INFEASIBLE = -2             # primal infeasible, dual unbounded
UNBOUNDED = -1              # primal unbounded, dual infeasible
UNFINISHED = 0              # never returned, used as placeholder
SOLVED = 1                  # problem solved to desired accuracy
SOLVED_INACCURATE = 2       # SCS best guess solved


def solve(probdata, cone, **kwargs):
  """Solves convex cone problems.

    @return dictionary with solution with keys:
         'x' - primal solution
         's' - primal slack solution
         'y' - dual solution
         'info' - information dictionary
  """
  if not probdata or not cone:
    raise ValueError('Missing data or cone information')

  if 'b' not in probdata or 'c' not in probdata:
    raise ValueError('Missing one or more of b, c from data dictionary')
  if 'A' not in probdata:
    raise ValueError('Missing A from data dictionary')

  A = probdata['A']
  b = probdata['b']
  c = probdata['c']

  if A is None or b is None or c is None:
    raise ValueError('Incomplete data specification')

  if not sparse.issparse(A):
    raise TypeError('A is required to be a sparse matrix')
  if not sparse.isspmatrix_csc(A):
    warn('Converting A to a CSC (compressed sparse column) matrix; may take a '
         'while.')
    A = A.tocsc()

  if sparse.issparse(b):
    b = b.todense()

  if sparse.issparse(c):
    c = c.todense()

  m = len(b)
  n = len(c)

  if not A.has_sorted_indices:
    A.sort_indices()
  Adata, Aindices, Acolptr = A.data, A.indices, A.indptr
  if A.shape != (m, n):
    raise ValueError('A shape not compatible with b,c')

  Pdata, Pindices, Pcolptr = None, None, None
  if 'P' in probdata:
    P = probdata['P']
    if P is not None:
      if not sparse.issparse(P):
        raise TypeError('P is required to be a sparse matrix')
      if P.shape != (n, n):
        raise ValueError('P shape not compatible with A,b,c')
      if not sparse.isspmatrix_csc(P):
        warn('Converting P to a CSC (compressed sparse column) matrix; '
             'may take a while.')
        P = P.tocsc()
      # extract upper triangular component only
      if sparse.tril(P, -1).data.size > 0:
        P = sparse.triu(P, format='csc')
      if not P.has_sorted_indices:
        P.sort_indices()
      Pdata, Pindices, Pcolptr = P.data, P.indices, P.indptr

  warm = {}
  if 'x' in probdata:
    warm['x'] = probdata['x']
  if 'y' in probdata:
    warm['y'] = probdata['y']
  if 's' in probdata:
    warm['s'] = probdata['s']
  if kwargs.pop('gpu', False):  # False by default
    if not kwargs.pop('use_indirect', _USE_INDIRECT_DEFAULT):
      raise NotImplementedError(
          'GPU direct solver not yet available, pass `use_indirect=True`.')
    import _scs_gpu
    return _scs_gpu.csolve((m, n), Adata, Aindices, Acolptr, Pdata, Pindices,
                           Pcolptr, b, c, cone, warm, **kwargs)

  if kwargs.pop('use_indirect', _USE_INDIRECT_DEFAULT):
    import _scs_indirect
    return _scs_indirect.csolve((m, n), Adata, Aindices, Acolptr, Pdata,
                                Pindices, Pcolptr, b, c, cone, warm, **kwargs)
  return _scs_direct.csolve((m, n), Adata, Aindices, Acolptr, Pdata, Pindices,
                            Pcolptr, b, c, cone, warm, **kwargs)

