from .... pyaz_utils import _call_az

def show(name, resource_group, scope_name):
    '''
    Show a scoped resource of a private link scope resource.

    Required Parameters:
    - name -- Name of the assigned resource.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scope_name -- Name of the Azure Monitor Private Link Scope.
    '''
    return _call_az("az monitor private-link-scope scoped-resource show", locals())


def list(resource_group, scope_name):
    '''
    List all scoped resource of a private link scope resource.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scope_name -- Name of the Azure Monitor Private Link Scope.
    '''
    return _call_az("az monitor private-link-scope scoped-resource list", locals())


def create(linked_resource, name, resource_group, scope_name):
    '''
    Create a scoped resource for a private link scope resource.

    Required Parameters:
    - linked_resource -- ARM resource ID of the linked resource. It should be one of log analytics workspace or application insights component.
    - name -- Name of the assigned resource.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scope_name -- Name of the Azure Monitor Private Link Scope.
    '''
    return _call_az("az monitor private-link-scope scoped-resource create", locals())


def delete(name, resource_group, scope_name, yes=None):
    '''
    Delete a scoped resource of a private link scope resource.

    Required Parameters:
    - name -- Name of the assigned resource.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scope_name -- Name of the Azure Monitor Private Link Scope.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az monitor private-link-scope scoped-resource delete", locals())

