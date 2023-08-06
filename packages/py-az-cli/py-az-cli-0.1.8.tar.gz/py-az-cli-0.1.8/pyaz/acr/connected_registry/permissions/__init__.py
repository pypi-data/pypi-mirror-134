from .... pyaz_utils import _call_az

def update(name, registry, add=None, remove=None, resource_group=None):
    '''
    Add and remove repository permissions accross all the necessary connected registry sync scope maps.

    Required Parameters:
    - name -- Name for the connected registry. Name must be between 5 to 40 character long, start with a letter and contain only alphanumeric characters (including ‘_’ or ‘-’). Name must be unique under the Cloud ACR hierarchy.
    - registry -- The login server of the Cloud ACR registry. Must be the FQDN to support also Azure Stack.

    Optional Parameters:
    - add -- repository permissions to be added to the targeted connected registry and it's ancestors sync scope maps. Use the format "--add [REPO1 REPO2 ...]" per flag. Valid actions are {'metadata/read', 'metadata/write', 'content/write', 'content/delete', 'content/read'}
    - remove -- respsitory permissions to be removed from the targeted connected registry and it's succesors sync scope maps. Use the format "--remove [REPO1 REPO2 ...]" per flag. Valid actions are {'metadata/read', 'metadata/write', 'content/write', 'content/delete', 'content/read'}
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr connected-registry permissions update", locals())


def show(name, registry, resource_group=None):
    '''
    Show the connected registry sync scope map information.

    Required Parameters:
    - name -- Name for the connected registry. Name must be between 5 to 40 character long, start with a letter and contain only alphanumeric characters (including ‘_’ or ‘-’). Name must be unique under the Cloud ACR hierarchy.
    - registry -- The login server of the Cloud ACR registry. Must be the FQDN to support also Azure Stack.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr connected-registry permissions show", locals())

