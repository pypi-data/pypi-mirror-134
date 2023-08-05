from ... pyaz_utils import _call_az

def show(scope):
    '''
    Get the details of an extension topic.

    Required Parameters:
    - scope -- The identifier of the resource to which extension topic is queried. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace. For example, use '/subscriptions/{subscriptionId}/' for a subscription, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for a resource group, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}' for Azure resource.
    '''
    return _call_az("az eventgrid extension-topic show", locals())

