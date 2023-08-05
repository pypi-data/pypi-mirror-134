'''
Manage the Azure Network Watcher.
'''
from ... pyaz_utils import _call_az
from . import connection_monitor, flow_log, packet_capture, troubleshooting


def configure(locations, enabled=None, resource_group=None, tags=None):
    '''
    Configure the Network Watcher service for different regions.

    Required Parameters:
    - locations -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.

    Optional Parameters:
    - enabled -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network watcher configure", locals())


def list():
    '''
    List Network Watchers.
    '''
    return _call_az("az network watcher list", locals())


def test_ip_flow(direction, local, protocol, remote, vm, nic=None, resource_group=None):
    '''
    Test IP flow to/from a VM given the currently configured network security group rules.

    Required Parameters:
    - direction -- None
    - local -- None
    - protocol -- None
    - remote -- None
    - vm -- Name or ID of the VM to target. If the name of the VM is provided, the --resource-group is required.

    Optional Parameters:
    - nic -- Name or ID of the NIC resource to test. If the VM has multiple NICs and IP forwarding is enabled on any of them, this parameter is required.
    - resource_group -- Name of the resource group the target VM is in.
    '''
    return _call_az("az network watcher test-ip-flow", locals())


def test_connectivity(source_resource, dest_address=None, dest_port=None, dest_resource=None, headers=None, method=None, protocol=None, resource_group=None, source_port=None, valid_status_codes=None):
    '''
    Test if a connection can be established between a Virtual Machine and a given endpoint.

    Required Parameters:
    - source_resource -- None

    Optional Parameters:
    - dest_address -- None
    - dest_port -- None
    - dest_resource -- None
    - headers -- Space-separated list of headers in `KEY=VALUE` format.
    - method -- HTTP method to use.
    - protocol -- Protocol to test on.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source_port -- None
    - valid_status_codes -- Space-separated list of HTTP status codes considered valid.
    '''
    return _call_az("az network watcher test-connectivity", locals())


def show_next_hop(dest_ip, resource_group, source_ip, vm, nic=None):
    '''
    Get information on the 'next hop' of a VM.

    Required Parameters:
    - dest_ip -- Destination IPv4 address.
    - resource_group -- Name of the resource group the target VM is in.
    - source_ip -- Source IPv4 address.
    - vm -- Name or ID of the VM to target. If the name of the VM is provided, the --resource-group is required.

    Optional Parameters:
    - nic -- Name or ID of the NIC resource to test. If the VM has multiple NICs and IP forwarding is enabled on any of them, this parameter is required.
    '''
    return _call_az("az network watcher show-next-hop", locals())


def show_security_group_view(resource_group, vm):
    '''
    Get detailed security information on a VM for the currently configured network security group.

    Required Parameters:
    - resource_group -- Name of the resource group the target VM is in.
    - vm -- Name or ID of the VM to target. If the name of the VM is provided, the --resource-group is required.
    '''
    return _call_az("az network watcher show-security-group-view", locals())


def show_topology(location=None, resource_group=None, subnet=None, vnet=None):
    '''
    Get the network topology of a resource group, virtual network or subnet.

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - resource_group -- None
    - subnet -- Name or ID of the subnet to target. If name is used, --vnet NAME must also be supplied.
    - vnet -- Name or ID of the virtual network to target.
    '''
    return _call_az("az network watcher show-topology", locals())


def run_configuration_diagnostic(resource, destination=None, direction=None, parent=None, port=None, protocol=None, queries=None, resource_group=None, resource_type=None, source=None):
    '''
    Run a configuration diagnostic on a target resource.

    Required Parameters:
    - resource -- Name or ID of the target resource to diagnose. If an ID is given, other resource arguments should not be given.

    Optional Parameters:
    - destination -- Traffic destination. Accepted values are '*', IP address/CIDR, or service tag.
    - direction -- Direction of the traffic.
    - parent -- The parent path. (ex: virtualMachineScaleSets/vmss1)
    - port -- Traffic destination port. Accepted values are '*', port number (3389) or port range (80-100).
    - protocol -- Protocol to be verified on.
    - queries -- JSON list of queries to use. Use `@{path}` to load from a file.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type
    - source -- Traffic source. Accepted values are '*', IP address/CIDR, or service tag.
    '''
    return _call_az("az network watcher run-configuration-diagnostic", locals())

