from ... pyaz_utils import _call_az
from . import authorization_rule


def set(alias, namespace_name, partner_namespace, resource_group, alternate_name=None):
    '''
    Sets Service Bus Geo-Disaster Recovery Configuration Alias for the give Namespace

    Required Parameters:
    - alias -- Name of the Geo-Disaster Recovery Configuration Alias
    - namespace_name -- Name of Namespace
    - partner_namespace -- Name (if within the same resource group) or ARM Id of Primary/Secondary Service Bus  namespace name, which is part of GEO DR pairing
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - alternate_name -- Alternate Name (Post failover) for Primary Namespace, when Namespace name and Alias name are same
    '''
    return _call_az("az servicebus georecovery-alias set", locals())


def show(alias, namespace_name, resource_group):
    '''
    shows properties of Service Bus Geo-Disaster Recovery Configuration Alias for Primay/Secondary Namespace

    Required Parameters:
    - alias -- Name of the Geo-Disaster Recovery Configuration Alias
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az servicebus georecovery-alias show", locals())


def list(namespace_name, resource_group):
    '''
    

    Required Parameters:
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az servicebus georecovery-alias list", locals())


def break_pair(alias, namespace_name, resource_group):
    '''
    Disables Service Bus Geo-Disaster Recovery Configuration Alias and stops replicating changes from primary to secondary namespaces

    Required Parameters:
    - alias -- Name of the Geo-Disaster Recovery Configuration Alias
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az servicebus georecovery-alias break-pair", locals())


def fail_over(alias, namespace_name, resource_group, parameters=None):
    '''
    Invokes Service Bus Geo-Disaster Recovery Configuration Alias failover and re-configure the alias to point to the secondary namespace

    Required Parameters:
    - alias -- Name of the Geo-Disaster Recovery Configuration Alias
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - parameters -- Parameters required to create an Alias(Disaster Recovery configuration).
    '''
    return _call_az("az servicebus georecovery-alias fail-over", locals())


def exists(alias, namespace_name, resource_group):
    '''
    Check if Geo Recovery Alias Name is available

    Required Parameters:
    - alias -- Name of Geo-Disaster Recovery Configuration Alias to check availability
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az servicebus georecovery-alias exists", locals())


def delete(alias, namespace_name, resource_group):
    '''
    Deletes Service Bus Geo-Disaster Recovery Configuration Alias request accepted

    Required Parameters:
    - alias -- Name of the Geo-Disaster Recovery Configuration Alias
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az servicebus georecovery-alias delete", locals())

