
#!/usr/bin/python

SRC_PREFIX="/Users/mdday/src/"

repos = [(SRC_PREFIX + "kvm/", "git://git.kernel.org/pub/scm/virt/kvm/kvm.git", 
          {"branch":"linux-next"}), 
         (SRC_PREFIX + "linux", "git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git"),
         (SRC_PREFIX + "linux-vfio/", "git://github.com/awilliam/linux-vfio.git", 
          {"branch": "vfio-vga-reset"}),
         (SRC_PREFIX + "glusterfs/", "git://git.gluster.com/glusterfs.git"),
         (SRC_PREFIX + "libstoragemgmt-code/", "git://git.code.sf.net/p/libstoragemgmt/code"),
         (SRC_PREFIX + "kvm-kmod/", "git://git.kiszka.org/kvm-kmod.git"),
         (SRC_PREFIX + "virtio-spec", "git://git.kernel.org/pub/scm/virt/kvm/mst/virtio-spec.git"),
         (SRC_PREFIX + "seabios", "git://git.kernel.org/pub/scm/virt/kvm/seabios.git"),
         (SRC_PREFIX + "vgabios", "git://git.kernel.org/pub/scm/virt/kvm/vgabios.git")]
