'''
Manage repositories (image names) for Azure Container Registries.
'''
from ... pyaz_utils import _call_az

def list(name, password=None, resource_group=None, suffix=None, top=None, username=None):
    '''
    List repositories in an Azure Container Registry.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - password -- The password used to log into a container registry
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - suffix -- The tenant suffix in registry login server. You may specify '--suffix tenant' if your registry login server is in the format 'registry-tenant.azurecr.io'. Applicable if you're accessing the registry from a different subscription or you have permission to access images but not the permission to manage the registry resource.
    - top -- Limit the number of items in the results.
    - username -- The username used to log into a container registry
    '''
    return _call_az("az acr repository list", locals())


def show_tags(name, repository, detail=None, orderby=None, password=None, resource_group=None, suffix=None, top=None, username=None):
    '''
    Show tags for a repository in an Azure Container Registry.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`
    - repository -- The name of the repository.

    Optional Parameters:
    - detail -- Show detailed information.
    - orderby -- Order the items in the results. Default to alphabetical order of names.
    - password -- The password used to log into a container registry
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - suffix -- The tenant suffix in registry login server. You may specify '--suffix tenant' if your registry login server is in the format 'registry-tenant.azurecr.io'. Applicable if you're accessing the registry from a different subscription or you have permission to access images but not the permission to manage the registry resource.
    - top -- Limit the number of items in the results.
    - username -- The username used to log into a container registry
    '''
    return _call_az("az acr repository show-tags", locals())


def show_manifests(name, repository, detail=None, orderby=None, password=None, resource_group=None, suffix=None, top=None, username=None):
    '''
    Show manifests of a repository in an Azure Container Registry.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`
    - repository -- The name of the repository.

    Optional Parameters:
    - detail -- Show detailed information.
    - orderby -- Order the items in the results. Default to alphabetical order of names.
    - password -- The password used to log into a container registry
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - suffix -- The tenant suffix in registry login server. You may specify '--suffix tenant' if your registry login server is in the format 'registry-tenant.azurecr.io'. Applicable if you're accessing the registry from a different subscription or you have permission to access images but not the permission to manage the registry resource.
    - top -- Limit the number of items in the results.
    - username -- The username used to log into a container registry
    '''
    return _call_az("az acr repository show-manifests", locals())


def show(name, image=None, password=None, repository=None, resource_group=None, suffix=None, username=None):
    '''
    Get the attributes of a repository or image in an Azure Container Registry.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - image -- The name of the image. May include a tag in the format 'name:tag' or digest in the format 'name@digest'.
    - password -- The password used to log into a container registry
    - repository -- The name of the repository.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - suffix -- The tenant suffix in registry login server. You may specify '--suffix tenant' if your registry login server is in the format 'registry-tenant.azurecr.io'. Applicable if you're accessing the registry from a different subscription or you have permission to access images but not the permission to manage the registry resource.
    - username -- The username used to log into a container registry
    '''
    return _call_az("az acr repository show", locals())


def update(name, delete_enabled=None, image=None, list_enabled=None, password=None, read_enabled=None, repository=None, resource_group=None, suffix=None, username=None, write_enabled=None):
    '''
    Update the attributes of a repository or image in an Azure Container Registry.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - delete_enabled -- Indicates whether delete operation is allowed.
    - image -- The name of the image. May include a tag in the format 'name:tag' or digest in the format 'name@digest'.
    - list_enabled -- Indicates whether this item shows in list operation results.
    - password -- The password used to log into a container registry
    - read_enabled -- Indicates whether read operation is allowed.
    - repository -- The name of the repository.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - suffix -- The tenant suffix in registry login server. You may specify '--suffix tenant' if your registry login server is in the format 'registry-tenant.azurecr.io'. Applicable if you're accessing the registry from a different subscription or you have permission to access images but not the permission to manage the registry resource.
    - username -- The username used to log into a container registry
    - write_enabled -- Indicates whether write or delete operation is allowed.
    '''
    return _call_az("az acr repository update", locals())


def delete(name, image=None, password=None, repository=None, resource_group=None, suffix=None, username=None, yes=None):
    '''
    Delete a repository or image in an Azure Container Registry.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - image -- The name of the image. May include a tag in the format 'name:tag' or digest in the format 'name@digest'.
    - password -- The password used to log into a container registry
    - repository -- The name of the repository.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - suffix -- The tenant suffix in registry login server. You may specify '--suffix tenant' if your registry login server is in the format 'registry-tenant.azurecr.io'. Applicable if you're accessing the registry from a different subscription or you have permission to access images but not the permission to manage the registry resource.
    - username -- The username used to log into a container registry
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az acr repository delete", locals())


def untag(image, name, password=None, resource_group=None, suffix=None, username=None):
    '''
    Untag an image in an Azure Container Registry.

    Required Parameters:
    - image -- The name of the image. May include a tag in the format 'name:tag'.
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - password -- The password used to log into a container registry
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - suffix -- The tenant suffix in registry login server. You may specify '--suffix tenant' if your registry login server is in the format 'registry-tenant.azurecr.io'. Applicable if you're accessing the registry from a different subscription or you have permission to access images but not the permission to manage the registry resource.
    - username -- The username used to log into a container registry
    '''
    return _call_az("az acr repository untag", locals())

