'''
Manage log analytics workspace for a vm.
'''
from .... pyaz_utils import _call_az

def show(analytics_query, name, resource_group, timespan=None):
    '''
    Execute a query against the Log Analytics workspace linked with a VM.

    Required Parameters:
    - analytics_query -- Query to execute over Log Analytics data.
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - timespan -- Timespan over which to query. Defaults to querying all available data.
    '''
    return _call_az("az vm monitor log show", locals())

