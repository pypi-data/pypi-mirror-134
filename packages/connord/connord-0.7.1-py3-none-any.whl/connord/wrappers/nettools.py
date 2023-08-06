# -*- coding: utf-8 -*-

#  Copyright (C) 2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.wrappers.nettools
-------------------------

This module provides utilities around networking.
"""
import re
import subprocess
from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool
from typing import Any, Dict, List, Optional, Tuple

import netaddr  # type: ignore
import netifaces  # type: ignore

from connord.exceptions import ConnordError


def get_default_gateway(ipv6: bool = False) -> Tuple[Optional[str], Optional[str]]:
    """Returns a tuple with ipaddress and interface of the default gateway.

    :param ipv6: If true return ip6 address and interface else ip4 address
    :raises IptablesError: If there is no default gateway.
    :returns: a tuple with (ip_address, interface) on success or (None, None) on failure
    """
    try:
        default_gateway: dict = netifaces.gateways()["default"]
    except KeyError:
        raise ConnordError("Could not find a default gateway. Are you connected?")

    if ipv6:
        try:
            gateway = default_gateway[netifaces.AF_INET6]
            return gateway
        except KeyError:
            return None, None

    try:
        gateway = default_gateway[netifaces.AF_INET]
        return gateway
    except KeyError:
        return None, None


def get_gateways() -> Dict[str, Any]:
    try:
        gateways: dict = netifaces.gateways()
        default_gateway: dict = gateways["default"]
    except KeyError:
        raise ConnordError("Could not find a default gateway. Are you connected?")

    result = {
        "default": default_gateway[netifaces.AF_INET]
        if netifaces.AF_INET in default_gateway
        else (None, None),
        "default_inet6": default_gateway[netifaces.AF_INET]
        if netifaces.AF_INET6 in default_gateway
        else (None, None),
        "other": [],
        "other_inet6": [],
    }

    if netifaces.AF_INET in gateways:
        for ipaddress, iface, default in gateways[netifaces.AF_INET]:
            if not default:
                result["other"].append((ipaddress, iface))

    if netifaces.AF_INET6 in gateways:
        for ipaddress, iface, default in gateways[netifaces.AF_INET6]:
            if not default:
                result["other_inet6"].append((ipaddress, iface))

    return result


def get_interface_addresses(iface: str) -> dict:
    """Returns the iface addresses as dictionary of the given interface."""
    iface_addresses = netifaces.ifaddresses(iface)

    default_iface_dict = {}
    try:
        default_iface_dict["link"] = iface_addresses[netifaces.AF_LINK]
    except KeyError:
        pass

    try:
        default_iface_dict["inet"] = iface_addresses[netifaces.AF_INET]
    except KeyError:
        pass

    try:
        default_iface_dict["inet6"] = iface_addresses[netifaces.AF_INET6]
    except KeyError:
        pass

    return default_iface_dict


def ping(ip_address: str) -> Dict[str, float]:
    """
    Ping an ip address
    :param ip_address: the ip address to be pinged
    :returns: ping
    """

    pattern = re.compile(r"rtt .* = ([\d.]+)/([\d.]+)/([\d.]+)/.* ms")
    with subprocess.Popen(
        ["ping", "-q", "-n", "-c", "1", "-l", "1", "-W", "1", ip_address],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ) as ping_:

        out, _ = ping_.communicate()
        mat = pattern.search(out.decode())
        if mat:
            result = float(mat.group(2))
        else:
            result = float("inf")
        return {ip_address: result}


def ping_servers_parallel(ip_addresses: List[str]) -> Dict[str, float]:
    """
    Ping a list of ip addresses
    :param ip_addresses: The list of ip addresses as string
    :returns: List of pings
    """
    worker_count = cpu_count() + 1
    with ThreadPool(processes=worker_count) as pool:
        results = []
        for ip_address in ip_addresses:
            results.append(pool.apply_async(ping, (ip_address,)))

        pinged_servers: Dict[str, float] = {}
        for result in results:
            pinged_servers.update(result.get())

        return pinged_servers


def iprange_to_cidr(iprange: str) -> str:
    return str(netaddr.IPNetwork(iprange).cidr)
