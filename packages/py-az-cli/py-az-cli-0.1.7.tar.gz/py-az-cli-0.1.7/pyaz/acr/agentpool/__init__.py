'''
Manage private Tasks agent pools with Azure Container Registries.
'''
from ... pyaz_utils import _call_az

def create(name, registry, count=None, no_wait=None, os=None, resource_group=None, subnet_id=None, tier=None):
    '''
    Create an agent pool for an Azure Container Registry.

    Required Parameters:
    - name -- The name of the agent pool.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - count -- The count of the agent pool.
    - no_wait -- Do not wait for the Agent Pool to complete action and return immediately after queuing the request.
    - os -- The os of the agent pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subnet_id -- The Virtual Network Subnet Resource Id of the agent machine.
    - tier -- Sets the VM your agent pool will run on. Valid values are: S1(2 vCPUs, 3 GiB RAM), S2(4 vCPUs, 8 GiB RAM), S3(8 vCPUs, 16 GiB RAM) or I6(64 vCPUs, 216 GiB RAM, Isolated)
    '''
    return _call_az("az acr agentpool create", locals())


def update(name, registry, count=None, no_wait=None, resource_group=None):
    '''
    Update an agent pool for an Azure Container Registry.

    Required Parameters:
    - name -- The name of the agent pool.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - count -- The count of the agent pool.
    - no_wait -- Do not wait for the Agent Pool to complete action and return immediately after queuing the request.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr agentpool update", locals())


def delete(name, registry, no_wait=None, resource_group=None, yes=None):
    '''
    Delete an agent pool.

    Required Parameters:
    - name -- The name of the agent pool.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - no_wait -- Do not wait for the Agent Pool to complete action and return immediately after queuing the request.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az acr agentpool delete", locals())


def list(registry, resource_group=None):
    '''
    List the agent pools for an Azure Container Registry.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr agentpool list", locals())


def show(name, registry, queue_count=None, resource_group=None):
    '''
    Get the properties of a specified agent pool for an Azure Container Registry.

    Required Parameters:
    - name -- The name of the agent pool.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - queue_count -- Get only the queue count
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr agentpool show", locals())

