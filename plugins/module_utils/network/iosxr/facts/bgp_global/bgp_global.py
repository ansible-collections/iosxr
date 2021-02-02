# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The iosxr bgp_global fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.rm_templates.bgp_global import (
    Bgp_globalTemplate,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.bgp_global.bgp_global import (
    Bgp_globalArgs,
)

class Bgp_globalFacts(object):
    """ The iosxr bgp_global facts class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Bgp_globalArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for Bgp_global network resource

        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf

        :rtype: dictionary
        :returns: facts
        """
        facts = {}
        objs = []

        if not data:
            data = connection.get('show running-config router bgp')
            #vrf_data = self._flatten_config(data, "vrf")
            neighbor_data = self._flatten_config(data, "neighbor")
            data = self._flatten_config(neighbor_data, "rpki server")

            # remove address_family configs from bgp_global
            bgp_global_config = []
            start = False
            confederation_peers = ""
            for bgp_line in data.splitlines():
                if "address-family" in bgp_line:
                    start = True
                if not start:
                    bgp_global_config.append(bgp_line)
                if start and '!' in bgp_line:
                    start = False

        """
            for bgp_line in bgp_global_config:
                if "confederation peers" in bgp_line:
                    start = True
                if start:
                    confederation_peers += bgp_line
                if start and '!' in bgp_line:
                    start = False
            bgp_global_config.append(confederation_peers)
        """

        # parse native config using the Bgp_global template
        bgp_global_parser = Bgp_globalTemplate(lines=bgp_global_config)
        objs = bgp_global_parser.parse()

        vrfs = objs.get("vrfs", {})

        # move global vals to their correct position in facts tree
        # this is only needed for keys that are valid for both global
        # and VRF contexts
        global_vals = vrfs.pop("vrf_", {})
        for key, value in iteritems(global_vals):
            if objs.get(key):
                objs[key].update(value)
            else:
                objs[key] = value
        # transform vrfs into a list
        if vrfs:
            objs["vrfs"] = sorted(
                list(objs["vrfs"].values()), key=lambda k, sk="vrf": k[sk]
            )
            for vrf in objs["vrfs"]:
                self._post_parse(vrf)
        else:
            objs["vrfs"] = []

        self._post_parse(objs)


        ansible_facts['ansible_network_resources'].pop('bgp_global', None)

        params = utils.remove_empties(
            utils.validate_config(self.argument_spec, {"config": objs})
        )
        #import epdb;epdb.serve()

        facts['bgp_global'] = params.get("config", {})
        ansible_facts['ansible_network_resources'].update(facts)

        return ansible_facts

    def _flatten_config(self, data, context):
        """ Flatten neighbor contexts in
            the running-config for easier parsing.
        :param obj: dict
        :returns: flattened running config
        """
        data = data.split("\n")
        in_nbr_cxt = False
        cur_nbr = {}

        for x in data:
            cur_indent = len(x) - len(x.lstrip())
            if x.strip().startswith(context):
                in_nbr_cxt = True
                cur_nbr["nbr"] = x
                cur_nbr["indent"] = cur_indent
            elif cur_nbr and (cur_indent <= cur_nbr["indent"]):
                in_nbr_cxt = False
            elif in_nbr_cxt:
                data[data.index(x)] = cur_nbr["nbr"] + " " + x.strip()
        return "\n".join(data)

    def _post_parse(self, obj):
        """ Converts the intermediate data structure
            to valid format as per argspec.
        :param obj: dict
        """
        #import epdb;
        #epdb.serve()
        neighbors = obj.get("neighbors", [])
        if neighbors:
            obj["neighbors"] = sorted(
                list(neighbors.values()),
                key=lambda k, sk="neighbor": k[sk],
            )
        rpki_servers = obj.get("rpki", {}).get("servers", [])
        #import epdb;epdb.serve()
        if rpki_servers:
            obj["rpki"]["servers"] = sorted(
                list(rpki_servers.values()),
                key=lambda k, sk="name": k[sk],
            )
