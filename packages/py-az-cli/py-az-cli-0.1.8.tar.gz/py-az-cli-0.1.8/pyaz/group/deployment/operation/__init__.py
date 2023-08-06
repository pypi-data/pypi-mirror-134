'''
Manage deployment operations.
'''
from .... pyaz_utils import _call_az

def list(name, resource_group, top=None):
    '''
    

    Required Parameters:
    - name -- The deployment name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - top -- The number of results to return.
    '''
    return _call_az("az group deployment operation list", locals())


def show(name, operation_ids, resource_group):
    '''
    

    Required Parameters:
    - name -- The deployment name.
    - operation_ids -- A list of operation ids to show
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az group deployment operation show", locals())

