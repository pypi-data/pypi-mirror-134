from .... pyaz_utils import _call_az

def delete(id=None, name=None, namespace_name=None, resource_group=None, yes=None):
    '''
    Delete a private endpoint connection request for eventhubs namespace.

    Optional Parameters:
    - id -- The ID of the private endpoint connection associated with the EventHubs Namespace. You can get it using `az eventhubs namespace show`.
    - name -- The name of the private endpoint connection associated with the EventHubs Namespace.
    - namespace_name -- The eventhubs namesapce name.
    - resource_group -- The resource group name of specified eventhubs namespace.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az eventhubs namespace private-endpoint-connection delete", locals())


def show(id=None, name=None, namespace_name=None, resource_group=None):
    '''
    Show details of a private endpoint connection request for eventhubs namespace.

    Optional Parameters:
    - id -- The ID of the private endpoint connection associated with the EventHubs Namespace. You can get it using `az eventhubs namespace show`.
    - name -- The name of the private endpoint connection associated with the EventHubs Namespace.
    - namespace_name -- The eventhubs namesapce name.
    - resource_group -- The resource group name of specified eventhubs namespace.
    '''
    return _call_az("az eventhubs namespace private-endpoint-connection show", locals())


def list(namespace_name, resource_group):
    '''
    

    Required Parameters:
    - namespace_name -- Name of the Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs namespace private-endpoint-connection list", locals())


def approve(description=None, id=None, name=None, namespace_name=None, resource_group=None):
    '''
    Approve a private endpoint connection request for eventhubs namesapce.

    Optional Parameters:
    - description -- Comments for approve operation.
    - id -- The ID of the private endpoint connection associated with the EventHubs Namespace. You can get it using `az eventhubs namespace show`.
    - name -- The name of the private endpoint connection associated with the EventHubs Namespace.
    - namespace_name -- The eventhubs namesapce name.
    - resource_group -- The resource group name of specified eventhubs namespace.
    '''
    return _call_az("az eventhubs namespace private-endpoint-connection approve", locals())


def reject(description=None, id=None, name=None, namespace_name=None, resource_group=None):
    '''
    Reject a private endpoint connection request for eventhubs namespace.

    Optional Parameters:
    - description -- Comments for reject operation.
    - id -- The ID of the private endpoint connection associated with the EventHubs Namespace. You can get it using `az eventhubs namespace show`.
    - name -- The name of the private endpoint connection associated with the EventHubs Namespace.
    - namespace_name -- The eventhubs namesapce name.
    - resource_group -- The resource group name of specified eventhubs namespace.
    '''
    return _call_az("az eventhubs namespace private-endpoint-connection reject", locals())

