from .... pyaz_utils import _call_az

def approve(description=None, id=None, name=None, resource_group=None, server_name=None):
    '''
    Approve the specified private endpoint connection associated with a MySQL server.

    Optional Parameters:
    - description -- Comments for approve operation.
    - id -- The ID of the private endpoint connection associated with the Server. If specified --server-name/-s and --name/-n, this should be omitted.
    - name -- The name of the private endpoint connection associated with the Server. Required if --id is not specified
    - resource_group -- The resource group name of specified server.
    - server_name -- Name of the Server. Required if --id is not specified
    '''
    return _call_az("az mysql server private-endpoint-connection approve", locals())


def reject(description=None, id=None, name=None, resource_group=None, server_name=None):
    '''
    Reject the specified private endpoint connection associated with a MySQL server.

    Optional Parameters:
    - description -- Comments for reject operation.
    - id -- The ID of the private endpoint connection associated with the Server. If specified --server-name/-s and --name/-n, this should be omitted.
    - name -- The name of the private endpoint connection associated with the Server. Required if --id is not specified
    - resource_group -- The resource group name of specified server.
    - server_name -- Name of the Server. Required if --id is not specified
    '''
    return _call_az("az mysql server private-endpoint-connection reject", locals())


def delete(id=None, name=None, resource_group=None, server_name=None):
    '''
    Delete the specified private endpoint connection associated with a MySQL server.

    Optional Parameters:
    - id -- The ID of the private endpoint connection associated with the Server. If specified --server-name/-s and --name/-n, this should be omitted.
    - name -- The name of the private endpoint connection associated with the Server. Required if --id is not specified
    - resource_group -- The resource group name of specified server.
    - server_name -- Name of the Server. Required if --id is not specified
    '''
    return _call_az("az mysql server private-endpoint-connection delete", locals())


def show(id=None, name=None, resource_group=None, server_name=None):
    '''
    Show details of a private endpoint connection associated with a MySQL server.

    Optional Parameters:
    - id -- The ID of the private endpoint connection associated with the Server. If specified --server-name/-s and --name/-n, this should be omitted.
    - name -- The name of the private endpoint connection associated with the Server. Required if --id is not specified
    - resource_group -- The resource group name of specified server.
    - server_name -- Name of the Server. Required if --id is not specified
    '''
    return _call_az("az mysql server private-endpoint-connection show", locals())

