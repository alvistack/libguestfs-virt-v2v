%global debug_package %{nil}

Name: virt-v2v
Epoch: 100
Version: 1.45.99
Release: 1%{?dist}
Summary: Convert a virtual machine to run on KVM
License: GPLv2+
URL: https://github.com/libguestfs/virt-v2v/tags
Source0: %{name}_%{version}.orig.tar.gz
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150000
BuildRequires: libcapstone-devel
BuildRequires: libjansson-devel
BuildRequires: qemu-tools
%else
BuildRequires: capstone-devel
BuildRequires: jansson-devel
BuildRequires: qemu-img
%endif
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bash-completion
BuildRequires: fuse-common
BuildRequires: fuse3
BuildRequires: gcc
BuildRequires: kernel
BuildRequires: libguestfs-devel >= 1.42
BuildRequires: libnbd-devel
BuildRequires: libosinfo-devel
BuildRequires: libtool
BuildRequires: libverto-devel
BuildRequires: libverto-libevent
BuildRequires: libvirt-devel
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: nbdkit
BuildRequires: nbdkit-python-plugin
BuildRequires: ncurses-devel
BuildRequires: ocaml >= 4.01
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-libguestfs-devel
BuildRequires: ocaml-libnbd-devel
BuildRequires: pcre2-devel
BuildRequires: pkgconfig
BuildRequires: po4a
BuildRequires: selinux-policy-minimum
BuildRequires: sqlite
BuildRequires: unzip
BuildRequires: xorriso
BuildRequires: zip
Requires: curl
Requires: edk2-ovmf
Requires: gawk
Requires: guestfs-tools >= 1.42
Requires: gzip
Requires: kernel
Requires: selinux-policy-minimum
Requires: libguestfs >= 1.42
Requires: libguestfs-xfs
Requires: unzip

%description
Virt-v2v converts a single guest from a foreign hypervisor to run on
KVM. It can read Linux and Windows guests running on VMware, Xen,
Hyper-V and some other hypervisors, and convert them to KVM managed by
libvirt, OpenStack, oVirt, Red Hat Virtualisation (RHV) or several other
targets. It can modify the guest to make it bootable on KVM and install
virtio drivers so it will run quickly.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
autoreconf -i
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check

%package -n virt-v2v-bash-completion
Summary: Bash tab-completion for virt-v2v
BuildArch: noarch
Requires: bash-completion >= 2.0
Requires: virt-v2v = %{epoch}:%{version}-%{release}

%description bash-completion
Install this package if you want intelligent bash tab-completion for
virt-v2v.

%files
%doc README
%license COPYING
%{_bindir}/virt-v2v
%{_datadir}/locale/*/LC_MESSAGES/virt-v2v.mo
%{_mandir}/*/man1/virt-v2v*.1*
%{_mandir}/man1/virt-v2v*.1*

%files -n virt-v2v-bash-completion
%license COPYING
%{_datadir}/bash-completion/completions/virt-v2v

%changelog
