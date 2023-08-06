'''
Manage Data Lake Analytics catalog tables.
'''
from .... pyaz_utils import _call_az

def show(account, database_name, schema_name, table_name):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - database_name -- The name of the database containing the table.
    - schema_name -- The name of the schema containing the table.
    - table_name -- The name of the table.
    '''
    return _call_az("az dla catalog table show", locals())


def list(account, database_name, schema_name=None):
    '''
    List tables in a database or schema.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - database_name -- None

    Optional Parameters:
    - schema_name -- None
    '''
    return _call_az("az dla catalog table list", locals())

