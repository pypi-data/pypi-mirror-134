'''
Manage Dedicated Hosts for Virtual Machines
'''
from ... pyaz_utils import _call_az
from . import group


def show(host_group, name, resource_group):
    '''
    Get the details of a dedicated host.

    Required Parameters:
    - host_group -- Name of the Dedicated Host Group
    - name -- Name of the Dedicated Host
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm host show", locals())


def get_instance_view(host_group, name, resource_group):
    '''
    Get instance information about a dedicated host.

    Required Parameters:
    - host_group -- Name of the Dedicated Host Group
    - name -- Name of the Dedicated Host
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm host get-instance-view", locals())


def create(host_group, name, resource_group, sku, auto_replace=None, license_type=None, location=None, platform_fault_domain=None, tags=None):
    '''
    Create a dedicated host.

    Required Parameters:
    - host_group -- Name of the Dedicated Host Group
    - name -- Name of the Dedicated Host
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku -- SKU of the dedicated host. Available SKUs: https://azure.microsoft.com/pricing/details/virtual-machines/dedicated-host/

    Optional Parameters:
    - auto_replace -- Replace the host automatically if a failure occurs
    - license_type -- The software license type that will be applied to the VMs deployed on the dedicated host.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`. Otherwise, location will default to the resource group's location
    - platform_fault_domain -- Fault domain of the host within a group. Allowed values: 0, 1, 2
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az vm host create", locals())


def list(host_group, resource_group):
    '''
    List dedicated hosts.

    Required Parameters:
    - host_group -- Name of the Dedicated Host Group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm host list", locals())


def update(host_group, name, resource_group, add=None, force_string=None, remove=None, set=None):
    '''
    Update a dedicated host.

    Required Parameters:
    - host_group -- Name of the Dedicated Host Group
    - name -- Name of the Dedicated Host
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az vm host update", locals())


def delete(host_group, name, resource_group, yes=None):
    '''
    

    Required Parameters:
    - host_group -- Name of the Dedicated Host Group
    - name -- Name of the Dedicated Host
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az vm host delete", locals())

