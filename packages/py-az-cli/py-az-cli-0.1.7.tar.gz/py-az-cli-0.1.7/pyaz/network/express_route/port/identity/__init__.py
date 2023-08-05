from ..... pyaz_utils import _call_az

def assign(identity, name, resource_group, no_wait=None):
    '''
    Assign a managed service identity to an ExpressRoute Port

    Required Parameters:
    - identity -- Name or ID of the ManagedIdentity Resource
    - name -- ExpressRoute port name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network express-route port identity assign", locals())


def remove(name, resource_group, no_wait=None):
    '''
    Remove the managed service identity of an ExpressRoute Port

    Required Parameters:
    - name -- ExpressRoute port name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network express-route port identity remove", locals())


def show(name, resource_group):
    '''
    Show the managed service identity of an ExpressRoute Port

    Required Parameters:
    - name -- ExpressRoute port name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route port identity show", locals())

