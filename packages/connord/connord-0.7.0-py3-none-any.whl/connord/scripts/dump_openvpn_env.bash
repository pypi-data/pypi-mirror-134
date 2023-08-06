#!/usr/bin/env bash

#
# Copyright (C) 2019-2022  Mael Stor <maelstor@posteo.de>
# GNU General Public License v3.0+
# See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt
#

# Ensure running script in openvpn environment
# shellcheck disable=SC2154
[[ "$script_type" ]] || exit 1

[[ "$1" ]] && dest_path="$1" || dest_path="/var/run/connord/${script_type}.env"

dest_dir="$(dirname "${dest_path}")"
mkdir -p "$dest_dir"
chmod 750 "$dest_dir"

NL=$'\n'

result=""
add_key_value() {
  result+="$(to_lower "$1"): '${2}'$NL"
}

add_list_key() {
  result+="$(to_lower "$1"):$NL"
}

indent() {
  count="$1"
  printf "%${count}s"
}

format_list_value() {
  echo "- '$1'"
}

has_key() {
  echo "$result" | grep -q "^$(to_lower "$1")"
}

key_insert() {
  key=$(to_lower "$1")
  val=$(to_lower "$2")
  ind=$(indent "$3")
  result=$(echo "$result" | sed '/^'"${key}"':$/ s:$:\n'"${ind}${val}\:"':')
  result+="$NL"
}

list_insert() {
  key=$(to_lower "$1")
  val=$(format_list_value "$2")
  ind=$(indent "$3")
  result=$(echo "$result" | sed '/^'"${key}"':$/ s:$:\n'"${ind}${val}"':')
  result+="$NL"
}

to_lower() {
  echo "$1" | tr '[:upper:]-' '[:lower:]_'
}

add_list_key "${script_type}_args"
for envvar in "$@"; do
  list_insert "${script_type}_args" "$envvar" "2"
done

for optname in ${!foreign_option_*}; do
  [ -n "${optname}" ] || break

  read -ra opts <<< "${!optname}"
  key=${opts[0]}
  value=${opts[1]}
  sec_value=${opts[2]}

  if [[ -z "$value" ]]; then
    id="push_reply"
    if has_key "$id"; then
      list_insert "$id" "$key" "2"
    else
      add_list_key "$id"
      list_insert "$id" "$key" "2"
    fi
  elif [[ -n "$sec_value" ]]; then
    if has_key "$key"; then
      if has_key "  $value"; then
        list_insert "  $value" "$sec_value" "4"
      else
        key_insert "$key" "$value" "2"
        list_insert "  $value" "$sec_value" "4"
      fi
    else
      add_list_key "$key"
      add_list_key "  $value"
      list_insert "  $value" "$sec_value" "4"
    fi
  else
    if ! has_key "$key"; then
      add_key_value "$key" "$value"
    fi
  fi
  unset key value sec_value
done

openvpn_env_vars=('ip_address' 'port_number' 'dev' 'dev_idx' 'ifconfig_broadcast'
  'ifconfig_ipv6_local' 'ifconfig_ipv6_netbits' 'ifconfig_ipv6_remote'
  'ifconfig_local' 'ifconfig_remote' 'ifconfig_netmask' 'ifconfig_pool_local_ip'
  'ifconfig_pool_netmask' 'ifconfig_pool_remote_ip' 'link_mtu' 'local'
  'local_port' 'proto' 'route_net_gateway' 'route_vpn_gateway' 'script_context'
  'time_ascii' 'time_duration' 'time_unix' 'tun_mtu' 'trusted_ip'
  'trusted_ip6' 'trusted_port' 'untrusted_ip' 'untrusted_ip6'
  'untrusted_port' 'redirect_gateway')

for var in "${openvpn_env_vars[@]}"; do
  [[ "${!var}" ]] && add_key_value "$var" "${!var}"
done

echo "connord '${script_type}' environment variables: '${dest_path}'"
echo "$result" | tee "${dest_path}" >&2

unset result
