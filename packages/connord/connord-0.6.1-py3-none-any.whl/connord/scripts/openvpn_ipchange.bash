#!/usr/bin/env bash

#
# Copyright (C) 2019-2022  Mael Stor <maelstor@posteo.de>
# GNU General Public License v3.0+
# See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt
#

# shellcheck disable=SC2154
[[ "$script_type" ]] || exit 2

# shellcheck disable=2034,2021
[[ "$2" ]] && ip_address="$(echo "$2" | tr -d '[AF_INET]' | cut -d' ' -f1)"
# shellcheck disable=2034
[[ "$2" ]] && port_number="$(echo "$2" | cut -d' ' -f2)"

this_dir="$(dirname "${BASH_SOURCE[0]}")"
source "${this_dir}/dump_openvpn_env.bash"
