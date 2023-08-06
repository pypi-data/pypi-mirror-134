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
resolvconf='/sbin/resolvconf'
[[ -x "$resolvconf" ]] || exit 1

case "$script_type" in
  up)
    for optname in ${!foreign_option_*}; do
      [ -n "${optname}" ] || break

      read -ra opts <<< "${!optname}"
      opt=${opts[0]}
      _type=${opts[1]}
      remote=${opts[2]}

      [[ "${opt}" == "dhcp-option" ]] || continue
      if [[ "${_type}" == "DOMAIN" ]] || [[ "${_type}" == "DOMAIN-SEARCH" ]]; then
        result="search ${remote}\n${result}"
      elif [ "${_type}" = "DNS" ]; then
        result+="nameserver ${remote}\n"
      fi
    done
    # echo -ne "$result" | "$resolvconf" -a "${dev}.openvpn"
    echo -ne "$result" > /etc/resolv.conf

    # shellcheck disable=1090
    source "${this_dir}/dump_openvpn_env.bash"

    chattr +i /etc/resolv.conf
    ;;
  down)
    "$resolvconf" -d "${dev}.openvpn"

    # shellcheck disable=1090
    source "${this_dir}/dump_openvpn_env.bash"

    chattr -i /etc/resolv.conf
    ;;
esac
