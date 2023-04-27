from os import listdir, mkdir
from os.path import join
from pathlib import Path


ddir = '__data__'
hdir = Path.home()
pdir = join(hdir, ddir)
if ddir in listdir(hdir): pass
else: mkdir(pdir)