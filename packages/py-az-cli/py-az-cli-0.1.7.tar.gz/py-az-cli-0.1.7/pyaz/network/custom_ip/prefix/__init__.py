from .... pyaz_utils import _call_az

def create(name, resource_group, authorization_message=None, cidr=None, cip_prefix_parent=None, location=None, no_wait=None, signed_message=None, tags=None, zone=None):
    '''
    Create a custom IP prefix resource.

    Required Parameters:
    - name -- The name of the custom IP prefix.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - authorization_message -- Authorization message for WAN validation.
    - cidr -- The prefix range in CIDR notation. Should include the start address and the prefix length.
    - cip_prefix_parent -- The Parent CustomIpPrefix for IPv6 /64 CustomIpPrefix.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - signed_message -- Signed message for WAN validation.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - zone -- Space-separated list of availability zones into which to provision the resource.
    '''
    return _call_az("az network custom-ip prefix create", locals())


def delete(name, resource_group):
    '''
    Delete a custom IP prefix resource.

    Required Parameters:
    - name -- The name of the custom IP prefix.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network custom-ip prefix delete", locals())


def list(resource_group=None):
    '''
    List custom IP prefix resources.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network custom-ip prefix list", locals())


def show(name, resource_group, expand=None):
    '''
    Get the details of a custom IP prefix resource.

    Required Parameters:
    - name -- The name of the custom IP prefix.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Expands referenced resources.
    '''
    return _call_az("az network custom-ip prefix show", locals())


def update(name, resource_group, add=None, authorization_message=None, force_string=None, no_wait=None, remove=None, set=None, signed_message=None, state=None, tags=None):
    '''
    Update a custom IP prefix resource.

    Required Parameters:
    - name -- The name of the custom IP prefix.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - authorization_message -- Authorization message for WAN validation.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - signed_message -- Signed message for WAN validation.
    - state -- Commissioned State of the custom ip prefix.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network custom-ip prefix update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, expand=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the custom ip prefix is met.

    Required Parameters:
    - name -- The name of the custom IP prefix.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - expand -- Expands referenced resources.
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az network custom-ip prefix wait", locals())

