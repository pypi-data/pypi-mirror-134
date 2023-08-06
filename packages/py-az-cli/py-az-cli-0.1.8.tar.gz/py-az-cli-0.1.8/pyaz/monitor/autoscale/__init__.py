'''
Manage autoscale settings.
'''
from ... pyaz_utils import _call_az
from . import profile, rule


def create(count, resource, action=None, disabled=None, email_administrator=None, email_coadministrators=None, location=None, max_count=None, min_count=None, name=None, resource_group=None, resource_namespace=None, resource_parent=None, resource_type=None, tags=None):
    '''
    Create new autoscale settings.

    Required Parameters:
    - count -- The numer of instances to use. If used with --min/max-count, the default number of instances to use.
    - resource -- Name or ID of the target resource.

    Optional Parameters:
    - action -- None
    - disabled -- Create the autoscale settings in a disabled state.
    - email_administrator -- Send email to subscription administrator on scaling.
    - email_coadministrators -- Send email to subscription co-administrators on scaling.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - max_count -- The maximum number of instances.
    - min_count -- The minimum number of instances.
    - name -- Name of the autoscale settings.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_namespace -- Target resource provider namespace.
    - resource_parent -- Target resource parent path, if applicable.
    - resource_type -- Target resource type. Can also accept namespace/type format (Ex: 'Microsoft.Compute/virtualMachines')
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az monitor autoscale create", locals())


def update(name, resource_group, add=None, add_action=None, count=None, email_administrator=None, email_coadministrators=None, enabled=None, force_string=None, max_count=None, min_count=None, remove=None, remove_action=None, set=None, tags=None):
    '''
    Update autoscale settings.

    Required Parameters:
    - name -- Name of the autoscale settings.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - add_action -- None
    - count -- The numer of instances to use. If used with --min/max-count, the default number of instances to use.
    - email_administrator -- Send email to subscription administrator on scaling.
    - email_coadministrators -- Send email to subscription co-administrators on scaling.
    - enabled -- Autoscale settings enabled status.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - max_count -- The maximum number of instances.
    - min_count -- The minimum number of instances.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - remove_action -- None
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az monitor autoscale update", locals())


def delete(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Name of the autoscale settings.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor autoscale delete", locals())


def show(name, resource_group):
    '''
    Show autoscale setting details.

    Required Parameters:
    - name -- Name of the autoscale settings.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor autoscale show", locals())


def list(resource_group):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor autoscale list", locals())

