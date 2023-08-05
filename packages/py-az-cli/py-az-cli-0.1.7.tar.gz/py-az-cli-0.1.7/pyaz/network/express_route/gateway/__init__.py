from .... pyaz_utils import _call_az
from . import connection


def create(name, resource_group, location=None, max_val=None, min_val=None, tags=None, virtual_hub=None):
    '''
    Create an ExpressRoute gateway.

    Required Parameters:
    - name -- ExpressRoute gateway name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - max_val -- Maximum number of scale units deployed for gateway.
    - min_val -- Minimum number of scale units deployed for gateway.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - virtual_hub -- Name or ID of the virtual hub to associate with the gateway.
    '''
    return _call_az("az network express-route gateway create", locals())


def delete(name, resource_group):
    '''
    Delete an ExpressRoute gateway.

    Required Parameters:
    - name -- ExpressRoute gateway name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route gateway delete", locals())


def list(resource_group=None):
    '''
    List ExpressRoute gateways.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route gateway list", locals())


def show(name, resource_group):
    '''
    Get the details of an ExpressRoute gateway.

    Required Parameters:
    - name -- ExpressRoute gateway name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route gateway show", locals())


def update(name, resource_group, add=None, force_string=None, max_val=None, min_val=None, remove=None, set=None, tags=None):
    '''
    Update settings of an ExpressRoute gateway.

    Required Parameters:
    - name -- ExpressRoute gateway name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - max_val -- Maximum number of scale units deployed for gateway.
    - min_val -- Minimum number of scale units deployed for gateway.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network express-route gateway update", locals())

