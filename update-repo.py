#!/usr/bin/python

import os, sys, stat, subprocess 
from imp import find_module, load_module
from optparse import OptionParser

def clone_repo(repo_spec):
# someone has already confirmed the src dir and it is our working dir

# clone the repo on origin/master
#if repo options includes branch, check the existince of the branch on origin/
    # if remote branch exists, then create and check out a  tracking branch    
    folder = repo_spec[0][::]
    if os.path.isdir(folder):
        raise Exception("Attempting to clone into a directory that already exists")
    
    repo = repo_spec[1][::]
    print "cloning sources from", repo
    subprocess.call(["git", "clone", repo, folder])

    olddir = os.getcwd()
    os.chdir(folder)

    if len(repo) is 3:
        options = repo_spec[2]
        try:
            repo_branch = options["branch"]
            if len(repo_branch) is not 0:
                # TODO: check if the remote branch exists
                print "creating and checking out tracking branch from origin/" + repo_branch
                subprocess.call(["git", "branch", "--track", repo_branch, "origin/" + repo_branch]) 
                subprocess.call(["git", "checkout", repo_branch ])                

            repo_tag = options["tag"]
            if len(repo_tag) is not 0:
                print "creating or updating the ctags database for", repo
                os.system("buildtags.sh > TAGS")
            
            repo_cscope = options["cscope"]
            if len(repo_cscope) is not 0:
                print "create or updating the cscope database for", repo
                subprocess.call(["cscope-init.sh", folder])

        except:
            continue
    
    
    os.chdir(olddir)    



usage="usage: %prog [options] REPOSITORY\n" \
"\t where REPOSITORY is a python module containing information\n"  \
"\t about the remote git repository and branch, as well as the\n" \
"\t local source directory."

parser = OptionParser(usage)

parser.add_option("-s", "--cscope", action="store_true", dest="cscope", default=False,
                  help="If used, program will generate a cscope database for the source repository.")

parser.add_option("-t", "--ctags", action="store_true", dest="ctags", default=False, 
                  help="If used, program will generate a TAGS file for emacs indexing the repository.")

(options, args) = parser.parse_args()

if len(args) < 1:
    parser.error("Must specify a git repository.")

file, pathname, description = find_module(args[0])
try:
    repo_mod = load_module(args[0], file, pathname, description)
finally:
    if file:
        file.close()

olddir = os.getcwd()
updated = 0
global buffer
global branch
global tag
global cscope

for this_repo in repo_mod.repos:
    branch = "origin/master"
    tag = "no"
    cscope = "no"
    folder = this_repo[0][::]
    repo = this_repo[1][::]
    if len(this_repo) is 3:
        repo_options = this_repo[2]
        try:
            branch = repo_options["branch"]
            tag = repo_options["tag"]
            cscope = repo_options["cscope"]
        except:
            continue

    if os.path.isdir(folder):
        os.chdir(folder)
        print ("pulling sources from " + repo + " " + str(branch) + " ... " )
        buffer = subprocess.check_output(["git", "pull", str(branch)])
        subprocess.call(["git", "reset", "--hard", str(branch)])
    else:
        if not os.path.isdir(repo_mod.SRC_PREFIX):
            os.mkdir(repo_mod.SRC_PREFIX)
        os.chdir(repo_mod.SRC_PREFIX )
        print "cloning sources from", repo
        subprocess.call(["git", "clone", repo, folder])
    if (options.cscope is True) or ("yes" in str(cscope)):
        print "rebuilding the cscope database"
        subprocess.call(["cscope-init.sh", folder])
    if (options.ctags is True) or ("yes" in str(tag)):
        print "\nrebuilding the ctags file\n"
        os.system("buildtags.sh > TAGS")
os.chdir(olddir)
