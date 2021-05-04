# Tempory APT repo for virt-v2v

Mainly used by https://github.com/alvistack/ansible-role-libvirt

Also see:

  * https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=966675#20
  * https://github.com/vagrant-libvirt/vagrant-libvirt/issues/1256
  * https://github.com/savoury1/ubuntu-rolling/issues/1

## Installation

    #!/bin/bash

    set -euxo pipefail

    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 644E28D3
    sudo apt-add-repository "deb [arch=amd64] https://alvistack.github.io/libguestfs-virt-v2v stable main"
    sudo apt update
    sudo apt -y install virt-v2v
