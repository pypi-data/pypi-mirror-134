'''
Manage Data Lake Analytics catalog table valued functions.
'''
from .... pyaz_utils import _call_az

def show(account, database_name, schema_name, table_valued_function_name):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - database_name -- The name of the database containing the table valued function.
    - schema_name -- The name of the schema containing the table valued function.
    - table_valued_function_name -- The name of the tableValuedFunction.
    '''
    return _call_az("az dla catalog tvf show", locals())


def list(account, database_name, schema_name=None):
    '''
    List table valued functions in a database or schema.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - database_name -- None

    Optional Parameters:
    - schema_name -- None
    '''
    return _call_az("az dla catalog tvf list", locals())

