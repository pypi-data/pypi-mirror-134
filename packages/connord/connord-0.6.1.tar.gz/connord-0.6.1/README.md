<h1 align="center">C&#xF8;nN&#xF8;rD</h1>
<h2 align="center">Connect to NordVPN servers secure and fast</h2>

<p align="center">
<a href="https://github.com/ambv/black"><img alt="Code Style: Black" src="https://img.shields.io/badge/code%20style-black-black.svg?style=flat-square"></a>
<a href="https://choosealicense.com/licenses/gpl-3.0/"><img alt="License" src="https://img.shields.io/badge/license-GPL--3.0--or--later-green.svg?style=flat-square"></a>
<a href="https://docs.python.org/"><img alt="Python Version" src="https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue.svg?style=flat-square"></a>
<a href="https://github.com/MaelStor/connord"><img alt="GitHub tag (latest SemVer)" src="https://img.shields.io/github/tag/MaelStor/connord.svg?style=flat-square"></a>
<a href="https://travis-ci.com/MaelStor/connord/"><img alt="Travis (.com) branch" src="https://img.shields.io/travis/com/MaelStor/connord/master.svg?style=flat-square"></a>
<a href="https://github.com/MaelStor/connord"><img alt="Coveralls github" src="https://img.shields.io/coveralls/github/MaelStor/connord.svg?style=flat-square"></a>
</p>

---

