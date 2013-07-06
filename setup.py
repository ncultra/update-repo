#!/usr/bin/python

'''
setup.py [--bin <binary dir>] [--mod <module dir>] 

default /usr/local/bin, /usr/local/lib

'''

import os, sys, shutil, stat, glob
from optparse import OptionParser

binpath = "/usr/local/bin/"
modpath = "/usr/local/lib/"


usage_string = "usage: %prog [--bin <binary location>] [--mod <module location>]"
parser = OptionParser(usage=usage_string)
parser.add_option("-b", "--binary", help="location for binary",
                  default="/usr/local/bin/")
parser.add_option("-m", "--mod", help="location for repo modules", 
                  default="/usr/local/lib/")

(options, args) = parser.parse_args()

if options.binary:
    binpath = options.binary + "/"
if options.mod:
    modpath = options.mod + "/"

for f in ["update-repo.py", 
          "update-repo.sh", 
          "cscope-init.sh", 
          "buildtags.sh"]:
    print "copying " + f + " to " + binpath
    shutil.copy(f, binpath)
    print "chmod: " + f + " 0755"
    os.chmod(binpath + f, 0o755)

for f in glob.glob("*_repository.py"):
    print "copying " + f + " to " + modpath
    shutil.copy(f, modpath)
