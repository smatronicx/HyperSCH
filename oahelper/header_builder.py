#
# This file is part of HyperDE.
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
# along with HyperDE.  If not, see <https://www.gnu.org/licenses/>.
#

def SplitTemplate(line):
    # Split template at ,
    tlist = list()
    tval = ""
    tnested = 0
    for c in line:
        if c is ",":
            if tnested == 0:
                tlist.append(tval)
                tval = ""

            else:
                tval = tval + c
        else:
            if c is "<":
                tnested = tnested + 1

            if c is ">":
                tnested = tnested - 1

            tval = tval + c

    tlist.append(tval)
    return tlist

def GetClassName(line):
    # Get class name from line
    if "operator" in line:
        return None

    line = line.replace("class OpenAccess_4::", "")
    line = line.replace("OpenAccess_4::", "")

    tokens = line.split("::")
    tokens = tokens[0].split("<")
    return tokens[0].replace(" ", "")

def GetConstructors(line):
    if "~" in line:
        return None

    if "operator" in line:
        return None

    line = line.replace("class OpenAccess_4::", "")
    line = line.replace("OpenAccess_4::", "")

    tokens = line.split("::")
    tokens = tokens[0].split("<")
    class_name = tokens[0].replace(" ", "")
    tlist = list()
    if "<" in line:
        tokens = line.split("::")
        line = line.replace(tokens[0], class_name)

        if "<" in tokens[0]:
            tstr = tokens[0].replace(class_name, "")
            tstr = tstr.replace(" ","")
            tstr = tstr[1:-1]
            tlist = SplitTemplate(tstr)


    tokens = line.split("::")
    rtn = [class_name, tokens[1].strip(), len(tlist), tlist]
    return rtn

def GetDestructors(line):
    if "~" in line:

        line = line.replace("class OpenAccess_4::", "")
        line = line.replace("OpenAccess_4::", "")

        tokens = line.split("::")
        tokens = tokens[0].split("<")
        class_name = tokens[0].replace(" ", "")
        tlist = list()
        if "<" in line:
            tokens = line.split("::")
            line = line.replace(tokens[0], class_name)

        tokens = line.split("::")
        rtn = [class_name, tokens[1].strip()]
        return rtn

    return None

def SplitFunction(line):
    # Split template at ,
    tlist = list()
    tval = ""
    tnested = 0
    for c in line:
        if c is " ":
            if tnested == 0:
                tlist.append(tval)
                tval = ""

            else:
                tval = tval + c
        else:
            if c is "<":
                tnested = tnested + 1

            if c is "(":
                tnested = tnested + 1

            if c is ">":
                tnested = tnested - 1

            if c is ")":
                tnested = tnested - 1

            tval = tval + c

    tlist.append(tval)
    return tlist

def CheckBraces(line):
    # Check if there are more than 1 '(' in line
    tokens = line.split("(")
    if len(tokens) > 2:
        return 1

    return 0

def GetFunctions(line):
    flist = SplitFunction(line)
    ftype = " ".join(flist[0:-1])
    fdef = flist[-1]

    if not fdef.startswith("OpenAccess_4"):
        return None

    line = line.replace("class OpenAccess_4::", "")
    line = line.replace("OpenAccess_4::", "")

    flist = SplitFunction(line)
    ftype = " ".join(flist[0:-1])
    fdef = flist[-1]

    if "::" not in line:
        return None

    tokens = fdef.split("::")
    tokens = tokens[0].split("<")
    class_name = tokens[0].replace(" ", "")
    tlist = list()

    if "<" in line:
        tokens = fdef.split("::")
        line = fdef.replace(tokens[0], class_name)

        if "<" in tokens[0]:
            tstr = tokens[0].replace(class_name, "")
            tstr = tstr.replace(" ","")
            tstr = tstr[1:-1]
            tlist = SplitTemplate(tstr)


    rtn = [class_name, ftype + " " + fdef, len(tlist), tlist]
    return rtn


filename = "D:\\Codes\\HyperSCH\\HyperSCH\\oalib\\win\\oaBaseFunc.txt"

class_list = dict();
# Get all classes
with open(filename, 'r') as fp:
    for line in fp:
        fn = SplitFunction(line)
        rtn = CheckBraces(line)
        if rtn == 1:
            print line
            
        #if not line.startswith("OpenAccess_4"):
        if False:
            if "operator" not in line:
                if "vftable" not in line:
                    if "Schema" not in line:
                        if "default" not in line:
                            if not line.startswith("struct"):
                                if "oaHierGroupDef" in line:
                                    if "create" in line:
                                        #print fn
                                        print line
        if False:
        #if line.startswith("OpenAccess_4"):
            cname = GetClassName(line)
            if cname is not None:
                if cname not in class_list:
                    class_list[cname] = dict()
                    class_list[cname]["written"] = 0

exit(0)

all_lines_step0 = list()
with open(filename, 'r') as fp:
    # Get constructor
    for line in fp:
        if line.startswith("OpenAccess_4"):
            ctr = GetConstructors(line)
            if ctr is not None:
                cname = ctr[0]
                if "constructor" not in class_list[cname]:
                    class_list[cname]["constructor"] = dict()
                    class_list[cname]["template"] = dict()
                    class_list[cname]["template"]["count"] = ctr[2]

                    if ctr[2] != 0:
                        for i in range(0, ctr[2]):
                            temp = "T{}".format(i)
                            class_list[cname]["template"][temp] = list()

                ctrfn = ctr[1]
                ctrfnnospace = ctrfn.replace(" ", "")
                class_list[cname]["constructor"][ctrfnnospace] = ctrfn
                ctrtempcnt = ctr[2]
                ctrtemp = ctr[3]

                if ctrtempcnt == class_list[cname]["template"]["count"]:
                    for i in range(0, ctrtempcnt):
                        temp = "T{}".format(i)
                        tempv = ctrtemp[i].replace(" ","")
                        tempv = ctrtemp[i].replace("*","")
                        if tempv not in class_list[cname]["template"][temp]:
                            class_list[cname]["template"][temp].append(tempv)

                else:
                    print ctr
                    exit(0)
            else:
                all_lines_step0.append(line)
        else:
            all_lines_step0.append(line)

all_lines_step1 = list()
# Get destructor
for line in all_lines_step0:
    if line.startswith("OpenAccess_4"):
        ctr = GetDestructors(line)
        if ctr is not None:
            cname = ctr[0]
            if "destructor" not in class_list[cname]:
                class_list[cname]["destructor"] = dict()

            ctrfn = ctr[1]
            ctrfnnospace = ctrfn.replace(" ", "")
            class_list[cname]["destructor"][ctrfnnospace] = ctrfn

        else:
            all_lines_step1.append(line)
    else:
        all_lines_step1.append(line)

all_lines_step2 = list()
# Get function
for line in all_lines_step1:
    ctr = GetFunctions(line)
    if ctr is not None:
        cname = ctr[0]
        if "functions" not in class_list[cname]:
            class_list[cname]["functions"] = dict()

        ctrfn = ctr[1]
        ctrfnnospace = ctrfn.replace(" ", "")
        class_list[cname]["functions"][ctrfnnospace] = ctrfn

    else:
        all_lines_step2.append(line)

#print all_lines_step2
line = "OpenAccess_4::oaObserver<class OpenAccess_4::oaConstraintParam>::~oaObserver<class OpenAccess_4::oaConstraintParam>(void)\n"

print line
print GetDestructors(line)
