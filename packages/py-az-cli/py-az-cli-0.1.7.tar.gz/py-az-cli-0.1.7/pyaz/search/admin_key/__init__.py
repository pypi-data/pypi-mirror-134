from ... pyaz_utils import _call_az

def show(resource_group, service_name):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the search service.
    '''
    return _call_az("az search admin-key show", locals())


def renew(key_kind, resource_group, service_name):
    '''
    

    Required Parameters:
    - key_kind -- The type (primary or secondary) of the admin key.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the search service.
    '''
    return _call_az("az search admin-key renew", locals())

