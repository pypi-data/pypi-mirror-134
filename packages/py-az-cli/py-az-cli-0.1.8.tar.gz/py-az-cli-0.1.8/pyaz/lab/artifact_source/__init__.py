from ... pyaz_utils import _call_az

def list(lab_name, resource_group, expand=None, filter=None, orderby=None, top=None):
    '''
    

    Required Parameters:
    - lab_name -- The name of the lab.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Specify the $expand query. Example: 'properties($select=displayName)'
    - filter -- The filter to apply to the operation. Example: '$filter=contains(name,'myName')
    - orderby -- The ordering expression for the results, using OData notation. Example: '$orderby=name desc'
    - top -- The maximum number of resources to return from the operation. Example: '$top=10'
    '''
    return _call_az("az lab artifact-source list", locals())


def show(lab_name, name, resource_group, expand=None):
    '''
    

    Required Parameters:
    - lab_name -- The name of the lab.
    - name -- The name of the artifact source.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Specify the $expand query. Example: 'properties($select=displayName)'
    '''
    return _call_az("az lab artifact-source show", locals())

