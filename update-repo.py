#!/usr/bin/python

import os, sys, stat, subprocess 
from imp import find_module, load_module

if sys.argv.__len__() < 2:
    print "Usage: ", sys.argv[0]  + " <repository module>"
    sys.exit(1)

this_repo = sys.argv[1]
file, pathname, description = find_module(this_repo)
try:
    repo_mod = load_module(this_repo, file, pathname, description)
finally:
    if file:
        file.close()

olddir = os.getcwd()
for folder, repo in repo_mod.repos:
    if os.path.isdir(folder):
        print "pulling sources from", repo
        os.chdir(folder)
        subprocess.call(["git", "pull"])
        subprocess.call(["git", "reset", "--hard", "master"])
    else:
        if not os.path.isdir(repo_mod.SRC_PREFIX):
            os.mkdir(repo_mod.SRC_PREFIX)
        os.chdir(repo_mod.SRC_PREFIX )
        print "cloning sources from", repo
        subprocess.call(["git", "clone", repo, folder])
    subprocess.call(["cscope-init.sh", folder])
    os.system("buildtags.sh > TAGS")
os.chdir(olddir)
