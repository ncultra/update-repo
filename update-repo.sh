#!/bin/bash

REPOS="kvm_repository ovirt_repository openstack_repository libvirt_repository gnulib_repository open_efs_repository"

for repo in $REPOS; do
    echo "updating $repo"
   update-repo.py -st  $repo
done
