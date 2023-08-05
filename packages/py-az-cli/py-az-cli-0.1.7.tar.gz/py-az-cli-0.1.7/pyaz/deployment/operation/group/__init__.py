'''
Manage deployment operations at resource group.
'''
from .... pyaz_utils import _call_az

def list(name, resource_group):
    '''
    List deployment operations at resource group.

    Required Parameters:
    - name -- The deployment name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az deployment operation group list", locals())


def show(name, operation_ids, resource_group):
    '''
    Show a deployment operation at resource group.

    Required Parameters:
    - name -- The deployment name.
    - operation_ids -- A list of operation ids to show
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az deployment operation group show", locals())

