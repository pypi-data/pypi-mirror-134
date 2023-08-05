from ... pyaz_utils import _call_az
from . import categories, subscription


def create(name, resource, event_hub=None, event_hub_rule=None, export_to_resource_specific=None, logs=None, metrics=None, resource_group=None, resource_namespace=None, resource_parent=None, resource_type=None, storage_account=None, workspace=None):
    '''
    Create diagnostic settings for the specified resource.

    Required Parameters:
    - name -- None
    - resource -- Name or ID of the target resource.

    Optional Parameters:
    - event_hub -- None
    - event_hub_rule -- None
    - export_to_resource_specific -- Indicate that the export to LA must be done to a resource specific table, a.k.a. dedicated or fixed schema table, as opposed to the default dynamic schema table called AzureDiagnostics. This argument is effective only when the argument --workspace is also given.
    - logs -- None
    - metrics -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_namespace -- Target resource provider namespace.
    - resource_parent -- Target resource parent path, if applicable.
    - resource_type -- Target resource type. Can also accept namespace/type format (Ex: 'Microsoft.Compute/virtualMachines')
    - storage_account -- None
    - workspace -- None
    '''
    return _call_az("az monitor diagnostic-settings create", locals())


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
    return _call_az("az monitor diagnostic-settings show", locals())


def list(resource, resource_group=None, resource_namespace=None, resource_parent=None, resource_type=None):
    '''
    

    Required Parameters:
    - resource -- Name or ID of the target resource.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_namespace -- Target resource provider namespace.
    - resource_parent -- Target resource parent path, if applicable.
    - resource_type -- Target resource type. Can also accept namespace/type format (Ex: 'Microsoft.Compute/virtualMachines')
    '''
    return _call_az("az monitor diagnostic-settings list", locals())


def delete(name, resource, resource_group=None, resource_namespace=None, resource_parent=None, resource_type=None):
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
    return _call_az("az monitor diagnostic-settings delete", locals())


def update(name, resource, add=None, force_string=None, remove=None, resource_group=None, resource_namespace=None, resource_parent=None, resource_type=None, set=None):
    '''
    Update diagnostic settings.

    Required Parameters:
    - name -- The name of the diagnostic setting.
    - resource -- Name or ID of the target resource.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_namespace -- Target resource provider namespace.
    - resource_parent -- Target resource parent path, if applicable.
    - resource_type -- Target resource type. Can also accept namespace/type format (Ex: 'Microsoft.Compute/virtualMachines')
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az monitor diagnostic-settings update", locals())

