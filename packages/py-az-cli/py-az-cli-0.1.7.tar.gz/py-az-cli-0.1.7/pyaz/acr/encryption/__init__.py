'''
Manage container registry encryption
'''
from ... pyaz_utils import _call_az

def show(name, resource_group=None):
    '''
    Show the container registry's encryption details

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr encryption show", locals())


def rotate_key(name, identity=None, key_encryption_key=None, resource_group=None):
    '''
    Rotate (update) the container registry's encryption key

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - identity -- client id of managed identity, resource name or id of user assigned identity. Use '[system]' to refer to the system assigned identity
    - key_encryption_key -- Key vault key uri. To enable automated rotation, provide a version-less key uri. For manual rotation, provide a versioned key uri.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr encryption rotate-key", locals())

