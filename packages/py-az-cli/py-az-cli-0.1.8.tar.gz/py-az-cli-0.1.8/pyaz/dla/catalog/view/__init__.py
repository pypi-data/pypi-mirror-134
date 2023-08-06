'''
Manage Data Lake Analytics catalog views.
'''
from .... pyaz_utils import _call_az

def show(account, database_name, schema_name, view_name):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - database_name -- The name of the database containing the view.
    - schema_name -- The name of the schema containing the view.
    - view_name -- The name of the view.
    '''
    return _call_az("az dla catalog view show", locals())


def list(account, database_name, schema_name=None):
    '''
    List views in a database or schema.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - database_name -- None

    Optional Parameters:
    - schema_name -- None
    '''
    return _call_az("az dla catalog view list", locals())

