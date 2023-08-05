from .... pyaz_utils import _call_az

def delete(name, resource_group, service_name):
    '''
    Delete a private link service endpoint connection.

    Required Parameters:
    - name -- Name of the private endpoint connection. List them by using "az network private-link-service show".
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- Name of the private link service.
    '''
    return _call_az("az network private-link-service connection delete", locals())


def update(connection_status, name, resource_group, service_name, action_required=None, description=None):
    '''
    Update a private link service endpoint connection.

    Required Parameters:
    - connection_status -- Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    - name -- Name of the private endpoint connection. List them by using "az network private-link-service show".
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- Name of the private link service.

    Optional Parameters:
    - action_required -- A message indicating if changes on the service provider require any updates on the consumer.
    - description -- The reason for approval/rejection of the connection.
    '''
    return _call_az("az network private-link-service connection update", locals())

