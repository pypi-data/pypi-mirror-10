"""
storlever.rest.network
~~~~~~~~~~~~~~~~

This module implements the rest API for network module.

:copyright: (c) 2014 by OpenSight (www.opensight.cn).
:license: AGPLv3, see LICENSE for more details.

"""


from storlever.rest.common import (get_view, post_view,
                                   put_view, delete_view)
from storlever.rest.common import get_params_from_request
from storlever.lib.exception import StorLeverError
from storlever.lib.schema import Schema, Optional, DoNotCare, \
    Use, IntVal, Default, SchemaError, BoolVal, StrRe, ListVal
from pyramid.response import FileResponse
from storlever.mngr.network import ifmgr
from storlever.mngr.network import netif
from pyramid.response import Response
from storlever.mngr.network import bond
from storlever.mngr.network import dnsmgr
from storlever.mngr.network import route
from storlever.mngr.system import sysinfo

def includeme(config):
    # network interface resource
    # GET:    interface information
    # POST:   start/stop interface
    # PUT:    modify interface parameter
    # DELETE: delete bound interface
    config.add_route('eth_list', '/network/eth_list')
    config.add_route('single_port', '/network/eth_list/{port_name}')
    config.add_route('port_stat', '/network/eth_list/{port_name}/stat')
    config.add_route('port_op', '/network/eth_list/{port_name}/op')
    config.add_route('bond_list', '/network/bond/bond_list')
    config.add_route('bond_port', '/network/bond/bond_list/{port_name}')
    config.add_route('dns', '/network/dns')
    config.add_route('host_list', '/network/host_list')
    config.add_route('route_tab', '/network/route_tab')
    config.add_route('route_tab6', '/network/route_tab6')

def get_port_info(netif_info):
    ip_info = netif_info.get_ip_config()
    property_info = netif_info.property_info
    link_state = netif_info.link_state
    port_info = {'name': netif_info.name,
                 'ip': ip_info[0],
                 'netmask': ip_info[1],
                 'gateway': ip_info[2],
                 'enabled': property_info["up"],
                 'is_bond_master': property_info["is_master"],
                 'is_bond_slave': property_info["is_slave"],
                 'mac': property_info["mac"],
                 'speed': link_state['speed'],
                 'linkup': link_state['link_up'],
                 'duplex': link_state['duplex'],
                 'auto': link_state['auto'],
                 }
    return port_info


#http://192.168.1.123:6543/storlever/api/v1/network/eth_list
@get_view(route_name='eth_list')
def network_get(request):
    eth_face = ifmgr.if_mgr()
    eth_list = eth_face.interface_name_list()
    eth_list_dict = []
    for port_name in eth_list:
        netif_info = eth_face.get_interface_by_name(port_name)
        port_info = get_port_info(netif_info)
        eth_list_dict.append(port_info)
    return eth_list_dict


#/network/eth_list/{port_name}
@get_view(route_name='single_port')
def get_single_port(request):
    port_name = request.matchdict['port_name']
    eth_face = ifmgr.if_mgr()
    netif_info = eth_face.get_interface_by_name(port_name)
    port_info = get_port_info(netif_info)
    return port_info


#/network/eth_list/{port_name}/stat
@get_view(route_name='port_stat')
def get_port_stat(request):
    port_name = request.matchdict['port_name']
    eth_face = ifmgr.if_mgr()
    netif_info = eth_face.get_interface_by_name(port_name)
    stat_info = netif_info.statistic_info
    return stat_info

port_mod_schema = Schema({
    Optional("ip"): StrRe(r"^(|\d+\.\d+\.\d+\.\d+)$"),  # ip addr
    Optional("netmask"): StrRe(r"^(|\d+\.\d+\.\d+\.\d+)$"),  # netmask addr
    Optional("gateway"): StrRe(r"^(|\d+\.\d+\.\d+\.\d+)$"), # gateway addr
    DoNotCare(Use(str)): object  # for all those key we don't care
})


#curl -v -X PUT  -d ip=192.168.0.222 -d gateway=192.168.1.1 -d netmask=255.255.0.0  http://192.168.1.123:6543/storlever/api/v1/network/eth_list/eth0
@put_view(route_name='single_port')
def modify_single_port(request):
    port_info = get_params_from_request(request, port_mod_schema)
    port_name = request.matchdict['port_name']
    eth_face = ifmgr.if_mgr()
    eth = eth_face.get_interface_by_name(port_name)
    eth.set_ip_config(ip=port_info.get("ip", None),
                      netmask=port_info.get("netmask", None),
                      gateway=port_info.get("gateway", None),
                      user=request.client_addr)
    return Response(status=200)


port_op_schema = Schema({
    Optional("opcode"): StrRe(r"^(enable|disable)$"),
    DoNotCare(Use(str)): object  # for all those key we don't care
})

#curl -v -X POST -d opcode=disable  http://192.168.1.123:6543/storlever/api/v1/network/eth_list/eth0/op
#enable eth* or disable eth*
@post_view(route_name='port_op')
def post_port_op(request):
    op_info = get_params_from_request(request, port_op_schema)
    port_name = request.matchdict['port_name']
    eth_face = ifmgr.if_mgr()
    eth = eth_face.get_interface_by_name(port_name)
    if op_info["opcode"] == "enable":
        eth.up(user=request.client_addr)
    elif op_info["opcode"] == "disable":
        eth.down(user=request.client_addr)
    return Response(status=200)

