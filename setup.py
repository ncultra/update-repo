#!/usr/bin/python

'''
setup.py [--bin <binary dir>] [--mod <module dir>] 

default /usr/local/bin, /usr/local/lib

'''

import os, sys, shutil, stat
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

shutil.copy("update-repo.py", binpath)
os.chmod(binpath + "update-repo.py", 0o755)
shutil.copy("update-repo.sh", binpath)
os.chmod(binpath + "update-repo.sh", 0o755)

shutil.copy("kvm_repository.py", modpath)
shutil.copy("ovirt_repository.py", modpath)
shutil.copy("openstack_repository.py", modpath)
shutil.copy("libvirt_repository.py", modpath)
shutil.copy("gnulib_repository.py", modpath)
