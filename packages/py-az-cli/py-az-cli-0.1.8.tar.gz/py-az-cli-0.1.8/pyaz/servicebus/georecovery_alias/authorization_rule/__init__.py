from .... pyaz_utils import _call_az
from . import keys


def list(alias, namespace_name, resource_group):
    '''
    Shows the list of Authorization Rule by Service Bus Namespace

    Required Parameters:
    - alias -- Name of Geo-Disaster Recovery Configuration Alias
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az servicebus georecovery-alias authorization-rule list", locals())


def show(alias, name, namespace_name, resource_group):
    '''
    

    Required Parameters:
    - alias -- Name of the Geo-Disaster Recovery Configuration Alias
    - name -- name of Namespace Authorization Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az servicebus georecovery-alias authorization-rule show", locals())

