from .... pyaz_utils import _call_az

def show(name, resource, resource_group=None, resource_namespace=None, resource_parent=None, resource_type=None):
    '''
    

    Required Parameters:
    - name -- The name of the diagnostic setting.
    - resource -- Name or ID of the target resource.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_namespace -- Target resource provider namespace.
    - resource_parent -- Target resource parent path, if applicable.
    - resource_type -- Target resource type. Can also accept namespace/type format (Ex: 'Microsoft.Compute/virtualMachines')
    '''
    return _call_az("az monitor diagnostic-settings categories show", locals())


def list(resource, resource_group=None, resource_namespace=None, resource_parent=None, resource_type=None):
    '''
    List the diagnostic settings categories for the specified resource.

    Required Parameters:
    - resource -- Name or ID of the target resource.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_namespace -- Target resource provider namespace.
    - resource_parent -- Target resource parent path, if applicable.
    - resource_type -- Target resource type. Can also accept namespace/type format (Ex: 'Microsoft.Compute/virtualMachines')
    '''
    return _call_az("az monitor diagnostic-settings categories list", locals())

