from ... pyaz_utils import _call_az

def create(name, provider, resource_group, vhub, location=None, tags=None):
    '''
    Create a Azure security partner provider.

    Required Parameters:
    - name -- Name of the Security Partner Provider.
    - provider -- The security provider name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vhub -- Name or ID of the virtual hub to which the Security Partner Provider belongs.

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network security-partner-provider create", locals())


def update(name, resource_group, add=None, force_string=None, provider=None, remove=None, set=None, tags=None, vhub=None):
    '''
    Update a Azure security partner provider.

    Required Parameters:
    - name -- Name of the Security Partner Provider.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - provider -- The security provider name
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vhub -- Name or ID of the virtual hub to which the Security Partner Provider belongs.
    '''
    return _call_az("az network security-partner-provider update", locals())


def show(name, resource_group):
    '''
    Show a Azure security partner provider.

    Required Parameters:
    - name -- Name of the Security Partner Provider.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network security-partner-provider show", locals())


def list(resource_group=None):
    '''
    List all Azure security partner provider.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network security-partner-provider list", locals())


def delete(name, resource_group):
    '''
    Delete a Azure security partner provider.

    Required Parameters:
    - name -- Name of the Security Partner Provider.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network security-partner-provider delete", locals())

