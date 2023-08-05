from .... pyaz_utils import _call_az

def list(resource_group, server_name):
    '''
    List the private link resources supported for a MySQL server.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the Server.
    '''
    return _call_az("az mysql server private-link-resource list", locals())

