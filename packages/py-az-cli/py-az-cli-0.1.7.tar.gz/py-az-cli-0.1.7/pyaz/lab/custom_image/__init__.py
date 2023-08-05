from ... pyaz_utils import _call_az

def show(lab_name, name, resource_group, expand=None):
    '''
    

    Required Parameters:
    - lab_name -- The name of the lab.
    - name -- The name of the custom image.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Specify the $expand query. Example: 'properties($select=vm)'
    '''
    return _call_az("az lab custom-image show", locals())


def list(lab_name, resource_group, expand=None, filter=None, orderby=None, top=None):
    '''
    

    Required Parameters:
    - lab_name -- The name of the lab.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Specify the $expand query. Example: 'properties($select=vm)'
    - filter -- The filter to apply to the operation. Example: '$filter=contains(name,'myName')
    - orderby -- The ordering expression for the results, using OData notation. Example: '$orderby=name desc'
    - top -- The maximum number of resources to return from the operation. Example: '$top=10'
    '''
    return _call_az("az lab custom-image list", locals())


def delete(lab_name, name, resource_group):
    '''
    

    Required Parameters:
    - lab_name -- The name of the lab.
    - name -- The name of the custom image.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az lab custom-image delete", locals())


def create(lab_name, name, os_state, os_type, resource_group, source_vm_id, author=None, description=None):
    '''
    Create a custom image in a DevTest Lab.

    Required Parameters:
    - lab_name -- None
    - name -- None
    - os_state -- None
    - os_type -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source_vm_id -- None

    Optional Parameters:
    - author -- None
    - description -- None
    '''
    return _call_az("az lab custom-image create", locals())