#curl -v -X GET  http://192.168.1.123:6543/storlever/api/v1/network/bond/bond_list
@get_view(route_name='bond_list')
def get_bond_list(request):
    bond_manager = bond.bond_mgr()
    bond_name_list = bond_manager.group_name_list()
    bond_info_dict = []
    
    for bond_name in bond_name_list:
        bond_object = bond_manager.get_group_by_name(bond_name)
        bond_info = {
            'name': bond_object.name,
            'mode': bond_object.mode,
            'miimon': bond_object.miimon,
            'slaves': bond_object.slaves
        }
        bond_info_dict.append(bond_info)
    return bond_info_dict

bond_add_schema = Schema({
    "mode": IntVal(0, 6),
    "miimon": IntVal(0, 65535),
    Optional("ifs"): Default(ListVal(Use(str)), default=[]),
    Optional("ip"): Default(StrRe(r"^(|\d+\.\d+\.\d+\.\d+)$"), default=""),  # ip addr
    Optional("netmask"): Default(StrRe(r"^(|\d+\.\d+\.\d+\.\d+)$"), default=""),  # netmask addr
    Optional("gateway"): Default(StrRe(r"^(|\d+\.\d+\.\d+\.\d+)$"), default=""),  # gateway addr
    DoNotCare(Use(str)): object  # for all those key we don't care
})

#curl -v -X POST -d ifs=eth0,eth1 -d ip=192.168.1.123 -d netmask=255.255.255.0 -d mode=1 -d miimon=1000 -d gateway=192.168.1.1 http://192.168.1.123:6543/storlever/api/v1/network/bond/bond_list
@post_view(route_name='bond_list')
def add_bond_group(request):
    params = get_params_from_request(request, bond_add_schema)
    bond_manager = bond.bond_mgr()
    bond_name = bond_manager.add_group(params['miimon'], params['mode'], params['ifs'],
                                       params['ip'], params['netmask'], params['gateway'],
                                       request.client_addr)

    resp = Response(status=201)
    resp.location = request.route_url('bond_port', port_name=bond_name)
    return resp


# /network/bond/bond_list/{port_name}
@get_view(route_name='bond_port')
def get_bond_port_info(request):
    bond_name = request.matchdict['port_name']
    bond_manager = bond.bond_mgr()
    bond_group = bond_manager.get_group_by_name(bond_name)

    bond_info = {
        'name': bond_group.name,
        'mode': bond_group.mode,
        'miimon': bond_group.miimon,
        'slaves': bond_group.slaves
    }

    return bond_info

bond_mod_schema = Schema({
    Optional("mode"): IntVal(0, 6),
    Optional("miimon"): IntVal(0, 65535),
    DoNotCare(Use(str)): object  # for all those key we don't care
})


#curl -v -X PUT -d mode=1  'http://192.168.1.123:6543/storlever/api/v1/network/bond_list/bond0'
@put_view(route_name='bond_port')
def modify_bond_group(request):
    bond_name = request.matchdict['port_name']
    params = get_params_from_request(request, bond_mod_schema)
    mode = params.get("mode")
    miimon = params.get("miimon")
    bond_manager = bond.bond_mgr()
    bond_group = bond_manager.get_group_by_name(bond_name)
    if mode is None:
        mode = bond_group.mode
    if miimon is None:
        miimon = bond_group.miimon
    bond_group.set_bond_config(miimon, mode, request.client_addr)
    return Response(status=200)


#curl -v -X delete  http://192.168.1.123:6543/storlever/api/v1/network/bond/bond_list/bond0
@delete_view(route_name='bond_port')
def delete_bond_group(request):
    bond_name = request.matchdict['port_name']
    bond_manager = bond.bond_mgr()
    bond_manager.del_group(bond_name, request.client_addr)
    return Response(status=200)



@get_view(route_name='dns')
def get_dns(request):
    dns_manager = dnsmgr.dns_mgr()
    servers = dns_manager.get_name_servers()
    dns_info = {
        "servers": servers
    }
    return dns_info


dns_mod_schema = Schema({
    Optional("servers"): Default(ListVal(StrRe(r"^(\d+\.\d+\.\d+\.\d+)$")), default=[]),
    DoNotCare(Use(str)): object  # for all those key we don't care
})


# curl -v -X put  -d servers=8.8.8.8,202.101.172.47  'http://192.168.1.123:6543/storlever/api/v1/network/dns'
@put_view(route_name='dns')
def modify_dns(request):
    params = get_params_from_request(request, dns_mod_schema)
    dns_manager = dnsmgr.dns_mgr()
    dns_manager.set_name_servers(params["servers"], request.client_addr)
    return Response(status=200)


@get_view(route_name='host_list')
def get_host_list(request):
    sys_mgr = sysinfo.sys_mgr()
    host_list = sys_mgr.get_host_list()
    return host_list

host_list_schema = Schema([{

    "addr": StrRe(r"^(\S)+$"),  # non-empty string

    "hostname": StrRe(r"^(\S)+$"),

    Optional("alias"): Default(Use(str), default=""),

    DoNotCare(Use(str)): object  # for all those key we don't care
}])

@put_view(route_name='host_list')
def put_host_list(request):
    params = get_params_from_request(request, host_list_schema)
    sys_mgr = sysinfo.sys_mgr()
    sys_mgr.set_host_list(params, request.client_addr)
    return Response(status=200)


@get_view(route_name='route_tab')
def get_route_tab(request):
    route_mgr = route.route_mgr()
    route_list = route_mgr.get_ipv4_route_list()
    return route_list

@get_view(route_name='route_tab6')
def get_route_tab6(request):
    route_mgr = route.route_mgr()
    route_list = route_mgr.get_ipv6_route_list()
    return route_list

