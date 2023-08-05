'''
Manage environments for an Azure DevTest Lab.
'''
from ... pyaz_utils import _call_az

def show(lab_name, name, resource_group, expand=None):
    '''
    Get the details for an environment of a lab.

    Required Parameters:
    - lab_name -- The name of the lab.
    - name -- The name of the environment.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Specify the $expand query. Example: 'properties($select=deploymentProperties)'
    '''
    return _call_az("az lab environment show", locals())


def list(lab_name, resource_group, expand=None, filter=None, orderby=None, top=None):
    '''
    List environments in a lab.

    Required Parameters:
    - lab_name -- The name of the lab.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Specify the $expand query. Example: 'properties($select=deploymentProperties)'
    - filter -- The filter to apply to the operation. Example: '$filter=contains(name,'myName')
    - orderby -- The ordering expression for the results, using OData notation. Example: '$orderby=name desc'
    - top -- The maximum number of resources to return from the operation. Example: '$top=10'
    '''
    return _call_az("az lab environment list", locals())


def delete(lab_name, name, resource_group):
    '''
    Delete an environment from a lab.

    Required Parameters:
    - lab_name -- The name of the lab.
    - name -- The name of the environment.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az lab environment delete", locals())


def create(arm_template, lab_name, name, resource_group, artifact_source_name=None, parameters=None, tags=None):
    '''
    Create an environment in a lab.

    Required Parameters:
    - arm_template -- None
    - lab_name -- None
    - name -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - artifact_source_name -- None
    - parameters -- None
    - tags -- None
    '''
    return _call_az("az lab environment create", locals())

