'''
Manage Azure DevTest Labs.
'''
from .. pyaz_utils import _call_az
from . import arm_template, artifact, artifact_source, custom_image, environment, formula, gallery_image, secret, vm, vnet


def get(name, resource_group, expand=None):
    '''
    

    Required Parameters:
    - name -- The name of the lab.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Specify the $expand query. Example: 'properties($select=defaultStorageAccount)'
    '''
    return _call_az("az lab get", locals())


def delete(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The name of the lab.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az lab delete", locals())

