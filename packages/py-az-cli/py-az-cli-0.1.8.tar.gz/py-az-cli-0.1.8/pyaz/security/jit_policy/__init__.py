from ... pyaz_utils import _call_az

def list(location=None, resource_group=None):
    '''
    List your Just in Time network access policies.

    Optional Parameters:
    - location -- location of the resource
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az security jit-policy list", locals())


def show(location, name, resource_group):
    '''
    Shows a Just in Time network access policy.

    Required Parameters:
    - location -- location of the resource
    - name -- name of the resource to be fetched
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az security jit-policy show", locals())

