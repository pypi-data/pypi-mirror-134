from .... pyaz_utils import _call_az

def show(name, resource_group, scope_name):
    '''
    Show a private link resource of a private link scope resource.

    Required Parameters:
    - name -- Name of the private link resource.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scope_name -- Name of the Azure Monitor Private Link Scope.
    '''
    return _call_az("az monitor private-link-scope private-link-resource show", locals())


def list(resource_group, scope_name):
    '''
    List all private link resources of a private link scope resource.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scope_name -- Name of the Azure Monitor Private Link Scope.
    '''
    return _call_az("az monitor private-link-scope private-link-resource list", locals())

