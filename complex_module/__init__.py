"""
The public names defined by a module are determined by checking the module’s
namespace for a variable named __all__; if defined, it must be a sequence of
strings which are names defined or imported by that module. The names given in
__all__ are all considered public and are required to exist. If __all__ is not
defined, the set of public names includes all names found in the module’s
namespace which do not begin with an underscore character ('_'). __all__ should
contain the entire public API. It is intended to avoid accidentally exporting
items that are not part of the API (such as library modules which were imported
and used within the module).

https://docs.python.org/3/reference/simple_stmts.html#module.__all__
"""

__all__ = ["first", "second"]

# for backwards compatibility, also import
# from .first import *
# from .second import *
