from ... pyaz_utils import _call_az
from . import authorization_rule


def set(alias, namespace_name, partner_namespace, resource_group, alternate_name=None):
    '''
    Sets a Geo-Disaster Recovery Configuration Alias for the give Namespace

    Required Parameters:
    - alias -- Name of Geo-Disaster Recovery Configuration Alias
    - namespace_name -- name of Namespace
    - partner_namespace -- Name (if within the same resource group) or ARM Id of the Primary/Secondary eventhub namespace name, which is part of GEO DR pairing
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - alternate_name -- Alternate Name for the Alias, when the Namespace name and Alias name are same
    '''
    return _call_az("az eventhubs georecovery-alias set", locals())


def show(alias, namespace_name, resource_group):
    '''
    shows properties of Geo-Disaster Recovery Configuration Alias for Primay or Secondary Namespace

    Required Parameters:
    - alias -- Name of Geo-Disaster Recovery Configuration Alias
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs georecovery-alias show", locals())


def list(namespace_name, resource_group):
    '''
    

    Required Parameters:
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs georecovery-alias list", locals())


def break_pair(alias, namespace_name, resource_group):
    '''
    Disables Geo-Disaster Recovery Configuration Alias and stops replicating changes from primary to secondary namespaces

    Required Parameters:
    - alias -- Name of Geo-Disaster Recovery Configuration Alias
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs georecovery-alias break-pair", locals())


def fail_over(alias, namespace_name, resource_group):
    '''
    Invokes Geo-Disaster Recovery Configuration Alias to point to the secondary namespace

    Required Parameters:
    - alias -- Name of Geo-Disaster Recovery Configuration Alias
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs georecovery-alias fail-over", locals())


def exists(alias, namespace_name, resource_group):
    '''
    Check the availability of Geo-Disaster Recovery Configuration Alias Name

    Required Parameters:
    - alias -- Name of Geo Recovery Configs - Alias to check availability
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs georecovery-alias exists", locals())


def delete(alias, namespace_name, resource_group):
    '''
    Delete Geo-Disaster Recovery Configuration Alias

    Required Parameters:
    - alias -- Name of Geo-Disaster Recovery Configuration Alias
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs georecovery-alias delete", locals())

