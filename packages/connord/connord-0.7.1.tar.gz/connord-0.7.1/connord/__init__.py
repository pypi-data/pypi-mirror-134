# -*- coding: utf-8 -*-

#  Copyright (C) 2019-2022  Mael Stor <maelstor@posteo.de>
#  GNU General Public License v3.0+
#  See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

"""
Connord
-------

Connord connects you to NordVPN servers, wrapping openvpn and iptables to provide
a rich, powerful and simple to use tool chain orchestrated from the command line.

Basic usage:

    $ sudo connord connect --country us

This command tells connord to connect to the fastest and most stable server available in
the US. There are a lot more flags to filter servers to your liking. To mention one
more usage. Connect to the fastest servers best known to work with Netflix within the
US:

    $ sudo connord connect -c us --netflix

Discover the full documentation at https://github.com/MaelStor/connord

:copyright: (c) 2019-2022 by Mael Stor <maelstor@posteo.de>.
:license: GPLv3+, see LICENSE for more details.
"""

__version__ = "0.7.1"
__license__ = "GNU General Public License v3 or later (GPLv3+)"
__copyright__ = """connord  Copyright (C) 2019-2022  Mael Stor <maelstor@posteo.de>
This program comes with ABSOLUTELY NO WARRANTY; This is free software, and you
are welcome to redistribute it under certain conditions; See the LICENSE file
shipped with this software for details."""
