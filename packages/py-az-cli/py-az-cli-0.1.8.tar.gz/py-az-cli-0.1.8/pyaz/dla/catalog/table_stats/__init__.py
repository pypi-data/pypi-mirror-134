from .... pyaz_utils import _call_az

def show(account, database_name, schema_name, statistics_name, table_name):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - database_name -- The name of the database containing the statistics.
    - schema_name -- The name of the schema containing the statistics.
    - statistics_name -- The name of the table statistics.
    - table_name -- The name of the table containing the statistics.
    '''
    return _call_az("az dla catalog table-stats show", locals())


def list(account, database_name, schema_name=None, table_name=None):
    '''
    List table statistics in a database, table, or schema.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - database_name -- None

    Optional Parameters:
    - schema_name -- None
    - table_name -- None
    '''
    return _call_az("az dla catalog table-stats list", locals())

