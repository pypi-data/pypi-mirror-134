from ... pyaz_utils import _call_az

def list(resource_group, service_name):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the search service.
    '''
    return _call_az("az search query-key list", locals())


def create(name, resource_group, service_name):
    '''
    

    Required Parameters:
    - name -- The name of the query key.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the search service.
    '''
    return _call_az("az search query-key create", locals())


def delete(key_value, resource_group, service_name):
    '''
    

    Required Parameters:
    - key_value -- The value of the query key.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the search service.
    '''
    return _call_az("az search query-key delete", locals())

