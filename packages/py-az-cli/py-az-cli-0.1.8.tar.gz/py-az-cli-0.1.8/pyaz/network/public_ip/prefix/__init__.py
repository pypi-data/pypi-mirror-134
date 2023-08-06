from .... pyaz_utils import _call_az

def create(length, name, resource_group, custom_ip_prefix_name=None, edge_zone=None, location=None, tags=None, version=None, zone=None):
    '''
    Create a public IP prefix resource.

    Required Parameters:
    - length -- Length of the prefix (i.e. `XX.XX.XX.XX/<Length>`)
    - name -- The name of the public IP prefix.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - custom_ip_prefix_name -- The customIpPrefix that this prefix is associated with.
    - edge_zone -- The name of edge zone.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - version -- IP address type.
    - zone -- Space-separated list of availability zones into which to provision the resource.
    '''
    return _call_az("az network public-ip prefix create", locals())


def delete(name, resource_group):
    '''
    Delete a public IP prefix resource.

    Required Parameters:
    - name -- The name of the public IP prefix.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network public-ip prefix delete", locals())


def list(resource_group=None):
    '''
    List public IP prefix resources.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network public-ip prefix list", locals())


def show(name, resource_group, expand=None):
    '''
    Get the details of a public IP prefix resource.

    Required Parameters:
    - name -- The name of the public IP prefix.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Expands referenced resources.
    '''
    return _call_az("az network public-ip prefix show", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None, tags=None):
    '''
    Update a public IP prefix resource.

    Required Parameters:
    - name -- The name of the public IP prefix.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network public-ip prefix update", locals())

