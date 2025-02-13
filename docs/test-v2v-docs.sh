#!/bin/bash -
# libguestfs
# Copyright (C) 2016 Red Hat Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

set -e

source ../tests/functions.sh
set -e
set -x

skip_if_skipped

$srcdir/../podcheck.pl virt-v2v.pod virt-v2v \
  --path $srcdir/../common/options \
  --ignore=\
--debug-overlay,\
--ic,\
--if,\
--io,\
--ip,\
--it,\
--no-trim,\
--password-file,\
--oa,\
--oc,\
--of,\
--on,\
--oo,\
--op,\
--os,\
--vddk-config,\
--vddk-cookie,\
--vddk-libdir,\
--vddk-nfchostport,\
--vddk-port,\
--vddk-snapshot,\
--vddk-thumbprint,\
--vddk-transports,\
--vdsm-compat,\
--vdsm-image-uuid,\
--vdsm-ovf-flavour,\
--vdsm-ovf-output,\
--vdsm-vm-uuid,\
--vdsm-vol-uuid,\
--vmtype
