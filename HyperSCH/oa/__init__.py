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

from . import tcl_wrapper

oa = tcl_wrapper._oa()
#oa.tcl_exec("puts $tcl_version")
#oa.tcl_exec("puts [info patchlevel]")

oa.load_extension("win","x86_64")
