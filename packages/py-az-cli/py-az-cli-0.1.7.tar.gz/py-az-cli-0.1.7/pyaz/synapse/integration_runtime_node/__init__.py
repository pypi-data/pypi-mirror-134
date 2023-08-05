from ... pyaz_utils import _call_az

def show(name, node_name, resource_group, workspace_name):
    '''
    Get self-hosted integration runtime node information.

    Required Parameters:
    - name -- The integration runtime name.
    - node_name -- The integration runtime node name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse integration-runtime-node show", locals())


def update(auto_update, name, node_name, resource_group, update_delay_offset, workspace_name):
    '''
    Update self-hosted integration runtime node.

    Required Parameters:
    - auto_update -- Enable or disable the self-hosted integration runtime auto-update.
    - name -- The integration runtime name.
    - node_name -- The integration runtime node name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - update_delay_offset -- The time of the day for the self-hosted integration runtime auto-update.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse integration-runtime-node update", locals())


def delete(name, node_name, resource_group, workspace_name, yes=None):
    '''
    Remove a self-hosted integration runtime node.

    Required Parameters:
    - name -- The integration runtime name.
    - node_name -- The integration runtime node name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse integration-runtime-node delete", locals())


def get_ip_address(name, node_name, resource_group, workspace_name):
    '''
    Get self-hosted integration runtime node ip.

    Required Parameters:
    - name -- The integration runtime name.
    - node_name -- The integration runtime node name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse integration-runtime-node get-ip-address", locals())

