'''
Manage DevTest Labs artifacts.
'''
from ... pyaz_utils import _call_az

def list(artifact_source_name, lab_name, resource_group, expand=None, filter=None, orderby=None, top=None):
    '''
    

    Required Parameters:
    - artifact_source_name -- The name of the artifact source.
    - lab_name -- The name of the lab.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Specify the $expand query. Example: 'properties($select=title)'
    - filter -- The filter to apply to the operation. Example: '$filter=contains(name,'myName')
    - orderby -- The ordering expression for the results, using OData notation. Example: '$orderby=name desc'
    - top -- The maximum number of resources to return from the operation. Example: '$top=10'
    '''
    return _call_az("az lab artifact list", locals())

