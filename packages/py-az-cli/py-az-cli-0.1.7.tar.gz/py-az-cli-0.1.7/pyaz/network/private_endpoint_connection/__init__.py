from ... pyaz_utils import _call_az

def approve(description=None, id=None, name=None, resource_group=None, resource_name=None, type=None):
    '''
    Approve a private endpoint connection.

    Optional Parameters:
    - description -- Comments for the approval.
    - id -- ID of the private endpoint connection
    - name -- Name of the private endpoint connection
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_name -- Name of the resource
    - type -- Type of the resource.
    '''
    return _call_az("az network private-endpoint-connection approve", locals())


def reject(description=None, id=None, name=None, resource_group=None, resource_name=None, type=None):
    '''
    Reject a private endpoint connection.

    Optional Parameters:
    - description -- Comments for the rejection.
    - id -- ID of the private endpoint connection
    - name -- Name of the private endpoint connection
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_name -- Name of the resource
    - type -- Type of the resource.
    '''
    return _call_az("az network private-endpoint-connection reject", locals())


def delete(id=None, name=None, resource_group=None, resource_name=None, type=None, yes=None):
    '''
    Delete a private endpoint connection.

    Optional Parameters:
    - id -- ID of the private endpoint connection
    - name -- Name of the private endpoint connection
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_name -- Name of the resource
    - type -- Type of the resource.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az network private-endpoint-connection delete", locals())


def show(id=None, name=None, resource_group=None, resource_name=None, type=None):
    '''
    Show a private endpoint connection.

    Optional Parameters:
    - id -- ID of the private endpoint connection
    - name -- Name of the private endpoint connection
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_name -- Name of the resource
    - type -- Type of the resource.
    '''
    return _call_az("az network private-endpoint-connection show", locals())


def list(id=None, name=None, resource_group=None, type=None):
    '''
    List all private endpoint connections.

    Optional Parameters:
    - id -- ID of the resource
    - name -- Name of the resource. If provided, --type and --resource-group must be provided too
    - resource_group -- Name of resource group. If provided, --name and --type must be provided too
    - type -- Type of the resource. If provided, --name and --resource-group must be provided too
    '''
    return _call_az("az network private-endpoint-connection list", locals())

