#!/usr/bin/env bash
#
# Copyright (C) 2022  Mael Stor <maelstor@posteo.de>
# GNU General Public License v3.0+
# See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt
#

# vim: set fileencoding=utf-8 :



# Ensure running script in openvpn environment
# shellcheck disable=2154
[[ "$script_type" ]] || exit 1

this_dir="$(dirname "$0")"

case "$script_type" in
  up)
    "${this_dir}/update-systemd-resolved"

    # shellcheck disable=1090
    source "${this_dir}/dump_openvpn_env.bash"
    ;;
  down)
    "${this_dir}/update-systemd-resolved"

    # shellcheck disable=1090
    source "${this_dir}/dump_openvpn_env.bash"
    ;;
esac
