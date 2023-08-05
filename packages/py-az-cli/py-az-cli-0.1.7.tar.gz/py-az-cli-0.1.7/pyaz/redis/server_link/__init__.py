from ... pyaz_utils import _call_az

def create(name, replication_role, resource_group, server_to_link):
    '''
    Adds a server link to the Redis cache (requires Premium SKU).

    Required Parameters:
    - name -- Name of the Redis cache.
    - replication_role -- Role of the redis cache to be linked
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_to_link -- Resource ID or name of the redis cache to be linked
    '''
    return _call_az("az redis server-link create", locals())


def delete(linked_server_name, name, resource_group):
    '''
    

    Required Parameters:
    - linked_server_name -- Name of the linked redis cache
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az redis server-link delete", locals())


def show(linked_server_name, name, resource_group):
    '''
    

    Required Parameters:
    - linked_server_name -- Name of the linked redis cache
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az redis server-link show", locals())


def list(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az redis server-link list", locals())

