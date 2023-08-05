from ... pyaz_utils import _call_az

def delete(name, resource_group, no_wait=None):
    '''
    Delete a virtual cluster.

    Required Parameters:
    - name -- The virtual cluster name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az sql virtual-cluster delete", locals())


def show(name, resource_group):
    '''
    Get the details for a virtual cluster.

    Required Parameters:
    - name -- The virtual cluster name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql virtual-cluster show", locals())


def list(resource_group=None):
    '''
    List available virtual clusters.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql virtual-cluster list", locals())

