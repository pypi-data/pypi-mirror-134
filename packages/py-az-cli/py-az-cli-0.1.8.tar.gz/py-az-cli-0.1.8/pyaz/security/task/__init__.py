'''
View security tasks (recommendations).
'''
from ... pyaz_utils import _call_az

def list(resource_group=None):
    '''
    List security tasks (recommendations).

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az security task list", locals())


def show(name, resource_group=None):
    '''
    shows a security task (recommendation).

    Required Parameters:
    - name -- name of the resource to be fetched

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az security task show", locals())

