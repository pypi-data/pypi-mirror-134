'''
Manage timer triggers for a task
'''
from .... pyaz_utils import _call_az

def add(name, registry, schedule, timer_name, enabled=None, resource_group=None):
    '''
    Add a timer trigger to a task.

    Required Parameters:
    - name -- The name of the task.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`
    - schedule -- The schedule of the timer trigger represented as a cron expression.
    - timer_name -- The name of the timer trigger.

    Optional Parameters:
    - enabled -- Indicates whether the timer trigger is enabled.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr task timer add", locals())


def update(name, registry, timer_name, enabled=None, resource_group=None, schedule=None):
    '''
    Update the timer trigger for a task.

    Required Parameters:
    - name -- The name of the task.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`
    - timer_name -- The name of the timer trigger.

    Optional Parameters:
    - enabled -- Indicates whether the timer trigger is enabled.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - schedule -- The schedule of the timer trigger represented as a cron expression.
    '''
    return _call_az("az acr task timer update", locals())


def remove(name, registry, timer_name, resource_group=None):
    '''
    Remove a timer trigger from a task.

    Required Parameters:
    - name -- The name of the task.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`
    - timer_name -- The name of the timer trigger.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr task timer remove", locals())


def list(name, registry, resource_group=None):
    '''
    List all timer triggers for a task.

    Required Parameters:
    - name -- The name of the task.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr task timer list", locals())

