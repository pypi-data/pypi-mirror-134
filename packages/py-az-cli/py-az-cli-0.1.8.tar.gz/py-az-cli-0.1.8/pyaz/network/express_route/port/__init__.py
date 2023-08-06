from .... pyaz_utils import _call_az
from . import identity, link, location


def create(name, resource_group, bandwidth=None, encapsulation=None, location=None, peering_location=None, tags=None):
    '''
    Create an ExpressRoute port.

    Required Parameters:
    - name -- ExpressRoute port name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - bandwidth -- Bandwidth of the circuit. Usage: INT {Mbps,Gbps}. Defaults to Gbps
    - encapsulation -- Encapsulation method on physical ports.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - peering_location -- The name of the peering location that the port is mapped to physically.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network express-route port create", locals())


def delete(name, resource_group):
    '''
    Delete an ExpressRoute port.

    Required Parameters:
    - name -- ExpressRoute port name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route port delete", locals())


def list(resource_group=None):
    '''
    List ExpressRoute ports.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route port list", locals())


def show(name, resource_group):
    '''
    Get the details of an ExpressRoute port.

    Required Parameters:
    - name -- ExpressRoute port name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route port show", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None, tags=None):
    '''
    Update settings of an ExpressRoute port.

    Required Parameters:
    - name -- ExpressRoute port name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network express-route port update", locals())


def generate_loa(customer_name, name, resource_group, file=None):
    '''
    Generate and download a letter of authorization for the requested ExpressRoutePort

    Required Parameters:
    - customer_name -- The customer name
    - name -- ExpressRoute port name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - file -- Directory or the file path of the letter to be saved to. If the file name extension is not .pdf, Azure CLI will help to append. Be careful, the existing file might get overwritten
    '''
    return _call_az("az network express-route port generate-loa", locals())

