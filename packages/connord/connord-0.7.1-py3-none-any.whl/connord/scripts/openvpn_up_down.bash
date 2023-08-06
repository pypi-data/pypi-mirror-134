#!/usr/bin/env bash

#
# Copyright (C) 2019-2022  Mael Stor <maelstor@posteo.de>
# GNU General Public License v3.0+
# See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt
#

# Ensure running script in openvpn environment
# shellcheck disable=2154
[[ "$script_type" ]] || exit 1

this_dir="$(dirname "$0")"

SYSTEMD=0
which systemctl > /dev/null 2>&1 && systemctl is-active systemd-resolved > /dev/null && SYSTEMD=1
RESOLVCONF=0
which resolvconf >/dev/null 2>&1 && RESOLVCONF=1

if [[ $SYSTEMD -eq 1 ]]; then
  "${this_dir}/openvpn_up_down_systemd.bash" "$@"
elif [[ $RESOLVCONF -eq 1 ]];then
  "${this_dir}/openvpn_up_down_resolvconf.bash" "$@"
else
  echo "Error: openvpn_up_down.bash: Cannot adjust dns settings: Aborting ..." >&2
  exit 1
fi
