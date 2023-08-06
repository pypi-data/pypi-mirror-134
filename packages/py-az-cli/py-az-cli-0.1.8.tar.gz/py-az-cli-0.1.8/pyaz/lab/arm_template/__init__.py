from ... pyaz_utils import _call_az

def list(artifact_source_name, lab_name, resource_group, expand=None, filter=None, orderby=None, top=None):
    '''
    

    Required Parameters:
    - artifact_source_name -- The name of the artifact source.
    - lab_name -- The name of the lab.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Specify the $expand query. Example: 'properties($select=displayName)'
    - filter -- The filter to apply to the operation. Example: '$filter=contains(name,'myName')
    - orderby -- The ordering expression for the results, using OData notation. Example: '$orderby=name desc'
    - top -- The maximum number of resources to return from the operation. Example: '$top=10'
    '''
    return _call_az("az lab arm-template list", locals())


def show(artifact_source_name, lab_name, name, resource_group, export_parameters=None):
    '''
    Get the details of an ARM template in a lab.

    Required Parameters:
    - artifact_source_name -- None
    - lab_name -- None
    - name -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - export_parameters -- None
    '''
    return _call_az("az lab arm-template show", locals())

