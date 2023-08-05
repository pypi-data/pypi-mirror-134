'''
Manage geo-replicated regions of Azure Container Registries.
'''
from ... pyaz_utils import _call_az

def list(registry, resource_group=None):
    '''
    List all of the regions for a geo-replicated Azure Container Registry.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr replication list", locals())


def create(location, registry, name=None, region_endpoint_enabled=None, resource_group=None, tags=None, zone_redundancy=None):
    '''
    Create a replicated region for an Azure Container Registry.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - name -- The name of the replication. Default to the location name.
    - region_endpoint_enabled -- Allow routing to this replication. Requests will not be routed to a disabled replication. Data syncing will continue regardless of the region endpoint status. Default: true.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - zone_redundancy -- Indicates whether or not zone redundancy should be enabled for this registry or replication. For more information, such as supported locations, please visit https://aka.ms/acr/az. Zone-redundancy cannot be updated. Defaults to 'Disabled'.
    '''
    return _call_az("az acr replication create", locals())


def delete(name, registry, resource_group=None):
    '''
    Delete a replicated region from an Azure Container Registry.

    Required Parameters:
    - name -- The name of the replication.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr replication delete", locals())


def show(name, registry, resource_group=None):
    '''
    Get the details of a replicated region.

    Required Parameters:
    - name -- The name of the replication.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr replication show", locals())


def update(name, registry, add=None, force_string=None, region_endpoint_enabled=None, remove=None, resource_group=None, set=None, tags=None):
    '''
    Updates a replication.

    Required Parameters:
    - name -- The name of the replication.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - region_endpoint_enabled -- Allow routing to this replication. Requests will not be routed to a disabled replication. Data syncing will continue regardless of the region endpoint status.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az acr replication update", locals())

