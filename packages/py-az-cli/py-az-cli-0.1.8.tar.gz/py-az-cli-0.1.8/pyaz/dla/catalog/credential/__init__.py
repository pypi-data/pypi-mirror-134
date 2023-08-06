'''
Manage Data Lake Analytics catalog credentials.
'''
from .... pyaz_utils import _call_az

def create(account, credential_name, database_name, uri, user_name, password=None):
    '''
    Create a new catalog credential for use with an external data source.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - credential_name -- None
    - database_name -- None
    - uri -- URI of the external data source.
    - user_name -- None

    Optional Parameters:
    - password -- Password for the credential user. Will prompt if not given.
    '''
    return _call_az("az dla catalog credential create", locals())


def show(account, credential_name, database_name):
    '''
    Retrieve a catalog credential.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - credential_name -- The name of the credential.
    - database_name -- The name of the database containing the schema.
    '''
    return _call_az("az dla catalog credential show", locals())


def update(account, credential_name, database_name, uri, user_name, new_password=None, password=None):
    '''
    Update a catalog credential for use with an external data source.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - credential_name -- None
    - database_name -- None
    - uri -- URI of the external data source.
    - user_name -- None

    Optional Parameters:
    - new_password -- New password for the credential user. Will prompt if not given.
    - password -- Current password for the credential user. Will prompt if not given.
    '''
    return _call_az("az dla catalog credential update", locals())


def list(account, database_name, count=None, filter=None, orderby=None, select=None, skip=None, top=None):
    '''
    List catalog credentials.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - database_name -- The name of the database containing the schema.

    Optional Parameters:
    - count -- The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true.
    - filter -- OData filter. Optional.
    - orderby -- OrderBy clause. One or more comma-separated expressions with an optional "asc" (the default) or "desc" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    - select -- OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    - skip -- The number of items to skip over before returning elements.
    - top -- Maximum number of items to return.
    '''
    return _call_az("az dla catalog credential list", locals())


def delete(account, credential_name, database_name, cascade=None, password=None):
    '''
    Delete a catalog credential.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - credential_name -- The name of the credential to delete
    - database_name -- The name of the database containing the credential.

    Optional Parameters:
    - cascade -- Indicates if the delete should be a cascading delete (which deletes all resources dependent on the credential as well as the credential) or not. If false will fail if there are any resources relying on the credential.
    - password -- the current password for the credential and user with access to the data source. This is required if the requester is not the account owner.
    '''
    return _call_az("az dla catalog credential delete", locals())

