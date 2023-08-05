from ... pyaz_utils import _call_az

def show(pe_name, workspace_name):
    '''
    Get a synapse managed private endpoints.

    Required Parameters:
    - pe_name -- The managed private endpoint name.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse managed-private-endpoints show", locals())


def create(group_Id, pe_name, resource_id, workspace_name):
    '''
    Create a synapse managed private endpoints.

    Required Parameters:
    - group_Id -- The groupId to which the managed private endpoint is created
    - pe_name -- The managed private endpoint name.
    - resource_id -- The ARM resource ID of the resource to which the managed private endpoint is created. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse managed-private-endpoints create", locals())


def list(workspace_name):
    '''
    List synapse managed private endpoints in a workspace.

    Required Parameters:
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse managed-private-endpoints list", locals())


def delete(pe_name, workspace_name, yes=None):
    '''
    delete synapse managed private endpoints in a workspace.

    Required Parameters:
    - pe_name -- The managed private endpoint name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse managed-private-endpoints delete", locals())

