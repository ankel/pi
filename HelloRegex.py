import re, pdb

# common variables

rawstr = r"""(__.+__)"""
embedded_rawstr = r"""(__.+__)"""
matchstr = """#ifdef __GLUE_VER__
#ifndef __GLUE_BASE__
#define __GLUE_BASE__
#endif
#endif"""

# method 1: using a compile object
compile_obj = re.compile(rawstr)
match_obj = compile_obj.findall(matchstr)

# method 2: using search function (w/ external flags)
#match_obj = re.search(rawstr, matchstr)

# method 3: using search function (w/ embedded flags)
#match_obj = re.search(embedded_rawstr, matchstr)

# Retrieve group(s) from match_obj
#all_groups = match_obj.groups()

# Retrieve group(s) by index
#group_1 = match_obj.group(1)

pdb.set_trace()