Connord connects to NordVPN servers by wrapping
[OpenVPN](https://openvpn.net/community-resources/#articles) and iptables. Most
tools, including the official nordvpn app do not allow customising iptables
properly. Often, iptables rules are left in a mess when finished and may even
lead to unexpected behaviour. Additionally, the native openvpn application lacks
kind of connection profiles, to easily switch between configurations depending
on your network you are currently using, for example on your laptop. Connord
connects you to NordVPN servers, wrapping openvpn and iptables to provide a
rich, powerful and simple to use tool chain orchestrated from the command line.

This tool is not for you, if you want to connect to nordvpn servers via NordLynx
or use other special nordvpn technologies. Connord connects you via openvpn over
the udp port 1196 or tcp port 443. If openvpn is patched correctly it connects
you to obfuscated servers. This should cover the most use cases, but it won't do
anything more... Use the official nordvpn tool instead if you wish to use
CyberSec etc.

However, compared to other tools, connord can deliver more information about
servers, areas, countries etc., easily accessible from the command line, with
its extensive filters. It also uses a powerful and yet simple mechanism to
determine the fastest NordVPN server for your location without gathering any
information about your exact place. It is less intrusive than other tools
because there is no need to install systemd services per default and just works
within your terminal.

## Version/Change notes

If you're already using connord and want to update from an earlier version it is
best to completely uninstall connord first. Then follow the Installation
instructions from this document. Connord is still under development and each
minor version (the `x` in `0.x.y`) difference is not backwards compatible. Save
your configuration files and adjust them to the new ones if necessary.
Currently, (as of `0.6.0`) only the `/etc/connord/config.yml` file has
additional configuration options. Iptables rules and fallback files still follow
the same scheme.

## Dependencies

- iptables
- openvpn
- Depending on what is installed: resolvconf or systemd-resolved
- and the python package dependencies of connord. See Installation section.

## Quick start guide

- Follow Installation instructions below
- Download or update the openvpn configuration files for nordvpn with
  `$ sudo connord update`.
- Execute `$ sudo connord connect -c YOUR_COUNTRY_CODE` and replace
  YOUR_COUNTRY_CODE with the country code of your current country. List all
  country codes with `$ connord list countries`. You will be asked for your
  username and password which are stored safely in
  `/etc/connord/openvpn/nordvpn/credentials`.

## Installation

Install the system dependencies depending on your distribution with

### Ubuntu/Debian

    $ sudo apt-get update
    $ sudo apt-get install iptables openvpn

### Archlinux

    $ sudo pacman -Sy iptables openvpn

For the up down scripts of openvpn there needs either `resolvconf` or
`systemd-resolved` to be installed and configured on your system. Connord
automatically detects which one is used. Other systems are currently not
natively supported, but by providing own `openvpn_up_down` scripts this can be
circumvented.

#### Installation from source

This is currently the recommended method to install connord, because it creates
all the directories needed in `/etc/connord` to get the most out of connord.

    $ git clone https://github.com/MaelStor/connord
    $ cd connord
    $ sudo make install

Remark, that this doesn't install the dependencies of connord, since your
distribution most likely offers packages for them, and this is usually the best
way to go, so you are best advised to install the dependencies of connord with
your distribution's package manager. In case you don't want to manage python
dependencies with the distribution's package manager, you can still install
connord with `pip` (See below). Installation of the python packages:

###### Ubuntu/Debian

    $ sudo apt-get install python3-cachetools python3-jinja2 python3-netaddr \
        python3-netifaces python3-progress python3-iptables python3-yaml \
        python3-requests python3-setuptools

###### Archlinux

You need to install the `python-iptables` package from the aur repository. So
for example with pacaur execute:

    $ sudo pacaur -Sy python-cachetools python-jinja python-netaddr \
        python-netifaces python-progress python-iptables python-yaml \
        python-requests python-setuptools

You can start right off or customize connord in `/etc/connord/config.yml` and
adjust the iptables rules in `/etc/connord/iptables/*`.

#### Installation of connord with pip

    $ pip install --user --upgrade connord

You need to run commands that need root access with

    $ sudo $(which connord) connect -c de

instead. Global installation although not recommended since this also installs
the dependencies of connord globally:

    $ sudo pip install --upgrade connord

## Configuration

All configuration files since version 0.5.0 reside in the `/etc/connord`
hierarchy. The configuration files are documented with the most recent
configuration values. Here just a quick overview to get started. 

The main configuration file is `/etc/connord/config.yml`. Iptables rules can be
adjusted in `/etc/connord/iptables/`.

#### The main configuration file: config.yml

The main configuration file in [YAML](https://yaml.org/) format. Every variable
set within this configuration file is exposed to .rules and .fallback 
iptables templates.

###### config.yml: iptables section

This section may look like this:

<pre>
iptables
  dns:
    # NordVPN
    - '103.86.99.100/32'
    - '103.86.96.100/32'
</pre>

Use these variables for example in 01-filter.rules:

<pre>
OUTPUT:
  policy: ACCEPT
  action: None
  rules:
{% for server in iptables.dns %}
  - dst: "{{ server }}"
    protocol: udp
    udp:
      dport: '53'
    target: ACCEPT
{% endfor %}
</pre>

what creates the following after rendering:

<pre>
OUTPUT:
  policy: ACCEPT
  action: None
  rules:
  - dst: '103.86.99.100/32'
    protocol: udp
    udp:
      dport: '53'
    target: ACCEPT
  - dst: '103.86.96.100/32'
    protocol: udp
    udp:
      dport: '53'
    target: ACCEPT
</pre>

Rendering is happening automatically, so no user side intervention is required.

###### config.yml: openvpn section

The settings which are used to start openvpn can be found in `config.yml`. For
an overview of all possible options see `$ man openvpn`. You just need to strip
off the leading '--' and place it somewhere in the openvpn section. Arguments
are written after `:` or if the option doesn't take any arguments place `True`
after `:`. Further reading
about [YAML Syntax](https://yaml.org/spec/1.1/spec.html). There's the special
keyword
`built-in`, which can be applied to:

- auth-user-pass
- scripts paths
    - name: up
    - name: down
    - name: ipchange

if you like to use the built-in paths, what is the default behaviour. If you
don't like to run a script say when openvpn goes down delete or comment out

<pre>
    - name: "down"
      path: "built-in"
      stage: "down"
      creates: "down.env"
</pre>

#### Iptables rules

The iptables rules reside in `/etc/connord/iptables`.

###### rules and fallback files

These files are [jinja2](http://jinja.pocoo.org/docs/2.10/) templates which are
rendered with the `config.yml` file and `.env` files created by the built-in
`up`, `down` and `ipchange` scripts when openvpn starts running.

###### Naming scheme

Let's take for example the rules file which shall be applied to netfilter's
`filter` table. `01-filter.rules`. The leading number isn't necessary, but that
way you can control the order when to apply the files. After the optional dash
follows the table name. The dash isn't needed when there is no leading number.
The suffix `.rules` causes the rules to be applied after successfully
establishing a connection to a server. The suffix `.fallback` causes the rules
to be applied when disconnecting from a server or after invocation of `connord
iptables flush`. If you're writing ipv6 rules for the `filter` table place them
in a file like `01-filter6.rules` or `01-filter6.fallback`.

#### Variables

Every variable you define or is already defined in `config.yml` is available in
iptables rules files. In addition to that the connord instance exposes the
following variables to `.rules` and `.fallback` files:

<pre>
vpn_remote      # the remote server ip address
vpn_protocol    # the protocol in use: udp or tcp
vpn_port        # may be 1194 (udp) or 443 (tcp)

gateway:
  ip_address    # the ip_address of the default gateway 
  interface     # the interface of the default gateway

lan:            # derived from the default gateway's interface
  inet:         # short for AF_INET
  - addr:       # the ip address of your LAN
    netmask:    # the netmask for your LAN
    broadcast:  # the broadcast address of your ipv4 LAN
  inet6:        # actually derived from AF_INET6
  - addr:       # (mostly one of) the ipv6 addresses
    netmask:    # the netmask for you LAN
  link:         # short for AF_LINK
  - addr:       # the MAC address of your LAN card
    broadcast:  # the broadcast address. Should be in most cases
                  ff:ff:ff:ff:ff:ff
</pre>

In `fallback` files `vpn_remote` is `0.0.0.0/0`, `vpn_protocol` is `udp` and
`vpn_port` is set to `1194`. Be aware that there can be more than one `inet` or
`inet6` addresses.

Variables exposed from OpenVPN scripts can be seen when starting connord not in
daemon mode. The list given here may be incomplete or too exhaustive for your
network and is therefore just an incomplete preview. Look at the output of
connord for your environment. For example here the variables from `up.env` when
the connection is started by openvpn.

<pre>
connord 'up' environment variables: '/var/run/connord/up.env'
up_args:
  - 'init'
  - '255.255.255.0'
  - '10.8.1.10'
  - '1590'
  - '1500'
  - 'tun1'
  - '/var/run/connord/up.env'
dhcp_option:
  dns:
    - '103.86.99.100'
    - '103.86.96.100'
dev: 'tun1'
ifconfig_broadcast: '10.8.1.255'
ifconfig_local: '10.8.1.10'
ifconfig_netmask: '255.255.255.0'
link_mtu: '1590'
route_net_gateway: '200.200.200.200'
route_vpn_gateway: '10.8.1.1'
script_context: 'init'
tun_mtu: '1500'
trusted_ip: '100.100.100.100'
trusted_port: '1194'
untrusted_ip: '100.100.100.100'
untrusted_port: '1194'
</pre>

Variables from OpenVPN scripts are only available in `.rules` files, not
`.fallback` files.

## Usage

Command-line options overwrite the configuration in `config.yml`. This is mostly
important for the openvpn command line options passed through to openvpn. To
connect to nordvpn servers and alter iptables rules connord needs to be executed
as root. Most subcommands, especially the list subcommand, do not need root
access.

#### Subcommands

First, list all possible commands with `$ connord --help`. Any sub command has a
help and can be accessed with `$ connord SUBCOMMAND --help`. Before connecting
to a server and execute connord with root rights, you may wish to play around
with connord commands and start with listing servers `$ connord list servers`.
See below for more information about the list subcommand.

#### Connect to NordVPN servers

Connecting to nordvpn servers is done with `$ sudo connord connect`. No further
options are required, but limiting the possible servers may be what you want if
you want a faster connection. However, connord tries its best to figure out the
best server. Internally it sorts the servers by load and then by their ping. 
Then it tries to connect to the server with the lowest load and lowest ping.

For instance, if limiting servers to the country you're living in is what you
want, pass the `--country COUNTRY_CODE` to the connect command. The country code
is a two letter abbreviation of a country. All possible country codes can be
listed with `$ connord list countries`.

There are many other options to filter the servers connord tries to connect to.
See `$ connord connect --help` for all possible options.

#### Manage Iptables

Managing iptables with connord can be done with `$ connord iptables ACTION`
where valid ACTIONs can be listed with `$ connord iptables --help`. Before
taking any action make sure to save your original iptables rules. This can be
done for example with `$ sudo iptables-save > /etc/iptables/iptables.rules`. For
your safety any connord command modifying system files and iptables rules needs
root access for example with sudo.

#### Listings

List all possible countries, features, categories (types), servers, iptables
rules etc. See what is possible with `$ connord list --help`. All sub commands
to the list command try to help with the usage of connord or provide additional
information about a topic.

###### Servers

Listing servers can be done with `$ connord list servers`. As with the connect
command, there are a lot of options to limit the servers in the output. The
output of the list command may help in figuring out which servers are available
or help with the connect command. Most options here are also available in the
connect command, so running the `list servers` command beforehand helps to
reduce the servers to the servers you really want to wish to connect to. More
help can be seen with `$ connord list servers --help`.

#### Update NordVPN server configuration files and the location database

Updating the configuration files and database must be done once after
installation and after that on a regular basis to ensure connord uses the latest
possible servers and correct openvpn configuration.

To do so, just execute `$ connord update`

## Supported FEATUREs:

Have a look at the output of `$ connord list features`

## Supported TYPEs:

All supported types are listed with `$ connord list categories`. The term
`types` and `categories` are used interchangeably

## General section

If you experience problems running connord, first try the same command in
verbose mode with

    connord -v COMMAND

or

    connord --verbose COMMAND

You should see in most cases where the error occurred. There may be still hard
to track bugs, please report them to the Issue board on
[Github](https://github.com/MaelStor/connord/issues).

Error messages are written to stderr in your shell. You can suppress error
messages with `-q` or `--quiet` if you like to.

Verbose mode of `openvpn` can be set in `config.yml` in the openvpn section or
at the command-line when using `connord connect` adding it to the openvpn
command with `-o '--verb 3'`.

## Obfuscated servers

In order to be able to connect to obfuscated servers you need to
[patch](https://github.com/clayface/openvpn_xorpatch) OpenVPN. For example the
repository of [Tunnelblick](https://github.com/Tunnelblick/Tunnelblick) includes
the patches in third_party/sources/openvpn. How this can be done is described
[here](https://www.reddit.com/r/nordvpn/comments/bsbxt6/how_to_make_nordvpn_obfuscated_servers_work_on/)
. I haven't patched my openvpn client, so I can't share experiences but above
solution is reported to work.

You can list obfuscated servers with `$ connord list servers -t obfuscated`.
Same scheme to finally connect to an obfuscated server for example located in
HongKong: `$ sudo connord connect -c hk -t obfuscated`.

## Development

Make sure to have `poetry` installed. Clone the repo and install the development
environment:

    $ git clone git@github.com:MaelStor/connord.git
    $ cd connord
    $ make develop

## Thanks

Thanks to Jonathan Wright @ https://github.com/jonathanio for his great
update-systemd-resolved
script (https://github.com/jonathanio/update-systemd-resolved)