#!/usr/bin/env python

import os, sys
from pathlib import Path

tocfile = 'sidebar.yml'
newtocfile = tocfile + '.new'
backuptocfile = tocfile + '.orig'

def createtocfromdir(dir, indentlevel):
    retval = ''
    path = Path(dir)
    for p in sorted(path.iterdir()):
        if p.name[0] == '.' or p.name[0] == '_':
            pass
        elif p.suffix == ".md":
            retval += ' ' * indentlevel + '- ' + (str(p)) + '\n'
        elif p.is_dir():
            retval += ' ' * indentlevel + '- section: ' + (str(p)) + '\n'
            retval += ' ' * (indentlevel+2) + 'contents:' + '\n'
            retval += createtocfromdir(p, indentlevel+2)
        else:
            pass
    return retval

tocbody = createtocfromdir(".", 6)
print(f"tocbody({len(tocbody)}):\n--\n")
print(tocbody)
print("--")
if len(tocbody) < 4:
    print("exiting")
    sys.exit()

with open(newtocfile, "w") as f:
    print("website:",file=f)
    print("  sidebar:", file=f)
    print("    contents:", file=f)
    print(createtocfromdir(".", 6), file=f)
    
os.rename(tocfile, backuptocfile)
os.rename(newtocfile, tocfile)
