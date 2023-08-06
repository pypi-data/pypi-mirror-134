'''
Manage Synapse Spark statements.
'''
from .... pyaz_utils import _call_az

def invoke(code, language, session_id, spark_pool_name, workspace_name):
    '''
    Invoke a Spark statement.

    Required Parameters:
    - code -- The code of Spark statement. This is either the code contents or use `@<file path>` to load the content from a file
    - language -- The language of Spark statement.
    - session_id -- The id of Spark session.
    - spark_pool_name -- The name of the Spark pool.
    - workspace_name -- The name of the workspace.
    '''
    return _call_az("az synapse spark statement invoke", locals())


def list(session_id, spark_pool_name, workspace_name):
    '''
    List all Spark statements

    Required Parameters:
    - session_id -- The id of Spark session.
    - spark_pool_name -- The name of the Spark pool.
    - workspace_name -- The name of the workspace.
    '''
    return _call_az("az synapse spark statement list", locals())


def show(livy_id, session_id, spark_pool_name, workspace_name):
    '''
    Get a Spark statement.

    Required Parameters:
    - livy_id -- The id of the statement.
    - session_id -- The id of Spark session.
    - spark_pool_name -- The name of the Spark pool.
    - workspace_name -- The name of the workspace.
    '''
    return _call_az("az synapse spark statement show", locals())


def cancel(livy_id, session_id, spark_pool_name, workspace_name, yes=None):
    '''
    Cancel a Spark statement.

    Required Parameters:
    - livy_id -- The id of the statement.
    - session_id -- The id of Spark session.
    - spark_pool_name -- The name of the Spark pool.
    - workspace_name -- The name of the workspace.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse spark statement cancel", locals())

