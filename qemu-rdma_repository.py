#!/usr/bin/python

## specialized Qemu repositories

SRC_PREFIX="/Users/mdday/src/"

repos = [[(SRC_PREFIX + "qemu/", "git://git.qemu.org/qemu.git"),
         (SRC_PREFIX + "qemu-aliguori/", "git://github.com/aliguori/qemu.git"),
         (SRC_PREFIX + "qemu-bonzini/", "git://github.com/bonzini/qemu.git"),
         (SRC_PREFIX + "qemu-rdma/", "git://github.com/hinesmr/qemu.git", "rdma"),
         (SRC_PREFIX + "qemu-agraf/", "git://github.com/agraf/qemu.git", "s390-for-upstream"),
         (SRC_PREFIX + "qemu-agraf/", "git://github.com/agraf/qemu.git", "ppc-for-upstream"),
         (SRC_PREFIX + "qemu-vfio/", "git://github.com/awilliam/qemu-vfio.git", "vfio-for-qemu")]
# agraf also has a ppc-for-upstream branch
