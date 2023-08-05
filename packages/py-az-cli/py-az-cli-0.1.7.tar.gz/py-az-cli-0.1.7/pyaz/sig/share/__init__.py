'''
Manage gallery sharing profile
'''
from ... pyaz_utils import _call_az

def add(gallery_name, resource_group, no_wait=None, op_type=None, subscription_ids=None, tenant_ids=None):
    '''
    Share gallery with subscriptions and tenants

    Required Parameters:
    - gallery_name -- The name of the Shared Image Gallery.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - op_type -- distinguish add operation and remove operation
    - subscription_ids -- A list of subscription ids to share the gallery.
    - tenant_ids -- A list of tenant ids to share the gallery.
    '''
    return _call_az("az sig share add", locals())


def remove(gallery_name, resource_group, no_wait=None, op_type=None, subscription_ids=None, tenant_ids=None):
    '''
    stop sharing gallery with a subscription or tenant

    Required Parameters:
    - gallery_name -- The name of the Shared Image Gallery.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - op_type -- distinguish add operation and remove operation
    - subscription_ids -- A list of subscription ids to share the gallery.
    - tenant_ids -- A list of tenant ids to share the gallery.
    '''
    return _call_az("az sig share remove", locals())


def reset(gallery_name, resource_group, no_wait=None):
    '''
    disable gallery from being shared with subscription or tenant

    Required Parameters:
    - gallery_name -- The name of the Shared Image Gallery.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az sig share reset", locals())


def wait(gallery_name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of a shared gallery is met.

    Required Parameters:
    - gallery_name -- gallery name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az sig share wait", locals())

