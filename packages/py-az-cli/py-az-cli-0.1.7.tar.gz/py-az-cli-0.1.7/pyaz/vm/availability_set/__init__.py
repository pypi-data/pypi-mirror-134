from ... pyaz_utils import _call_az

def convert(name, resource_group):
    '''
    Convert an Azure Availability Set to contain VMs with managed disks.

    Required Parameters:
    - name -- Name of the availability set
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm availability-set convert", locals())


def create(name, resource_group, location=None, no_wait=None, platform_fault_domain_count=None, platform_update_domain_count=None, ppg=None, tags=None, unmanaged=None, validate=None):
    '''
    Create an Azure Availability Set.

    Required Parameters:
    - name -- Name of the availability set
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - platform_fault_domain_count -- Fault Domain count.
    - platform_update_domain_count -- Update Domain count. If unspecified, the server will pick the most optimal number like 5.
    - ppg -- The name or ID of the proximity placement group the availability set should be associated with.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - unmanaged -- contained VMs should use unmanaged disks
    - validate -- Generate and validate the ARM template without creating any resources.
    '''
    return _call_az("az vm availability-set create", locals())


def delete(name, resource_group):
    '''
    Delete an availability set.

    Required Parameters:
    - name -- Name of the availability set
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm availability-set delete", locals())


def list(resource_group=None):
    '''
    List availability sets.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm availability-set list", locals())


def list_sizes(name, resource_group):
    '''
    List VM sizes for an availability set.

    Required Parameters:
    - name -- Name of the availability set
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm availability-set list-sizes", locals())


def show(name, resource_group):
    '''
    Get information for an availability set.

    Required Parameters:
    - name -- Name of the availability set
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm availability-set show", locals())


def update(name, resource_group, add=None, force_string=None, ppg=None, remove=None, set=None):
    '''
    Update an Azure Availability Set.

    Required Parameters:
    - name -- Name of the availability set
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - ppg -- The name or ID of the proximity placement group the availability set should be associated with.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az vm availability-set update", locals())

