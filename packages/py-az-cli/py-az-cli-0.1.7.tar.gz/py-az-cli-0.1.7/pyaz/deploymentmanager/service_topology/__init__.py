from ... pyaz_utils import _call_az

def create(location, resource_group, service_topology_name, artifact_source=None, tags=None):
    '''
    Creates a service topology.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_topology_name -- The name of the service topology

    Optional Parameters:
    - artifact_source -- The name or resource identifier of the artifact source.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az deploymentmanager service-topology create", locals())


def delete(resource_group, service_topology_name):
    '''
    Deletes the service topology.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_topology_name -- The name of the service topology
    '''
    return _call_az("az deploymentmanager service-topology delete", locals())


def show(resource_group, service_topology_name):
    '''
    Get the details of a service topology.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_topology_name -- The name of the service topology
    '''
    return _call_az("az deploymentmanager service-topology show", locals())


def list(resource_group):
    '''
    List all service topologies in a resource group.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az deploymentmanager service-topology list", locals())


def update(resource_group, service_topology_name, add=None, artifact_source=None, force_string=None, remove=None, set=None, tags=None):
    '''
    Updates the service topology.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_topology_name -- The name of the service topology

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - artifact_source -- The name or resource identifier of the artifact source.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az deploymentmanager service-topology update", locals())

