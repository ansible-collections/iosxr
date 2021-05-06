# Cisco IOSXR Collection
[![CI](https://zuul-ci.org/gated.svg)](https://dashboard.zuul.ansible.com/t/ansible/project/github.com/ansible-collections/cisco.iosxr) <!--[![Codecov](https://img.shields.io/codecov/c/github/ansible-collections/vyos)](https://codecov.io/gh/ansible-collections/cisco.iosxr)-->

The Ansible Cisco IOSXR collection includes a variety of Ansible content to help automate the management of Cisco IOSXR network appliances.

This collection has been tested against Cisco IOSXR version 6.1.3.

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10**.

Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.
<!--end requires_ansible-->

### Supported connections
The Cisco IOSXR collection supports ``network_cli``  and ``netconf`` connections.

## Included content
<!--start collection content-->
### Cliconf plugins
Name | Description
--- | ---
[cisco.iosxr.iosxr](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_cliconf.rst)|Use iosxr cliconf to run command on Cisco IOS XR platform

### Filter plugins
Name | Description
--- | ---

### Inventory plugins
Name | Description
--- | ---

### Netconf plugins
Name | Description
--- | ---
[cisco.iosxr.iosxr](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_netconf.rst)|Use iosxr netconf plugin to run netconf commands on Cisco IOSXR platform

### Modules
Name | Description
--- | ---
[cisco.iosxr.iosxr_acl_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_acl_interfaces_module.rst)|ACL interfaces resource module
[cisco.iosxr.iosxr_acls](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_acls_module.rst)|ACLs resource module
[cisco.iosxr.iosxr_banner](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_banner_module.rst)|Manage multiline banners on Cisco IOS XR devices
[cisco.iosxr.iosxr_bgp](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_bgp_module.rst)|Configure global BGP protocol settings on Cisco IOS-XR
[cisco.iosxr.iosxr_bgp_address_family](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_bgp_address_family_module.rst)|Manages BGP Address Family resource module.
[cisco.iosxr.iosxr_bgp_global](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_bgp_global_module.rst)|Manages BGP global resource module.
[cisco.iosxr.iosxr_bgp_neighbor_address_family](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_bgp_neighbor_address_family_module.rst)|Manages BGP neighbor address family resource module.
[cisco.iosxr.iosxr_command](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_command_module.rst)|Run commands on remote devices running Cisco IOS XR
[cisco.iosxr.iosxr_config](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_config_module.rst)|Manage Cisco IOS XR configuration sections
[cisco.iosxr.iosxr_facts](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_facts_module.rst)|Get facts about iosxr devices.
[cisco.iosxr.iosxr_interface](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_interface_module.rst)|(deprecated, removed after 2022-06-01) Manage Interface on Cisco IOS XR network devices
[cisco.iosxr.iosxr_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_interfaces_module.rst)|Interfaces resource module
[cisco.iosxr.iosxr_l2_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_l2_interfaces_module.rst)|L2 interfaces resource module
[cisco.iosxr.iosxr_l3_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_l3_interfaces_module.rst)|L3 interfaces resource module
[cisco.iosxr.iosxr_lacp](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_lacp_module.rst)|LACP resource module
[cisco.iosxr.iosxr_lacp_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_lacp_interfaces_module.rst)|LACP interfaces resource module
[cisco.iosxr.iosxr_lag_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_lag_interfaces_module.rst)|LAG interfaces resource module
[cisco.iosxr.iosxr_lldp_global](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_lldp_global_module.rst)|LLDP resource module
[cisco.iosxr.iosxr_lldp_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_lldp_interfaces_module.rst)|LLDP interfaces resource module
[cisco.iosxr.iosxr_logging](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_logging_module.rst)|Configuration management of system logging services on network devices
[cisco.iosxr.iosxr_netconf](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_netconf_module.rst)|Configures NetConf sub-system service on Cisco IOS-XR devices
[cisco.iosxr.iosxr_ospf_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_ospf_interfaces_module.rst)|OSPF Interfaces Resource Module.
[cisco.iosxr.iosxr_ospfv2](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_ospfv2_module.rst)|OSPFv2 resource module
[cisco.iosxr.iosxr_ospfv3](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_ospfv3_module.rst)|ospfv3 resource module
[cisco.iosxr.iosxr_static_routes](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_static_routes_module.rst)|Static routes resource module
[cisco.iosxr.iosxr_system](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_system_module.rst)|Manage the system attributes on Cisco IOS XR devices
[cisco.iosxr.iosxr_user](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_user_module.rst)|Manage the aggregate of local users on Cisco IOS XR device

<!--end collection content-->

Click the ``Content`` button to see the list of content included in this collection.

## Installing this collection

You can install the Cisco IOSXR collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install cisco.iosxr

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: cisco.iosxr
```
## Using this collection


This collection includes [network resource modules](https://docs.ansible.com/ansible/latest/network/user_guide/network_resource_modules.html).

### Using modules from the Cisco IOSXR collection in your playbooks

You can call modules by their Fully Qualified Collection Namespace (FQCN), such as `cisco.iosxr.iosxr_l2_interfaces`.
The following example task replaces configuration changes in the existing configuration on a Cisco IOSXR network device, using the FQCN:

```yaml
---
 - name: Replace device configuration of specified L2 interfaces with provided configuration.
   cisco.iosxr.iosxr_l2_interfaces:
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

```

**NOTE**: For Ansible 2.9, you may not see deprecation warnings when you run your playbooks with this collection. Use this documentation to track when a module is deprecated.


### See Also:

* [Cisco IOSXR Platform Options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_iosxr.html)
* [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [Cisco IOSXR collection repository](https://github.com/ansible-collections/cisco.iosxr). See [Contributing to Ansible-maintained collections](https://docs.ansible.com/ansible/devel/community/contributing_maintained_collections.html#contributing-maintained-collections) for complete details.

You can also join us on:

- Freenode IRC - ``#ansible-network`` Freenode channel
- Slack - https://ansiblenetwork.slack.com

See the [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html) for details on contributing to Ansible.

### Code of Conduct
This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.

## Release notes

Release notes are available [here](https://github.com/ansible-collections/cisco.iosxr/blob/main/CHANGELOG.rst).

## Roadmap

<!-- Optional. Include the roadmap for this collection, and the proposed release/versioning strategy so users can anticipate the upgrade/update cycle. -->

## More information

- [Ansible network resources](https://docs.ansible.com/ansible/latest/network/getting_started/network_resources.html)
- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
