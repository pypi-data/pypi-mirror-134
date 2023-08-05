from ... pyaz_utils import _call_az
from . import private_endpoint_connection, private_link_resource, scoped_resource


def show(name, resource_group):
    '''
    Show a monitor private link scope resource.

    Required Parameters:
    - name -- Name of the Azure Monitor Private Link Scope.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor private-link-scope show", locals())


def list(resource_group=None):
    '''
    List all monitor private link scope resource.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor private-link-scope list", locals())


def create(name, resource_group, tags=None):
    '''
    Create a private link scope resource.

    Required Parameters:
    - name -- Name of the Azure Monitor Private Link Scope.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az monitor private-link-scope create", locals())


def update(name, resource_group, tags):
    '''
    Update a monitor private link scope resource.

    Required Parameters:
    - name -- Name of the Azure Monitor Private Link Scope.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az monitor private-link-scope update", locals())


def delete(name, resource_group, yes=None):
    '''
    Delete a monitor private link scope resource.

    Required Parameters:
    - name -- Name of the Azure Monitor Private Link Scope.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az monitor private-link-scope delete", locals())

