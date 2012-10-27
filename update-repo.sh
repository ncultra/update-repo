#/bin/bash

REPOS="kvm ovirt openstack"

for repo in $REPOS; do
    update-repo.py --$repo
done
