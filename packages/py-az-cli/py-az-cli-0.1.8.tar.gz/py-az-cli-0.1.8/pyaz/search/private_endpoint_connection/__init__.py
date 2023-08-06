from ... pyaz_utils import _call_az

def list(resource_group, service_name):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the search service.
    '''
    return _call_az("az search private-endpoint-connection list", locals())


def show(private_endpoint_connection_name, resource_group, service_name):
    '''
    

    Required Parameters:
    - private_endpoint_connection_name -- The name of the private endpoint connection to the Azure Cognitive Search service with the specified resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the search service.
    '''
    return _call_az("az search private-endpoint-connection show", locals())


def delete(private_endpoint_connection_name, resource_group, service_name, yes=None):
    '''
    

    Required Parameters:
    - private_endpoint_connection_name -- The name of the private endpoint connection to the Azure Cognitive Search service with the specified resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the search service.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az search private-endpoint-connection delete", locals())


def update(actions_required, description, name, resource_group, service_name, status):
    '''
    

    Required Parameters:
    - actions_required -- Custom 'actions required' message when updating the private endpoint connection resource.
    - description -- Custom description when updating the private endpoint connection resource.
    - name -- Name of the private endpoint connection resource; for example: {the name of the private endpoint resource}.{guid}.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the search service.
    - status -- The updated status of the private endpoint connection resource. Possible values include: "Pending", "Approved", "Rejected", "Disconnected".
    '''
    return _call_az("az search private-endpoint-connection update", locals())

