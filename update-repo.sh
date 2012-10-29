#/bin/bash

REPOS="kvm_repository ovirt_repository openstack_repository"

for repo in $REPOS; do
    update-repo.py $repo
done
