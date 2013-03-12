#!/usr/bin/python

import os, sys, stat, subprocess 
from imp import find_module, load_module
from optparse import OptionParser

usage="usage: %prog [options]. Repository is mandatory."
parser = OptionParser(usage)
parser.add_option("-r", "--repo", dest="repository", default="", 
                  help="module containing git repository URLs", metavar="REPOSITORY")
parser.add_option("-s", "--cscope", action="store_true", dest="cscope", default=False,
                  help="If used, program will generate a cscope database for the source repository")

parser.add_option("-t", "--ctags", action="store_true", dest="ctags", default=False, 
                  help="If used, program will generate a TAGS file for emacs indexing the repository.")

(options, args) = parser.parse_args()

if len(options.repository) < 1:
    parser.error("Must specify a git repository.")

file, pathname, description = find_module(options.repository)
try:
    repo_mod = load_module(options.repository, file, pathname, description)
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
    if os.path.isdir(folder):
        os.chdir(folder)
        buffer = subprocess.check_output(["git", "pull", "origin", branch])
        print ("pulling sources from " + repo + " origin " + branch + " ... " +  buffer)
        subprocess.call(["git", "reset", "--hard", branch])
    else:
        if not os.path.isdir(repo_mod.SRC_PREFIX):
            os.mkdir(repo_mod.SRC_PREFIX)
        os.chdir(repo_mod.SRC_PREFIX )
        print "cloning sources from", repo
        subprocess.call(["git", "clone", repo, folder])
    if options.cscope is True:
        print "rebuilding the cscope database"
        subprocess.call(["cscope-init.sh", folder])
    if options.ctags is True:
        print "\nrebuilding the ctags file\n"
        os.system("buildtags.sh > TAGS")
os.chdir(olddir)
