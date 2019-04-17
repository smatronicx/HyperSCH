#
# This file is part of HyperSCH.
# Copyright (c) 2019 by Smatronicx.
# All Rights Reserved.
#
# HyperDE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HyperDE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HyperSCH.  If not, see <https://www.gnu.org/licenses/>.
#

# Wrapper around the Tcl functions

import os
import sys
import Tkinter

class _oa(object):
    # Class for oa functions
    def __init__(self):
        # Initialize
        self.tclsh = Tkinter.Tcl()

    def load_extension(self, ostype = "linux", arch = "x86_64"):
        # Load shared extenstion
        script_path = os.path.abspath(os.path.dirname(sys.argv[0]))
        oalib_path = os.path.join(script_path, "oalib", ostype, arch)
        os.environ['PATH'] = oalib_path + os.pathsep + os.environ['PATH']

        oalib_path = self.escape_string(oalib_path)
        self.tcl_exec("lappend", "auto_path", oalib_path)

        #self.tcl_exec("set dir ", oalib_path)
        #self.tcl_exec("package ifneeded oa 2.2 [list load [file join $dir oaTcl.dll] oa]")
        #self.tcl_exec("package require oa")
        self.tcl_exec("load oaTcl.dll oa")

    def tcl_exec(self, *argv):
        cmd = ""
        for arg in argv:
            cmd = cmd + arg + " "

        print cmd
        self.tclsh.eval(cmd)

    def escape_string(self, str):
        # Add quotes around string
        str = repr(str)
        str = str[1:-1]
        str = "\"" + str + "\""
        return str
