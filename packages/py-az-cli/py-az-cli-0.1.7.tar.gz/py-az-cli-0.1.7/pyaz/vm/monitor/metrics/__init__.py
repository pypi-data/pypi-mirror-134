'''
Manage metrics for a vm.
'''
from .... pyaz_utils import _call_az

def tail(name, resource_group, aggregation=None, dimension=None, end_time=None, filter=None, interval=None, metadata=None, metrics=None, namespace=None, offset=None, orderby=None, start_time=None, top=None):
    '''
    List the metric values for a VM.

    Required Parameters:
    - name -- Name or ID of a virtual machine
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

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
    - start_time -- Start time of the query. Format: date (yyyy-mm-dd) time (hh:mm:ss.xxxxx) timezone (+/-hh:mm)
    - top -- Max number of records to retrieve. Valid only if --filter used.
    '''
    return _call_az("az vm monitor metrics tail", locals())


def list_definitions(name, resource_group, namespace=None):
    '''
    List the metric definitions for a VM.

    Required Parameters:
    - name -- Name or ID of a virtual machine
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - namespace -- Namespace to query metric definitions for.
    '''
    return _call_az("az vm monitor metrics list-definitions", locals())

