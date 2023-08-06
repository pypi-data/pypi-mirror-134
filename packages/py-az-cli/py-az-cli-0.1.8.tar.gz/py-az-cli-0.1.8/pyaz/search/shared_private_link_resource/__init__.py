from ... pyaz_utils import _call_az

def list(resource_group, service_name):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the search service.
    '''
    return _call_az("az search shared-private-link-resource list", locals())


def show(name, resource_group, service_name):
    '''
    

    Required Parameters:
    - name -- The name of the shared private link resource managed by the Azure Cognitive Search service within the specified resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the search service.
    '''
    return _call_az("az search shared-private-link-resource show", locals())


def delete(name, resource_group, service_name, yes=None):
    '''
    

    Required Parameters:
    - name -- The name of the shared private link resource managed by the Azure Cognitive Search service within the specified resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the search service.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az search shared-private-link-resource delete", locals())


def create(group_id, name, resource_group, resource_id, service_name, no_wait=None, request_message=None):
    '''
    

    Required Parameters:
    - group_id -- The group id of the resource; for example: blob, sql or vault.
    - name -- Name of the shared private link resource.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_id -- Fully qualified resource ID for the resource. for example: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/ {resourceProviderNamespace}/{resourceType}/{resourceName}.
    - service_name -- The name of the search service.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - request_message -- Custom request message when creating or updating the shared privatelink resources.
    '''
    return _call_az("az search shared-private-link-resource create", locals())


def update(group_id, name, request_message, resource_group, resource_id, service_name, no_wait=None):
    '''
    

    Required Parameters:
    - group_id -- The group id of the resource; for example: blob, sql or vault.
    - name -- Name of the shared private link resource.
    - request_message -- Custom request message when creating or updating the shared privatelink resources.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_id -- Fully qualified resource ID for the resource; for example: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/ {resourceProviderNamespace}/{resourceType}/{resourceName}.
    - service_name -- The name of the search service.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az search shared-private-link-resource update", locals())


def wait(name, resource_group, service_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Wait for async shared private link resource operations.

    Required Parameters:
    - name -- The name of the shared private link resource managed by the Azure Cognitive Search service within the specified resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the search service.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az search shared-private-link-resource wait", locals())

