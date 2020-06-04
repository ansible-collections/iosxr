#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The iosxr_ospfv2 class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from copy import deepcopy
from ansible.module_utils.six import iteritems
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.facts import (
    Facts,
)

from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.rm_templates.ospfv2 import (
    Ospfv2Template,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.resource_module import (
    ResourceModule,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
)
import q


class Ospfv2(ResourceModule):
    """
    The ios_ospfv2 class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["ospfv2"]

    def __init__(self, module):
        super(Ospfv2, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="ospfv2",
            tmplt=Ospfv2Template(),
        )

    def execute_module(self):
        """ Execute the module
        :rtype: A dictionary
        :returns: The result from module execution
        """
        self.gen_config()
        self.run_commands()

        return self.result

    def gen_config(self):
        """ Select the appropriate function based on the state provided
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        if self.want:
            wantd = {
                (entry["process_id"], entry.get("vrf")): entry
                for entry in self.want.get("processes", [])
            }
        else:
            wantd = {}
        if self.have:
            haved = {
                (entry["process_id"], entry.get("vrf")): entry
                for entry in self.have.get("processes", [])
            }
        else:
            haved = {}

        # turn all lists of dicts into dicts prior to merge
        for thing in wantd, haved:
            for _pid, proc in iteritems(thing):
                for area in proc.get("areas", []):
                    ranges = {
                        entry["address"]: entry
                        for entry in area.get("ranges", [])
                    }
                    if bool(ranges):
                        area["ranges"] = ranges
                    filter_list = {
                        entry["direction"]: entry
                        for entry in area.get("filter_list", [])
                    }
                    if bool(filter_list):
                        area["filter_list"] = filter_list
                    virtual_link = {
                        entry["id"]: entry
                        for entry in area.get("virtual_link", [])
                    }
                    if bool(virtual_link):
                        area["virtual_link"] = virtual_link
                proc["areas"] = {
                    entry["area_id"]: entry for entry in proc.get("areas", [])
                }
                if proc.get("distribute_list"):
                    if "acls" in proc.get("distribute_list"):
                        proc["distribute_list"]["acls"] = {
                            entry["name"]: entry
                            for entry in proc["distribute_list"].get(
                                "acls", []
                            )
                        }

        # if state is merged, merge want onto have
        if self.state == "merged":
            q(wantd)
            q(haved)
            wantd = dict_merge(haved, wantd)

        # if state is deleted, limit the have to anything in want
        # set want to nothing
        if self.state == "deleted":
            haved = {
                k: v for k, v in iteritems(haved) if k in wantd or not wantd
            }
            wantd = {}

        # delete processes first so we do run into "more than one" errors
        if self.state in ["overridden", "deleted"]:
            for k, have in iteritems(haved):
                if k not in wantd:
                    self.addcmd(have, "pid", True)

        for k, want in iteritems(wantd):
            self._compare(want=want, have=haved.pop(k, {}))

    def _compare(self, want, have):
        parsers = [
            "bfd",
            "cost",
            "weight",
            "passive",
            "priority",
            "protocol",
            "auto_cost",
            "flood_reduction",
            "default_metric",
            "router_id",
            "demand_circuit",
            "packet_size",
            "transmit_delay",
            "summary_in",
            "external_out",
            "dead_interval",
            "hello_interval",
            "authentication",
            "adjacency_stagger",
            "retransmit_interval",
            "mtu_ignore",
            "bfd.fast_detect",
            "capability",
            "capability.opaque",
            "admin_distance",
            "ospf_distance",
            "address_family_unicast",
            "authentication.message_digest",
            "default_information_originate",
            "loopback_stub_network",
        ]

        if want != have:
            self.addcmd(want or have, "pid", False)
            self.compare(parsers, want, have)
            self._areas_compare(want, have)

    def _areas_compare(self, want, have):
        q(want)
        q(have)
        wareas = want.get("areas", {})
        hareas = have.get("areas", {})
        q(wareas)
        q(hareas)
        for name, entry in iteritems(wareas):
            self._area_compare(want=entry, have=hareas.pop(name, {}))
        for name, entry in iteritems(hareas):
            self._area_compare(want={}, have=entry)

    def _area_compare(self, want, have):
        parsers = [
            "area.authentication",
            "area.authentication_key",
            "area.authentication.message_digest",
            "area.mpls_traffic_eng",
            "area.mpls_ldp",
            "area.bfd",
            "area.bfd.fast_detect",
            "area.nssa",
            "area.nssa.default_information_originate",
            "area.nssa.translate",
            "area.default_cost",
            "area.stub",
            "area.ranges",
            "area.cost",
            "area.dead_interval",
            "area.hello_interval",
            "area.transmit_delay",
            "area.mtu_ignore",
            "area.packet_size",
            "area.priority",
            "area.weight",
            "area.external_out",
            "area.summary_in",
            "area.demand_circuit",
            "area.passive",
        ]
        self.compare(parsers=parsers, want=want, have=have)
        self._areas_compare_virtual_link(want, have)
        self._area_compare_filters(want, have)

    def _areas_compare_virtual_link(self, want, have):
        q(want)
        q(have)
        wvlinks = want.get("virtual_link", {})
        hvlinks = have.get("virtual_link", {})
        q(wvlinks)
        q(hvlinks)
        for name, entry in iteritems(wvlinks):
            self._area_compare_virtual_link(want=entry, have=hvlinks.pop(name, {}))
        for name, entry in iteritems(hvlinks):
            self._area_compare_virtual_link(want={}, have=entry)

    def _area_compare_virtual_link(self, want, have):
        parsers = [
            "virtual_link.hello_interval",
        ]
        self.compare(parsers=parsers, want=want, have=have)

    def _area_compare_filters(self, wantd, haved):
        for name, entry in iteritems(wantd):
            h_item = haved.pop(name, {})
            if entry != h_item and name == "filter_list":
                filter_list_entry = {}
                filter_list_entry["area_id"] = wantd["area_id"]
                if h_item:
                    li_diff = [
                        item
                        for item in entry + h_item
                        if item not in entry or item not in h_item
                    ]
                else:
                    li_diff = entry
                filter_list_entry["filter_list"] = li_diff
                self.addcmd(filter_list_entry, "area.filter_list", False)
        for name, entry in iteritems(haved):
            if name == "filter_list":
                self.addcmd(entry, "area.filter_list", True)
