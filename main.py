# import complex_module.submodule.fourth  # doesn't work
# from complex_module.submodule import fourth # does not work because from _ import _ is for importing identifiers
# works because it's a file module
from complex_module.submodule.fourth import last_fn


import example_module
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
2. PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH), sys.path
3. The installation-dependent default (by convention usually /usr/local/lib/python/site-packages; consult the documentation for your platform for the exact location)

If none of these are found, Python will search each directory in the environment variable LD_LIBRARY_PATH (UNIX only) and each location specified in the environment variable PYTHONHOME.

The script directory is inserted before PYTHONPATH so that a program can modify sys.path by inserting there before executing a script.

'''


# import complex_module.first
# from modules import first # does the same thing

# on a directory module, imports the submodules, but not those submodules' functions directly
# see example_module for an example of importing all identifiers from a file module
from complex_module import *

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
