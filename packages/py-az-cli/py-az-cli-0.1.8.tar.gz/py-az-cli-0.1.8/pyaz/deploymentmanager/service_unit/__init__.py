from ... pyaz_utils import _call_az

def create(deployment_mode, parameters_path, resource_group, service_name, service_topology_name, service_unit_name, target_resource_group, template_path, location=None, tags=None):
    '''
    Creates a service unit under the specified service and service topology.

    Required Parameters:
    - deployment_mode -- The type of depoyment mode to be used when deploying the service unit. Possible values: Incremental, Complete
    - parameters_path -- The path to the ARM parameters file. Either the full SAS Uri or the relative path in the artifact source for this topology.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the service
    - service_topology_name -- The name of the service topology
    - service_unit_name -- The name of the service unit
    - target_resource_group -- The resource group where the resources in the service unit should be deployed to
    - template_path -- The path to the ARM template file. Either the full SAS Uri or the relative path in the artifact source for this topology.

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az deploymentmanager service-unit create", locals())


def delete(resource_group, service_name, service_topology_name, service_unit_name):
    '''
    Deletes the service unit.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the service
    - service_topology_name -- The name of the service topology
    - service_unit_name -- The name of the service unit
    '''
    return _call_az("az deploymentmanager service-unit delete", locals())


def show(resource_group, service_name, service_topology_name, service_unit_name):
    '''
    Get the details of a service unit.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the service
    - service_topology_name -- The name of the service topology
    - service_unit_name -- The name of the service unit
    '''
    return _call_az("az deploymentmanager service-unit show", locals())


def list(resource_group, service_name, service_topology_name):
    '''
    List all service units in a service.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the service
    - service_topology_name -- The name of the service topology
    '''
    return _call_az("az deploymentmanager service-unit list", locals())


def update(resource_group, service_name, service_topology_name, service_unit_name, add=None, deployment_mode=None, force_string=None, parameters_path=None, remove=None, set=None, tags=None, target_resource_group=None, template_path=None):
    '''
    Updates the service unit.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the service
    - service_topology_name -- The name of the service topology
    - service_unit_name -- The name of the service unit

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - deployment_mode -- The type of depoyment mode to be used when deploying the service unit. Possible values: Incremental, Complete
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - parameters_path -- The path to the ARM parameters file. Either the full SAS Uri or the relative path in the artifact source for this topology.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - target_resource_group -- The resource group where the resources in the service unit should be deployed to
    - template_path -- The path to the ARM template file. Either the full SAS Uri or the relative path in the artifact source for this topology.
    '''
    return _call_az("az deploymentmanager service-unit update", locals())

