from setuptools import setup, Extension
import os
import sys

# Build c modules
cpp_modules = ["oa2a"]
cpp_ext_modules = list()

script_path = os.path.abspath(os.path.dirname(sys.argv[0]))
cpp_modules_path = os.path.join(script_path, "HyperSCH","oa2")
include_path = cpp_modules_path

libpath = os.path.join(script_path, "build")

oalib_path = os.path.join(script_path, "oalib", "win", "x86_64")


for cmod in cpp_modules:
    mod_path = os.path.join(cpp_modules_path, cmod)

    src_files = list()
    src_files.append(os.path.join(mod_path, cmod) + ".i")

    for file in os.listdir(mod_path):
        if file.endswith(".cpp") and "_wrap" not in file:
            src_files.append(os.path.join(mod_path, file))

    ext_mod = Extension("_" + cmod, sources=src_files,
        include_dirs=[include_path],
        library_dirs=[oalib_path],
        libraries = ["oaBase"],
        extra_compile_args = ["/EHsc"],
        swig_opts=["-c++"])
    cpp_ext_modules.append(ext_mod)

# Set arguments
setup_path = sys.argv[0]
setup_cmd = None
if len(sys.argv) > 1:
    # Read setup command
    setup_cmd = sys.argv[1]

lib_path = os.path.join(script_path, "lib")
if setup_cmd == 'clean':
    # Clean build
    sys.argv = [setup_path, setup_cmd, '--all', '--build-lib', lib_path]
else:
    # Build
    sys.argv = [setup_path, 'build_ext', '--build-lib', lib_path]


setup(
    name="cppmodules",
    ext_modules=cpp_ext_modules,
    py_modules=cpp_modules
)
