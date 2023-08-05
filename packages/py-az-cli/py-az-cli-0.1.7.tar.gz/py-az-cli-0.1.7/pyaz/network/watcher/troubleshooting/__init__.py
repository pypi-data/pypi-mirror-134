'''
Manage Network Watcher troubleshooting sessions.
'''
from .... pyaz_utils import _call_az

def start(resource, storage_account, storage_path, no_wait=None, resource_group=None, resource_type=None):
    '''
    Troubleshoot issues with VPN connections or gateway connectivity.

    Required Parameters:
    - resource -- Name or ID of the resource to troubleshoot.
    - storage_account -- None
    - storage_path -- None

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type
    '''
    return _call_az("az network watcher troubleshooting start", locals())


def show(resource, resource_group=None, resource_type=None):
    '''
    Get the results of the last troubleshooting operation.

    Required Parameters:
    - resource -- Name or ID of the resource to troubleshoot.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type
    '''
    return _call_az("az network watcher troubleshooting show", locals())

