'''
Manage Azure Service Bus Migration of Standard to Premium
'''
from ... pyaz_utils import _call_az

def start(name, post_migration_name, resource_group, target_namespace):
    '''
    Create and Start Service Bus Migration of Standard to Premium namespace.

    Required Parameters:
    - name -- Name of Standard Namespace used as source of the migration
    - post_migration_name -- Post migration name is the name that can be used to connect to standard namespace after migration is complete.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - target_namespace -- Name (if within the same resource group) or ARM Id of empty Premium Service Bus namespace name that will be target of the migration
    '''
    return _call_az("az servicebus migration start", locals())


def show(name, resource_group):
    '''
    shows properties of properties of Service Bus Migration

    Required Parameters:
    - name -- Name of Standard Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az servicebus migration show", locals())


def complete(name, resource_group):
    '''
    Completes the Service Bus Migration of Standard to Premium namespace

    Required Parameters:
    - name -- Name of Standard Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az servicebus migration complete", locals())


def abort(name, resource_group):
    '''
    Disable the Service Bus Migration of Standard to Premium namespace

    Required Parameters:
    - name -- Name of Standard Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az servicebus migration abort", locals())

