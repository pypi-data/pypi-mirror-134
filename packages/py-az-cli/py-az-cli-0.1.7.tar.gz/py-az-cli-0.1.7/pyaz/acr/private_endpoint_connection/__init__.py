from ... pyaz_utils import _call_az

def delete(name, registry_name, resource_group=None):
    '''
    Delete a private endpoint connection request for a container registry

    Required Parameters:
    - name -- The name of the private endpoint connection
    - registry_name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr private-endpoint-connection delete", locals())


def show(name, registry_name, resource_group=None):
    '''
    Show details of a container registry's private endpoint connection

    Required Parameters:
    - name -- The name of the private endpoint connection
    - registry_name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr private-endpoint-connection show", locals())


def list(registry_name, resource_group=None):
    '''
    List all private endpoint connections to a container registry

    Required Parameters:
    - registry_name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr private-endpoint-connection list", locals())


def approve(name, registry_name, description=None, resource_group=None):
    '''
    Approve a private endpoint connection request for a container registry

    Required Parameters:
    - name -- The name of the private endpoint connection
    - registry_name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - description -- Approval description. For example, the reason for approval.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr private-endpoint-connection approve", locals())


def reject(name, registry_name, description=None, resource_group=None):
    '''
    Reject a private endpoint connection request for a container registry

    Required Parameters:
    - name -- The name of the private endpoint connection
    - registry_name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - description -- Rejection description. For example, the reason for rejection.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr private-endpoint-connection reject", locals())

