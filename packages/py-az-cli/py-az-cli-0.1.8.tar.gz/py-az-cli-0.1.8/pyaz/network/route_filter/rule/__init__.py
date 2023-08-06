from .... pyaz_utils import _call_az

def create(access, communities, filter_name, name, resource_group, location=None):
    '''
    Create a rule in a route filter.

    Required Parameters:
    - access -- The access type of the rule.
    - communities -- None
    - filter_name -- Name of the route filter.
    - name -- Name of the route filter rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az network route-filter rule create", locals())


def list(filter_name, resource_group):
    '''
    List rules in a route filter.

    Required Parameters:
    - filter_name -- Name of the route filter.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network route-filter rule list", locals())


def show(filter_name, name, resource_group):
    '''
    Get the details of a rule in a route filter.

    Required Parameters:
    - filter_name -- Name of the route filter.
    - name -- Name of the route filter rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network route-filter rule show", locals())


def delete(filter_name, name, resource_group):
    '''
    Delete a rule from a route filter.

    Required Parameters:
    - filter_name -- Name of the route filter.
    - name -- Name of the route filter rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network route-filter rule delete", locals())


def update(filter_name, name, resource_group, add=None, force_string=None, remove=None, set=None):
    '''
    Update a rule in a route filter.

    Required Parameters:
    - filter_name -- Name of the route filter.
    - name -- Name of the route filter rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network route-filter rule update", locals())


def list_service_communities():
    '''
    Gets all the available BGP service communities.
    '''
    return _call_az("az network route-filter rule list-service-communities", locals())

