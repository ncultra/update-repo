#!/usr/bin/python

## Qemu repositories

SRC_PREFIX="/Users/mdday/src/"

repos = [(SRC_PREFIX + "qemu/", "git://git.qemu.org/qemu.git"),
         (SRC_PREFIX + "qemu-kvm/", "git://git.kernel.org/pub/scm/virt/kvm/qemu-kvm.git"),
         (SRC_PREFIX + "qemu-rdma/", "git://github.com/hinesmr/qemu.git", {"branch": "rdma"}),
         (SRC_PREFIX + "qemu-agraf/", "git://github.com/agraf/qemu.git", {"branch": "s390-for-upstream"}),
         (SRC_PREFIX + "qemu-agraf/", "git://github.com/agraf/qemu.git", {"branch": "ppc-for-upstream"}),
         (SRC_PREFIX + "qemu-vfio/", "git://github.com/awilliam/qemu-vfio.git", {"branch":"vfio-for-qemu"}),
         (SRC_PREFIX + "qemu-aliguori/", "git://github.com/aliguori/qemu.git"),
         (SRC_PREFIX + "qemu-bonzini/", "git://github.com/bonzini/qemu.git", {"branch":"rcu"})]
