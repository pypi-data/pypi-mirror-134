from .... pyaz_utils import _call_az
from . import keys


def list(alias, namespace_name, resource_group):
    '''
    List of Authorizationrule by EventHubs Namespace

    Required Parameters:
    - alias -- Name of Geo-Disaster Recovery Configuration Alias
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs georecovery-alias authorization-rule list", locals())


def show(alias, name, namespace_name, resource_group):
    '''
    Show properties of EventHubs Geo-Disaster Recovery Configuration Alias and Namespace Authorizationrule

    Required Parameters:
    - alias -- Name of Geo-Disaster Recovery Configuration Alias
    - name -- Name of Namespace AuthorizationRule
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs georecovery-alias authorization-rule show", locals())

