from ... pyaz_utils import _call_az

def list(name, resource_group=None):
    '''
    list the private link resources supported for a registry

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr private-link-resource list", locals())

