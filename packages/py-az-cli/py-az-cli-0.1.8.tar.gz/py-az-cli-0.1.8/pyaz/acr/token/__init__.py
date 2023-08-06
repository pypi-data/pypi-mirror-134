'''
Manage tokens for an Azure Container Registry.
'''
from ... pyaz_utils import _call_az
from . import credential


def create(name, registry, expiration=None, expiration_in_days=None, gateway=None, no_passwords=None, repository=None, resource_group=None, scope_map=None, status=None):
    '''
    Create a token associated with a scope map for an Azure Container Registry.

    Required Parameters:
    - name -- The name of the token.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - expiration -- UTC time for which the credentials will be valid. In the format of %Y-%m-%dT%H:%M:%SZ, e.g. 2025-12-31T12:59:59Z
    - expiration_in_days -- Number of days for which the credentials will be valid. If not specified, the expiration will default to the max value "9999-12-31T23:59:59.999999+00:00"
    - gateway -- gateway permissions. Use the format "--gateway GATEWAY [ACTION1 ACTION2 ...]" per flag. Valid actions are {'message/write', 'config/read', 'message/read', 'config/write'}
    - no_passwords -- Do not generate passwords, instead use "az acr token credential generate"
    - repository -- repository permissions. Use the format "--repository REPO [ACTION1 ACTION2 ...]" per flag. Valid actions are {'metadata/read', 'metadata/write', 'content/write', 'content/delete', 'content/read'}
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scope_map -- The name of the scope map with pre-configured repository permissions. Use "--repository" and/or "--gateway" if you would like CLI to configure one for you
    - status -- The status of the token
    '''
    return _call_az("az acr token create", locals())


def delete(name, registry, resource_group=None, yes=None):
    '''
    Delete a token for an Azure Container Registry.

    Required Parameters:
    - name -- The name of the token.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az acr token delete", locals())


def update(name, registry, resource_group=None, scope_map=None, status=None):
    '''
    Update a token (replace associated scope map) for an Azure Container Registry.

    Required Parameters:
    - name -- The name of the token.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scope_map -- The name of the scope map associated with the token. If not specified, running this command will disassociate the current scope map related to the token.
    - status -- The status of the token
    '''
    return _call_az("az acr token update", locals())


def show(name, registry, resource_group=None):
    '''
    Show details and attributes of a token for an Azure Container Registry.

    Required Parameters:
    - name -- The name of the token.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr token show", locals())


def list(registry, resource_group=None):
    '''
    List all tokens for an Azure Container Registry.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr token list", locals())

