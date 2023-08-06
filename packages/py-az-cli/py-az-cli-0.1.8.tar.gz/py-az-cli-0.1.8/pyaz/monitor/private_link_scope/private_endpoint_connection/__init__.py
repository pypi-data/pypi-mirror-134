from .... pyaz_utils import _call_az

def show(id=None, name=None, resource_group=None, scope_name=None):
    '''
    Show a private endpoint connection of a private link scope resource.

    Optional Parameters:
    - id -- The ID of the private endpoint connection associated with the private link scope. You can get it using `az monitor private-link-scope show`.
    - name -- The name of the private endpoint connection associated with the private link scope.
    - resource_group -- The resource group name of specified private link scope.
    - scope_name -- Name of the Azure Monitor Private Link Scope.
    '''
    return _call_az("az monitor private-link-scope private-endpoint-connection show", locals())


def list(resource_group, scope_name):
    '''
    List all private endpoint connections of a private link scope resource.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scope_name -- Name of the Azure Monitor Private Link Scope.
    '''
    return _call_az("az monitor private-link-scope private-endpoint-connection list", locals())


def approve(description=None, id=None, name=None, resource_group=None, scope_name=None):
    '''
    Approve a private endpoint connection of a private link scope resource.

    Optional Parameters:
    - description -- Comments for approve operation.
    - id -- The ID of the private endpoint connection associated with the private link scope. You can get it using `az monitor private-link-scope show`.
    - name -- The name of the private endpoint connection associated with the private link scope.
    - resource_group -- The resource group name of specified private link scope.
    - scope_name -- Name of the Azure Monitor Private Link Scope.
    '''
    return _call_az("az monitor private-link-scope private-endpoint-connection approve", locals())


def reject(description=None, id=None, name=None, resource_group=None, scope_name=None):
    '''
    Reject a private endpoint connection of a private link scope resource.

    Optional Parameters:
    - description -- Comments for reject operation.
    - id -- The ID of the private endpoint connection associated with the private link scope. You can get it using `az monitor private-link-scope show`.
    - name -- The name of the private endpoint connection associated with the private link scope.
    - resource_group -- The resource group name of specified private link scope.
    - scope_name -- Name of the Azure Monitor Private Link Scope.
    '''
    return _call_az("az monitor private-link-scope private-endpoint-connection reject", locals())


def delete(id=None, name=None, resource_group=None, scope_name=None, yes=None):
    '''
    Delete a private endpoint connection of a private link scope resource.

    Optional Parameters:
    - id -- The ID of the private endpoint connection associated with the private link scope. You can get it using `az monitor private-link-scope show`.
    - name -- The name of the private endpoint connection associated with the private link scope.
    - resource_group -- The resource group name of specified private link scope.
    - scope_name -- Name of the Azure Monitor Private Link Scope.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az monitor private-link-scope private-endpoint-connection delete", locals())

