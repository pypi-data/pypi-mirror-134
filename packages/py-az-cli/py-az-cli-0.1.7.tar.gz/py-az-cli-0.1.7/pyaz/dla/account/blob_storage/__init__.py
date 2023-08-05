from .... pyaz_utils import _call_az

def show(account, storage_account_name, resource_group=None):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - storage_account_name -- Name of an existing storage account to link to.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    '''
    return _call_az("az dla account blob-storage show", locals())


def add(access_key, account, storage_account_name, resource_group=None, suffix=None):
    '''
    Links an Azure Storage account to the specified Data Lake Analytics account.

    Required Parameters:
    - access_key -- the access key associated with this Azure Storage account that will be used to connect to it
    - account -- Name of the Data Lake Analytics account.
    - storage_account_name -- Name of an existing storage account to link to.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    - suffix -- the optional suffix for the storage account
    '''
    return _call_az("az dla account blob-storage add", locals())


def update(access_key, account, storage_account_name, resource_group=None, suffix=None):
    '''
    Updates an Azure Storage account linked to the specified Data Lake Analytics account.

    Required Parameters:
    - access_key -- the access key associated with this Azure Storage account that will be used to connect to it
    - account -- Name of the Data Lake Analytics account.
    - storage_account_name -- Name of an existing storage account to link to.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    - suffix -- the optional suffix for the storage account
    '''
    return _call_az("az dla account blob-storage update", locals())


def delete(account, storage_account_name, resource_group=None):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - storage_account_name -- Name of an existing storage account to link to.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    '''
    return _call_az("az dla account blob-storage delete", locals())


def list(account, count=None, filter=None, orderby=None, resource_group=None, select=None, skip=None, top=None):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.

    Optional Parameters:
    - count -- The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true.
    - filter -- The OData filter. Optional.
    - orderby -- OrderBy clause. One or more comma-separated expressions with an optional "asc" (the default) or "desc" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    - select -- OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    - skip -- The number of items to skip over before returning elements.
    - top -- Maximum number of items to return.
    '''
    return _call_az("az dla account blob-storage list", locals())

