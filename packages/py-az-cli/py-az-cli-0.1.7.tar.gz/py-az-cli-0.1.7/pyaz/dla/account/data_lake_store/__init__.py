from .... pyaz_utils import _call_az

def show(account, data_lake_store_account_name, resource_group=None):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - data_lake_store_account_name -- The name of the Data Lake Store account to retrieve

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    '''
    return _call_az("az dla account data-lake-store show", locals())


def list(account, count=None, filter=None, orderby=None, resource_group=None, select=None, skip=None, top=None):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.

    Optional Parameters:
    - count -- The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true.
    - filter -- OData filter. Optional.
    - orderby -- OrderBy clause. One or more comma-separated expressions with an optional "asc" (the default) or "desc" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    - select -- OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    - skip -- The number of items to skip over before returning elements.
    - top -- Maximum number of items to return.
    '''
    return _call_az("az dla account data-lake-store list", locals())


def add(account, data_lake_store_account_name, resource_group=None, suffix=None):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - data_lake_store_account_name -- The name of the Data Lake Store account to add.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    - suffix -- the optional suffix for the Data Lake Store account.
    '''
    return _call_az("az dla account data-lake-store add", locals())


def delete(account, data_lake_store_account_name, resource_group=None):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - data_lake_store_account_name -- The name of the Data Lake Store account to remove

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    '''
    return _call_az("az dla account data-lake-store delete", locals())

