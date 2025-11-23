# import complex_module.submodule.fourth  # doesn't work
# from complex_module.submodule import fourth # does not work because from _ import _ is for importing identifiers
# works because it's a file module
from complex_module import *
from complex_module.submodule.fourth import last_fn


import example_module
from complex_module import add
print(add(2, 3))
# import example_module as em

# from example_module import square, cube, circumference, area
# from example_module import * # except those beginning with _ which are private, not recommended as you don't know which names are imported and defined, frowned upon
# in the two above, example_module is not defined in main's namespace

# from example_module import circumference as c


'''
Import path:

First sys.builtin_module_names is searched to see if the module is built-in
If not found, it will then search in a list of directories in the sys.path variable which is initialized from these locations:
1. The directory containing the input script (or current directory if none is specified)
2. PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH), sys.path is initialized to a default or overridden with this env var if set
3. The installation-dependent default (by convention usually /usr/local/lib/python/site-packages; consult the documentation for your platform for the exact location)

sys.path is modified by the running program to place its own directory at the beginning of the list

If none of these are found, Python will search each directory in the environment variable LD_LIBRARY_PATH (UNIX only) and each location specified in the environment variable PYTHONHOME.

The script directory is inserted before PYTHONPATH so that a program can modify sys.path by inserting there before executing a script.

'''


'''
Packages allow for "dotted module names", just as modules allow users to not worry about global identifiers colliding,
packages allow authors of multi-module packages from worrying about colliding module names

__init__.py is what makes python treat a directory as a package
It can be empty, or initialize things for the package, or define __all__

Note that when using from package import item, the item can be either a submodule (or subpackage) of the package,
or some other name defined in the package, like a function, class or variable. The import statement first tests
whether the item is defined in the package; if not, it assumes it is a module and attempts to load it.
If it fails to find it, an ImportError exception is raised.

from item.subitem.subsubitem (import object) all these items must be packages, the last one can be a package or a module

from package.subpackagewithsubpackages import * only imports the __all__ items from the subpackage, and doesn't do anything if __all__ is not defined,
since looking through the file system and importing everything dynamically would be slow and prone to unintended side effects

from package import specific_submodule is the recommended way to import a submodule of a package, give it an alias if colliding with a submodule from another package

if a subpackage needs to import from a submodule of a sibling subpackage, use an absolute import: from rootPackage import siblingSubpackage.specificSubmodule
you can also a relative import: from . import siblingSubpackageOrModule, from .. import siblingSubpackageOrModule, etc.
'''


# import complex_module.first
# from modules import first # does the same thing

# on a directory module, imports the submodules, but not those submodules' functions directly
# see example_module for an example of importing all identifiers from a file module

print(example_module.square(2))

# without complex_module/__init__.py the following do not work:

# print(complex_module.first.add(2, 3)) # doesn't work without explicitly importing first from complex_module
# print(complex_module.second.power(2, 3)) # same reason
# print(power(2, 3)) # also does not work

# with __init__.py __all__ defined, we can import * from complex_module the root and use functions by name directly
# because import * resolves to the modules that are in __all__
print(second.power(2, 3))


print(last_fn())


if __name__ == "__main__":
    print("This is the main module and being ran as a script")
