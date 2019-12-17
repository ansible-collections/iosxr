#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for iosxr_l2_interfaces
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

GENERATOR_VERSION = "1.0"

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "network",
}


DOCUMENTATION = """module: iosxr_l2_interfaces
short_description: Manage Layer-2 interface on Cisco IOS-XR devices
description: This module manages the Layer-2 interface attributes on Cisco IOS-XR
  devices.
author: Sumit Jaiswal (@justjais)
notes:
- Tested against Cisco IOS-XRv Version 6.1.3 on VIRL.
- This module works with connection C(network_cli). See L(the IOS-XR Platform Options,../network/user_guide/platform_iosxr.html).
options:
  config:
    description: A dictionary of Layer-2 interface options
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Full name of the interface/sub-interface excluding any logical unit number,
          e.g. GigabitEthernet0/0/0/1 or GigabitEthernet0/0/0/1.100.
        type: str
        required: true
      native_vlan:
        description:
        - Configure a native VLAN ID for the trunk
        type: int
      l2transport:
        description:
        - Switchport mode access command to configure the interface as a layer 2 access
        type: bool
      l2protocol:
        description:
        - Configures Layer 2 protocol tunneling and protocol data unit (PDU) filtering
          on an interface.
        type: list
        suboptions:
          cdp:
            description:
            - Cisco Discovery Protocol (CDP) tunneling and data unit parameters.
            choices:
            - drop
            - forward
            - tunnel
            type: str
          pvst:
            description:
            - Configures the per-VLAN Spanning Tree Protocol (PVST) tunneling and
              data unit parameters.
            choices:
            - drop
            - forward
            - tunnel
            type: str
          stp:
            description:
            - Spanning Tree Protocol (STP) tunneling and data unit parameters.
            choices:
            - drop
            - forward
            - tunnel
            type: str
          vtp:
            description:
            - VLAN Trunk Protocol (VTP) tunneling and data unit parameters.
            choices:
            - drop
            - forward
            - tunnel
            type: str
      q_vlan:
        description:
        - 802.1Q VLAN configuration. Note that it can accept either 2 VLAN IDs when
          configuring Q-in-Q VLAN, or it will accept 1 VLAN ID and 'any' as input
          list when configuring Q-in-any vlan as input. Note, that this option is
          valid only with respect to Sub-Interface and is not valid when configuring
          for Interface.
        type: list
      propagate:
        description:
        - Propagate Layer 2 transport events. Note that it will work only when the
          I(l2tranport) option is set to TRUE
        type: bool
  state:
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
    description:
    - The state of the configuration after module completion
    type: str
"""

EXAMPLES = """
---
# Using merged
#
# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
# !
# interface GigabitEthernet0/0/0/4
#  description Test description
# !

- name: Merge provided configuration with device configuration
  iosxr_l2_interfaces:
    config:
      - name: GigabitEthernet0/0/0/3
        native_vlan: 20
      - name: GigabitEthernet0/0/0/4
        native_vlan: 40
        l2transport: True
        l2protocol:
        - stp: tunnel
      - name: GigabitEthernet0/0/0/3.900
        l2transport: True
        q_vlan:
        - 20
        - 40
    state: merged

# After state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
#  dot1q native vlan 20
# !
# interface GigabitEthernet0/0/0/4
# description Test description
#  dot1q native vlan 10
#  l2transport
#   l2protocol stp tunnel
#  !
# !
# interface GigabitEthernet0/0/0/3.900 l2transport
#  dot1q vlan 20 40
# !

# Using replaced
#
# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
#  dot1q native vlan 20
# !
# interface GigabitEthernet0/0/0/4
# description Test description
#  dot1q native vlan 10
#  l2transport
#   l2protocol stp tunnel
#  !
# !
# interface GigabitEthernet0/0/0/3.900 l2transport
#  dot1q vlan 20 40
# !

- name: Replaces device configuration of listed interfaces with provided configuration
  iosxr_l2_interfaces:
    config:
      - name: GigabitEthernet0/0/0/4
        native_vlan: 40
        l2transport: True
        l2protocol:
        - stp: forward
      - name: GigabitEthernet0/0/0/3.900
        q_vlan:
        - 20
        - any
    state: replaced

# After state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
#  dot1q native vlan 20
# !
# interface GigabitEthernet0/0/0/4
# description Test description
#  dot1q native vlan 40
#  l2transport
#   l2protocol stp forward
#  !
# !
# interface GigabitEthernet0/0/0/3.900 l2transport
#  dot1q vlan 20 any
# !

# Using overridden
#
# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
#  dot1q native vlan 20
# !
# interface GigabitEthernet0/0/0/4
# description Test description
#  dot1q native vlan 10
#  l2transport
#   l2protocol stp tunnel
#  !
# !
# interface GigabitEthernet0/0/0/3.900 l2transport
#  dot1q vlan 20 40
# !

- name: Override device configuration of all interfaces with provided configuration
  iosxr_l2_interfaces:
    config:
      - name: GigabitEthernet0/0/0/4
        native_vlan: 40
        l2transport: True
        l2protocol:
        - stp: forward
      - name: GigabitEthernet0/0/0/3.900
        q_vlan:
        - 20
        - any
    state: overridden

# After state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
# !
# interface GigabitEthernet0/0/0/4
# description Test description
#  dot1q native vlan 40
#  l2transport
#   l2protocol stp forward
#  !
# !
# interface GigabitEthernet0/0/0/3.900
#  dot1q vlan 20 any
# !

# Using deleted
#
# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
#  dot1q native vlan 20
# !
# interface GigabitEthernet0/0/0/4
#  description Test description
#  dot1q native vlan 10
#  l2transport
#   l2protocol stp tunnel
#  !
# !
#

- name: "Delete L2 attributes of given interfaces (Note: This won't delete the interface itself)"
  iosxr_l2_interfaces:
    config:
      - name: GigabitEthernet0/0/0/4
    state: deleted

# After state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
#  dot1q native vlan 20
# !
# interface GigabitEthernet0/0/0/4
#  description Test description
# !

# Using Deleted without any config passed
# "(NOTE: This will delete all of configured resource module attributes from each configured interface)"
#
# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
#  dot1q native vlan 20
# !
# interface GigabitEthernet0/0/0/4
#  description Test description
#  dot1q native vlan 10
#  l2transport
#   l2protocol stp tunnel
#  !
# !

- name: "Delete L2 attributes of all interfaces (Note: This won't delete the interface itself)"
  iosxr_l2_interfaces:
    state: deleted

# After state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/3
#  description Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
# !
# interface GigabitEthernet0/0/0/4
#  description Test description
# !
"""

RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: The configuration returned will always be in the same format of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: The configuration returned will always be in the same format of the parameters above.
commands:
  description: The set of commands pushed to the remote device
  returned: always
  type: list
  sample: ['interface GigabitEthernet0/0/0/2', 'command 2', 'command 3']
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.l2_interfaces.l2_interfaces import (
    L2_InterfacesArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.config.l2_interfaces.l2_interfaces import (
    L2_Interfaces,
)


def main():
    """
    Main entry point for module execution
    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "overridden", ("config",)),
    ]

    module = AnsibleModule(
        argument_spec=L2_InterfacesArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
    )

    result = L2_Interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
