from ..... pyaz_utils import _call_az

def list(alias, name, namespace_name, resource_group):
    '''
    Shows the keys and connection strings of Authorizationrule for the EventHubs Namespace

    Required Parameters:
    - alias -- Name of Geo-Disaster Recovery Configuration Alias
    - name -- Name of Namespace AuthorizationRule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs georecovery-alias authorization-rule keys list", locals())

