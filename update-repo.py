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
updated = 0
global buffer
global branch

for this_repo in repo_mod.repos:
    folder = this_repo[0][::]
    repo = this_repo[1][::]
    if len(this_repo) is 3:
        branch = this_repo[2][::]
    else:
        branch = "master"
    print folder + " " + repo + " " + branch
    if os.path.isdir(folder):
        os.chdir(folder)
        print "executing command " + "git pull origin " + branch
        buffer = subprocess.check_output(["git", "pull", "origin", branch])
        print ("pulling sources from" +  " " + repo + "origin " + branch + " ... " +  buffer)
        subprocess.call(["git", "reset", "--hard", branch])
    else:
        if not os.path.isdir(repo_mod.SRC_PREFIX):
            os.mkdir(repo_mod.SRC_PREFIX)
        os.chdir(repo_mod.SRC_PREFIX )
        print "cloning sources from", repo
        subprocess.call(["git", "clone", repo, folder])
    if ("Already up-to-date.") in buffer:
        print "no update - skipping cscope and tags\n"
    else:
        print "rebuilding the cscope database"
        subprocess.call(["cscope-init.sh", folder])
        print "\nrebuilding the ctags file\n"
        os.system("buildtags.sh > TAGS")
os.chdir(olddir)
