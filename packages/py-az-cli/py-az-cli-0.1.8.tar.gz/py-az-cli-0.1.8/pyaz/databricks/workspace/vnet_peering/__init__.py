from .... pyaz_utils import _call_az

def create(name, remote_vnet, resource_group, workspace_name, allow_forwarded_traffic=None, allow_gateway_transit=None, allow_virtual_network_access=None, no_wait=None, use_remote_gateways=None):
    '''
    Create a vnet peering for a workspace.

    Required Parameters:
    - name -- The name of the vnet peering.
    - remote_vnet -- The remote virtual network name or Resource ID.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace.

    Optional Parameters:
    - allow_forwarded_traffic -- Whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network.
    - allow_gateway_transit -- If gateway links can be used in remote virtual networking to link to this virtual network.
    - allow_virtual_network_access -- Whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space.
    - no_wait -- Do not wait for the long-running operation to finish.
    - use_remote_gateways -- If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway.
    '''
    return _call_az("az databricks workspace vnet-peering create", locals())


def update(name, resource_group, workspace_name, allow_forwarded_traffic=None, allow_gateway_transit=None, allow_virtual_network_access=None, no_wait=None, use_remote_gateways=None):
    '''
    Update the vnet peering.

    Required Parameters:
    - name -- The name of the vnet peering.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace.

    Optional Parameters:
    - allow_forwarded_traffic -- Whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network.
    - allow_gateway_transit -- If gateway links can be used in remote virtual networking to link to this virtual network.
    - allow_virtual_network_access -- Whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space.
    - no_wait -- Do not wait for the long-running operation to finish.
    - use_remote_gateways -- If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway.
    '''
    return _call_az("az databricks workspace vnet-peering update", locals())


def delete(name, resource_group, workspace_name, no_wait=None):
    '''
    Delete the vnet peering.

    Required Parameters:
    - name -- The name of the vnet peering.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az databricks workspace vnet-peering delete", locals())


def list(resource_group, workspace_name):
    '''
    List vnet peerings under a workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace.
    '''
    return _call_az("az databricks workspace vnet-peering list", locals())


def show(name, resource_group, workspace_name):
    '''
    Show the vnet peering.

    Required Parameters:
    - name -- The name of the vnet peering.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace.
    '''
    return _call_az("az databricks workspace vnet-peering show", locals())


def wait(name, resource_group, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the Databricks workspace vnet peering is met.

    Required Parameters:
    - name -- The name of the vnet peering.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az databricks workspace vnet-peering wait", locals())

