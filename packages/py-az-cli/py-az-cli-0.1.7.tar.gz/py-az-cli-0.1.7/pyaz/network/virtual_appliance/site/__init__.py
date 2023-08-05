from .... pyaz_utils import _call_az

def create(address_prefix, appliance_name, name, resource_group, allow=None, default=None, optimize=None):
    '''
    Create an Azure network virtual appliance site.

    Required Parameters:
    - address_prefix -- Address Prefix of Network Virtual Appliance Site
    - appliance_name -- The name of Network Virtual Appliance
    - name -- The name of Network Virtual Appliance Site
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - allow -- Flag to control breakout of o365 allow category.
    - default -- Flag to control breakout of o365 default category.
    - optimize -- Flag to control breakout of o365 optimize category.
    '''
    return _call_az("az network virtual-appliance site create", locals())


def update(address_prefix, appliance_name, name, resource_group, add=None, allow=None, default=None, force_string=None, optimize=None, remove=None, set=None):
    '''
    Update an Azure network virtual appliance site.

    Required Parameters:
    - address_prefix -- Address Prefix of Network Virtual Appliance Site
    - appliance_name -- The name of Network Virtual Appliance
    - name -- The name of Network Virtual Appliance Site
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - allow -- Flag to control breakout of o365 allow category.
    - default -- Flag to control breakout of o365 default category.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - optimize -- Flag to control breakout of o365 optimize category.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network virtual-appliance site update", locals())


def show(appliance_name, name, resource_group):
    '''
    Show the detail of an Azure network virtual appliance site.

    Required Parameters:
    - appliance_name -- The name of Network Virtual Appliance
    - name -- The name of Network Virtual Appliance Site
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network virtual-appliance site show", locals())


def delete(appliance_name, name, resource_group, yes=None):
    '''
    Delete an Azure network virtual appliance site.

    Required Parameters:
    - appliance_name -- The name of Network Virtual Appliance
    - name -- The name of Network Virtual Appliance Site
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az network virtual-appliance site delete", locals())


def list(appliance_name, resource_group):
    '''
    List all Azure network virtual appliance site.

    Required Parameters:
    - appliance_name -- The name of Network Virtual Appliance
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network virtual-appliance site list", locals())

