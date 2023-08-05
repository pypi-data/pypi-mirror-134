'''
Manage formulas for an Azure DevTest Lab.
'''
from ... pyaz_utils import _call_az

def show(lab_name, name, resource_group, expand=None):
    '''
    Show formulae from an Azure DevTest Lab.

    Required Parameters:
    - lab_name -- The name of the lab.
    - name -- The name of the formula.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Specify the $expand query. Example: 'properties($select=description)'
    '''
    return _call_az("az lab formula show", locals())


def list(lab_name, resource_group, expand=None, filter=None, orderby=None, top=None):
    '''
    

    Required Parameters:
    - lab_name -- The name of the lab.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Specify the $expand query. Example: 'properties($select=description)'
    - filter -- The filter to apply to the operation. Example: '$filter=contains(name,'myName')
    - orderby -- The ordering expression for the results, using OData notation. Example: '$orderby=name desc'
    - top -- The maximum number of resources to return from the operation. Example: '$top=10'
    '''
    return _call_az("az lab formula list", locals())


def delete(lab_name, name, resource_group):
    '''
    

    Required Parameters:
    - lab_name -- The name of the lab.
    - name -- The name of the formula.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az lab formula delete", locals())


def export_artifacts(lab_name, name, resource_group):
    '''
    Export artifacts from a formula.

    Required Parameters:
    - lab_name -- The name of the lab.
    - name -- The name of the formula.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az lab formula export-artifacts", locals())

