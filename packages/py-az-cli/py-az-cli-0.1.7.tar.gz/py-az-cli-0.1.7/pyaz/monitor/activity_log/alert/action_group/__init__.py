from ..... pyaz_utils import _call_az

def add(action_group, name, resource_group, reset=None, strict=None, webhook_properties=None):
    '''
    Add action groups to this activity log alert. It can also be used to overwrite existing webhook properties of particular action groups.

    Required Parameters:
    - action_group -- None
    - name -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - reset -- None
    - strict -- None
    - webhook_properties -- None
    '''
    return _call_az("az monitor activity-log alert action-group add", locals())


def remove(action_group, name, resource_group):
    '''
    Remove action groups from this activity log alert

    Required Parameters:
    - action_group -- None
    - name -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor activity-log alert action-group remove", locals())

