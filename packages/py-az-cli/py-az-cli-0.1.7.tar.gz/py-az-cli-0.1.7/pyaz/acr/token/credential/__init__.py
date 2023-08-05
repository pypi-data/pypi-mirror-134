'''
Manage credentials of a token for an Azure Container Registry.
'''
from .... pyaz_utils import _call_az

def delete(name, registry, password1=None, password2=None, resource_group=None):
    '''
    Delete a token credential.

    Required Parameters:
    - name -- The name of the token.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - password1 -- Flag indicating if first password should be deleted
    - password2 -- Flag indicating if second password should be deleted.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr token credential delete", locals())


def generate(name, registry, expiration=None, expiration_in_days=None, password1=None, password2=None, resource_group=None):
    '''
    Generate or replace one or both passwords of a token for an Azure Container Registry. For using token and password to access a container registry, see https://aka.ms/acr/repo-permissions.

    Required Parameters:
    - name -- The name of the token.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - expiration -- UTC time for which the credentials will be valid. In the format of %Y-%m-%dT%H:%M:%SZ, e.g. 2025-12-31T12:59:59Z
    - expiration_in_days -- Number of days for which the credentials will be valid. If not specified, the expiration will default to the max value "9999-12-31T23:59:59.999999+00:00"
    - password1 -- Flag indicating if password1 should be generated.
    - password2 -- Flag indicating if password2 should be generated.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr token credential generate", locals())

