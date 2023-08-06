from ..... pyaz_utils import _call_az

def add(name, resource_group, scope, reset=None):
    '''
    Add scopes to this activity log alert.

    Required Parameters:
    - name -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scope -- None

    Optional Parameters:
    - reset -- None
    '''
    return _call_az("az monitor activity-log alert scope add", locals())


def remove(name, resource_group, scope):
    '''
    Removes scopes from this activity log alert.

    Required Parameters:
    - name -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scope -- None
    '''
    return _call_az("az monitor activity-log alert scope remove", locals())

