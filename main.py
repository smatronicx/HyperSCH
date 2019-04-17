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

#from HyperSCH.oa import oa
import os
import sys

script_path = os.path.abspath(os.path.dirname(sys.argv[0]))
oalib_path = os.path.join(script_path, "oalib", "win", "x86_64")
print oalib_path
os.environ['PATH'] = oalib_path + os.pathsep + os.environ['PATH']
lib_path = os.path.join(script_path, "lib")
print lib_path
sys.path.append(lib_path)
sys.path.append(oalib_path)
os.environ['PATH'] = lib_path + os.pathsep + os.environ['PATH']

#import oahelper.header_builder

#oahelper.header_builder

#import HyperSCH.oa2.oa2c.oa2c as oa2c

#WRAPPIT <dll> <txt> <convention> <point dll name> <cpp> <def>
#move wsock32.dll wsock32_.dll
#dumpbin /exports wsock32_.dll > exports.txt
#wrappit wsock32.dll exports.txt __stdcall .\\wsock32_.dll wsock32.cpp wsock32.def
#print oa2c.mainfn("")

#import HyperSCH.oa2.oa2a.oa2a as oa2a

#oas = oa2a.oaString("Hello??")
#print oas.getLength()

#print "done"
#import HyperSCH.oa as oa
