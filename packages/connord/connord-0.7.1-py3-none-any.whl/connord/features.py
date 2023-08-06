# -*- coding: utf-8 -*-

#  Copyright (C) 2019-2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
connord.features
----------------

This module provides classes and functions to manage server features.
"""
from typing import List

from connord.exceptions import FeatureError
from connord.formatter import Formatter

FEATURES = {
    "ikev2": "IKEv2/IPSec Protocol",
    "openvpn_udp": "UDP",
    "openvpn_tcp": "TCP",
    "socks": "Socks 5",
    "proxy": "HTTP Proxy",
    "pptp": "PPTP",
    "l2tp": "L2TP/IPSec",
    "openvpn_xor_udp": "OpenVPN UDP Obfuscated",
    "openvpn_xor_tcp": "OpenVPN TCP Obfuscated",
    "proxy_cybersec": "HTTP Proxy CyberSec",
    "proxy_ssl": "HTTP Proxy (SSL)",
    "proxy_ssl_cybersec": "HTTP CyberSec Proxy (SSL)",
    "ikev2_v6": "IKEv2/IPSec IPv6",
    "openvpn_udp_v6": "UDPv6",
    "openvpn_tcp_v6": "TCPv6",
    "wireguard_udp": "WireGuard UDP",
    "openvpn_udp_tls_crypt": "UDP TLS encryption",
    "openvpn_tcp_tls_crypt": "TCP TLS encryption",
    "openvpn_dedicated_udp": "Dedicated UDP",
    "openvpn_dedicated_tcp": "Dedicated TCP",
    "skylark": "Skylark",
    "mesh_relay": "Mesh Relay",
}


class Feature:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Feature):
            return self.name == other.name

        return False


def verify_features(features: List[str]) -> bool:
    """
    Verify if features are valid.

    :param features: List of features.
    :returns: True if all features are valid or else raises an exception.
    :raises FeatureError: raises a FeatureError if the format of the features
                          were invalid

    """

    wrong_features = []
    for feature in features:
        if feature not in FEATURES:
            wrong_features.append(feature)

    if wrong_features:
        raise FeatureError(f"Wrong server features: {wrong_features!s}")

    return True


class FeaturesPrettyFormatter(Formatter):
    """Format Features in pretty format"""

    def format_headline(self, sep: str = "=") -> str:
        features_header = "Server Features"
        return self.center_string(features_header, sep)

    @staticmethod
    def format_feature(feature: str, description: str) -> str:
        return f"  {feature:26}{description}"


def to_string(stream: bool = False) -> str:
    """Gather all features in a printable string

    :param stream: If True print to stdout else print to 'formatter.output' variable
    :returns: Formatted string if stream is False else an empty string
    """

    formatter = FeaturesPrettyFormatter()
    file_ = formatter.get_stream_file(stream)

    headline = formatter.format_headline()
    print(headline, file=file_)

    for feature, description in FEATURES.items():
        formatted_feature = formatter.format_feature(feature, description)
        print(formatted_feature, file=file_)

    print(formatter.format_ruler(sep="-"), file=file_)
    return formatter.get_output()


def print_features():
    """Prints all features to stdout"""
    to_string(stream=True)
