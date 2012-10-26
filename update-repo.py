#!/usr/bin/python

import os, sys, stat, subprocess 

from optparse import OptionParser

usage = "usage: %prog [ --kvm | --openstack | --ovirt ]"
parser = OptionParser(usage=usage)
parser.add_option("-k", "--kvm", help="include the KVM repository module.",
                  default=False, action="store_true")
parser.add_option("-o", "--openstack", help="include the openstack repository module.",
                  default=False, action="store_true")
parser.add_option("-v", "--ovirt", help="include the ovirt repository module",
                  default=False, action="store_true")
(options, args) = parser.parse_args()

if options.kvm == True:
    from kvm_repository import repos, SRC_PREFIX 
else:
    if options.openstack == True:
        from openstack_repository import repos, SRC_PREFIX
    else:
        if options.ovirt == True:
            from ovirt_repository import repos, SRC_PREFIX
        
olddir = os.getcwd()
for folder, repo in repos:
    if os.path.isdir(folder):
        print "pulling sources from", folder
        os.chdir(folder)
        subprocess.call(["git", "pull"])
        subprocess.call(["git", "reset", "--hard", "master"])
    else:
        os.chdir(SRC_PREFIX)
        print "cloning sources from", repo
        subprocess.call(["git", "clone", repo, folder])
os.chdir(olddir)
