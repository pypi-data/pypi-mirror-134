from .... pyaz_utils import _call_az
from . import action_group, scope


def list(resource_group=None):
    '''
    List activity log alerts under a resource group or the current subscription.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor activity-log alert list", locals())


def create(name, resource_group, action_group=None, condition=None, description=None, disable=None, scope=None, tags=None, webhook_properties=None):
    '''
    Create a default activity log alert

    Required Parameters:
    - name -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - action_group -- None
    - condition -- None
    - description -- None
    - disable -- None
    - scope -- None
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - webhook_properties -- None
    '''
    return _call_az("az monitor activity-log alert create", locals())


def show(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The name of the activity log alert.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor activity-log alert show", locals())


def delete(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The name of the activity log alert.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor activity-log alert delete", locals())


def update(name, resource_group, add=None, condition=None, description=None, enabled=None, force_string=None, remove=None, set=None, tags=None):
    '''
    Update the details of this activity log alert

    Required Parameters:
    - name -- The name of the activity log alert.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - condition -- None
    - description -- None
    - enabled -- None
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az monitor activity-log alert update", locals())

