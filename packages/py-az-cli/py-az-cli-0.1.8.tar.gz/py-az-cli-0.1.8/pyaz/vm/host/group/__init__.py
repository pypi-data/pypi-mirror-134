'''
Manage Dedicated Host Groups
'''
from .... pyaz_utils import _call_az

def show(name, resource_group):
    '''
    Get the details of a dedicated host group.

    Required Parameters:
    - name -- Name of the Dedicated Host Group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm host group show", locals())


def get_instance_view(name, resource_group):
    '''
    Get instance view of a dedicated host group.

    Required Parameters:
    - name -- Name of the Dedicated Host Group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm host group get-instance-view", locals())


def create(name, platform_fault_domain_count, resource_group, automatic_placement=None, location=None, tags=None, zone=None):
    '''
    Create a dedicated host group.

    Required Parameters:
    - name -- Name of the Dedicated Host Group
    - platform_fault_domain_count -- Number of fault domains that the host group can span.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - automatic_placement -- Specify whether virtual machines or virtual machine scale sets can be placed automatically on the dedicated host group. Automatic placement means resources are allocated on dedicated hosts, that are chosen by Azure, under the dedicated host group. The value is defaulted to false when not provided.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`. Otherwise, location will default to the resource group's location
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - zone -- Availability zone into which to provision the resource.
    '''
    return _call_az("az vm host group create", locals())


def list(resource_group=None):
    '''
    List dedicated host groups.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm host group list", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None):
    '''
    Update a dedicated host group.

    Required Parameters:
    - name -- Name of the Dedicated Host Group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az vm host group update", locals())


def delete(name, resource_group, yes=None):
    '''
    

    Required Parameters:
    - name -- Name of the Dedicated Host Group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az vm host group delete", locals())

