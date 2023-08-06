from .... pyaz_utils import _call_az

def assign(gateway_name, identity, resource_group, no_wait=None):
    '''
    Assign a managed service identity to an application-gateway

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - identity -- Name or ID of the ManagedIdentity Resource
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway identity assign", locals())


def remove(gateway_name, resource_group, no_wait=None):
    '''
    Remove the managed service identity of an application-gateway

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway identity remove", locals())


def show(gateway_name, resource_group):
    '''
    Show the managed service identity of an application-gateway

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway identity show", locals())

