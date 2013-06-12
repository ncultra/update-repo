#!/usr/bin/python

## Qemu repositories

SRC_PREFIX="/Users/mdday/src/"

repos = [(SRC_PREFIX + "qemu/", "git://git.qemu.org/qemu.git"),
         (SRC_PREFIX + "qemu-kvm/", "git://git.kernel.org/pub/scm/virt/kvm/qemu-kvm.git"),
         (SRC_PREFIX + "qemu-rdma/", "git://github.com/hinesmr/qemu.git", "rdma"),
         (SRC_PREFIX + "qemu-agraf/", "git://github.com/agraf/qemu.git", "s390-for-upstream"),
         (SRC_PREFIX + "qemu-agraf/", "git://github.com/agraf/qemu.git", "ppc-for-upstream"),
         (SRC_PREFIX + "qemu-vfio/", "git://github.com/awilliam/qemu-vfio.git", "vfio-for-qemu"),
         (SRC_PREFIX + "qemu-aliguori/", "git://github.com/aliguori/qemu.git"),
         (SRC_PREFIX + "spice-spice", "git://anongit.freedesktop.org/spice/spice"),
         (SRC_PREFIX + "spice-qemu", "git://anongit.freedesktop.org/spice/qemu"),
         (SRC_PREFIX + "spice-common", "git://anongit.freedesktop.org/spice/spice-common"),
         (SRC_PREFIX + "spice-server", "git://anongit.freedesktop.org/spice/spice-server"),
         (SRC_PREFIX + "spice-protocol", "git://anongit.freedesktop.org/spice/spice-protocol") ]
# agraf also has a ppc-for-upstream branch
