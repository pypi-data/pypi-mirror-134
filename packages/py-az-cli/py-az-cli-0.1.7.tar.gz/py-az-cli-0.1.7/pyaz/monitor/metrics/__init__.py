'''
View Azure resource metrics.
'''
from ... pyaz_utils import _call_az
from . import alert


def list(resource, aggregation=None, dimension=None, end_time=None, filter=None, interval=None, metadata=None, metrics=None, namespace=None, offset=None, orderby=None, resource_group=None, resource_namespace=None, resource_parent=None, resource_type=None, start_time=None, top=None):
    '''
    List the metric values for a resource.

    Required Parameters:
    - resource -- Name or ID of the target resource.

    Optional Parameters:
    - aggregation -- None
    - dimension -- None
    - end_time -- End time of the query. Defaults to the current time. Format: date (yyyy-mm-dd) time (hh:mm:ss.xxxxx) timezone (+/-hh:mm)
    - filter -- None
    - interval -- None
    - metadata -- None
    - metrics -- None
    - namespace -- None
    - offset -- None
    - orderby -- Aggregation to use for sorting results and the direction of the sort. Only one order can be specificed. Examples: sum asc
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_namespace -- Target resource provider namespace.
    - resource_parent -- Target resource parent path, if applicable.
    - resource_type -- Target resource type. Can also accept namespace/type format (Ex: 'Microsoft.Compute/virtualMachines')
    - start_time -- Start time of the query. Format: date (yyyy-mm-dd) time (hh:mm:ss.xxxxx) timezone (+/-hh:mm)
    - top -- Max number of records to retrieve. Valid only if --filter used.
    '''
    return _call_az("az monitor metrics list", locals())


def list_definitions(resource, namespace=None, resource_group=None, resource_namespace=None, resource_parent=None, resource_type=None):
    '''
    List the metric definitions for the resource.

    Required Parameters:
    - resource -- Name or ID of the target resource.

    Optional Parameters:
    - namespace -- Namespace to query metric definitions for.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_namespace -- Target resource provider namespace.
    - resource_parent -- Target resource parent path, if applicable.
    - resource_type -- Target resource type. Can also accept namespace/type format (Ex: 'Microsoft.Compute/virtualMachines')
    '''
    return _call_az("az monitor metrics list-definitions", locals())


def list_namespaces(resource_uri, start_time=None):
    '''
    List the metric namespaces for the resource.

    Required Parameters:
    - resource_uri -- The identifier of the resource.

    Optional Parameters:
    - start_time -- Start time of the query. Format: date (yyyy-mm-dd) time (hh:mm:ss.xxxxx) timezone (+/-hh:mm)
    '''
    return _call_az("az monitor metrics list-namespaces", locals())

