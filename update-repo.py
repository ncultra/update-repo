#!/usr/bin/python

import os, sys, stat, subprocess 
from imp import find_module, load_module
from optparse import OptionParser


def local_branch_exists(repo_spec):
# TODO: this is really bad duplication right now
    status = "false"
    folder = repo_spec[0][::]
    options = repo_spec[2]

    try:
        repo_branch = options["branch"]
        print "checking on existence of local branch: " + repo_branch
    except:
        print "repo_spec does not contain a branch option"
        return status
        
    olddir = os.getcwd()
    try:
        os.chdir(folder)
        local_branches = subprocess.check_output(["git", "branch"])
        print "local  branches: " + local_branches
        if repo_branch in local_branches:
            status = "true"
    except:
        print "folder does not contain a git repository"
    os.chdir(olddir) # overkill but no one is profiling for millisecond gains here
    return status

def remote_branch_exists(repo_spec):
    status = "false"
    folder = repo_spec[0][::]
    options = repo_spec[2]

    try:
        repo_branch = options["branch"]
        print "checking on existence of remote branch to track: " + repo_branch
    except:
        print "repo_spec does not contain a branch option"
        return status
        
    olddir = os.getcwd()
    try:
        os.chdir(folder)
        remote_branches = subprocess.check_output(["git", "branch", "-r"])
        print "remote branches: " + remote_branches
        if repo_branch in remote_branches:
            status = "true"
    except:
        print "folder does not contain a git repository"
    os.chdir(olddir) # overkill but no one is profiling for millisecond gains here
    return status

def apply_repo_options(repo_spec):
  folder = repo_spec[0][::]
  repo = repo_spec[1]

  # vanilla repo spec will have the base dir and the url 
  # as elements (len of 2)
  if len(repo_spec) is 3: # this repo spec has an options hash
      if (not os.path.isdir(folder)):
          raise Exception("Repo folder does not exist ... check repo spec")

      olddir = os.getcwd()
      os.chdir(folder)
      options = repo_spec[2]

      try:
          repo_branch = options["branch"]
          print "checking for remote branch origin/" + repo_branch
          remote_branch = remote_branch_exists(repo_spec)
          if "false" in remote_branch:
              raise Exception("remote branch does not exist ... check the repo spec")

          print "checking out (possibly first creating) tracking branch from origin/" + repo_branch
          local_branch = local_branch_exists(repo_spec)
          if "false" in local_branch:
              subprocess.call(["git", "branch", "--track", repo_branch, repo_branch]) 

          current_branch = subprocess.check_output(["git", "branch"])
          if ("* " + str(branch) in current_branch):
              pass
          else:
              subprocess.call(["git", "checkout", repo_branch ])                
          
          subprocess.call(["git", "branch", "-a"])

          repo_tag = options["tag"]
          print "creating or updating the ctags database for", repo
          os.system("buildtags.sh > TAGS")

          repo_cscope = options["cscope"]
          print "creating or updating the cscope database for", repo
          subprocess.call(["cscope-init.sh", folder])
      except:
          pass
      os.chdir(olddir)
      


def clone_repo(repo_spec):
# clone the repo on origin/master
#if repo options includes branch, check the existince of the branch on origin/
# if remote branch exists, then create and check out a  tracking branch    
    folder = repo_spec[0][::]
    if os.path.isdir(folder):
        raise Exception("Attempting to clone into a directory that already exists")
    
    repo = repo_spec[1][::]
    print "cloning sources from", repo
    subprocess.call(["git", "clone", repo, folder])

def pull_repo(repo_spec):
    folder = repo_spec[0][::]
    repo = repo_spec[1][::]
    olddir = os.getcwd()

# we already know that the repo folder exists

    try:
        os.chdir(folder)
        print ("pulling changes from " + repo)
        subprocess.call(["git", "pull", "origin"])
        subprocess.call(["git", "reset", "--hard", "origin"])
    except:
        print "unable to pull from " + repo + " " + str(branch) + " , check the repo spec"

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

for this_repo in repo_mod.repos:
    folder = this_repo[0][::]
    if os.path.isdir(folder):
        pull_repo(this_repo)
    else:
        clone_repo(this_repo)

    if len(this_repo) is 3: # this repo spec has an options hash
      apply_repo_options(this_repo)
  

