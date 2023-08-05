from ... pyaz_utils import _call_az

def show(name, resource_group):
    '''
    Show the details of an action group

    Required Parameters:
    - name -- The name of the action group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor action-group show", locals())


def create(name, resource_group, action=None, short_name=None, tags=None):
    '''
    Create a new action group

    Required Parameters:
    - name -- The name of the action group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - action -- None
    - short_name -- None
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az monitor action-group create", locals())


def delete(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The name of the action group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor action-group delete", locals())


def enable_receiver(action_group, name, resource_group):
    '''
    Enable a receiver in an action group.

    Required Parameters:
    - action_group -- The name of the action group.
    - name -- The name of the receiver to resubscribe.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor action-group enable-receiver", locals())


def list(resource_group=None):
    '''
    List action groups under a resource group or the current subscription

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor action-group list", locals())


def update(name, resource_group, add=None, add_action=None, force_string=None, remove=None, remove_action=None, set=None, short_name=None, tags=None):
    '''
    Update an action group

    Required Parameters:
    - name -- The name of the action group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - add_action -- None
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - remove_action -- None
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - short_name -- None
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az monitor action-group update", locals())

