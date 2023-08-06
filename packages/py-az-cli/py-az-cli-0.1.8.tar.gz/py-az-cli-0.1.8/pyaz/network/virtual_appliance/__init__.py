from ... pyaz_utils import _call_az
from . import site, sku


def create(name, resource_group, scale_unit, vendor, version, vhub, asn=None, boot_strap_config_blobs=None, cloud_init_config=None, cloud_init_config_blobs=None, location=None, tags=None):
    '''
    Create an Azure network virtual appliance.

    Required Parameters:
    - name -- The name of Network Virtual Appliance
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scale_unit -- Virtual Appliance Scale Unit.
    - vendor -- Virtual Appliance Vendor.
    - version -- Virtual Appliance Version.
    - vhub -- Name or ID of the virtual hub to which the Security Partner Provider belongs.

    Optional Parameters:
    - asn -- VirtualAppliance ASN. The valid value ranges from 1 to 4294967295. 
    - boot_strap_config_blobs -- Space-separated list of BootStrapConfigurationBlobs storage URLs.
    - cloud_init_config -- CloudInitConfiguration scripts that will be run during cloud initialization
    - cloud_init_config_blobs -- Space-separated list of CloudInitConfigurationBlob storage URLs.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network virtual-appliance create", locals())


def update(name, resource_group, add=None, asn=None, cloud_init_config=None, force_string=None, remove=None, set=None):
    '''
    Update an Azure network virtual appliance.

    Required Parameters:
    - name -- The name of Network Virtual Appliance
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - asn -- VirtualAppliance ASN. The valid value ranges from 1 to 4294967295. 
    - cloud_init_config -- CloudInitConfiguration scripts that will be run during cloud initialization
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network virtual-appliance update", locals())


def show(name, resource_group, expand=None):
    '''
    Show the detail of an Azure network virtual appliance.

    Required Parameters:
    - name -- The name of Network Virtual Appliance
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Expands referenced resources.
    '''
    return _call_az("az network virtual-appliance show", locals())


def list(resource_group=None):
    '''
    List all Azure network virtual appliance.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network virtual-appliance list", locals())


def delete(name, resource_group, yes=None):
    '''
    Delete an Azure network virtual appliance.

    Required Parameters:
    - name -- The name of Network Virtual Appliance
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az network virtual-appliance delete", locals())

