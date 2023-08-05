'''
Manage Synapse Spark sessions.
'''
from .... pyaz_utils import _call_az

def create(executor_size, executors, name, spark_pool_name, workspace_name, configuration=None, reference_files=None, tags=None):
    '''
    Create a Spark session.

    Required Parameters:
    - executor_size -- The executor size
    - executors -- The number of executors.
    - name -- The Spark session name.
    - spark_pool_name -- The name of the Spark pool.
    - workspace_name -- The name of the workspace.

    Optional Parameters:
    - configuration -- The configuration of Spark session.
    - reference_files -- Additional files used for reference in the main definition file.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az synapse spark session create", locals())


def list(spark_pool_name, workspace_name, from_index=None, size=None):
    '''
    List all Spark sessions.

    Required Parameters:
    - spark_pool_name -- The name of the Spark pool.
    - workspace_name -- The name of the workspace.

    Optional Parameters:
    - from_index -- Optional parameter specifying which index the list should begin from.
    - size -- The size of the returned list.By default it is 20 and that is the maximum.
    '''
    return _call_az("az synapse spark session list", locals())


def show(livy_id, spark_pool_name, workspace_name):
    '''
    Get a Spark session.

    Required Parameters:
    - livy_id -- The id of the Spark session job.
    - spark_pool_name -- The name of the Spark pool.
    - workspace_name -- The name of the workspace.
    '''
    return _call_az("az synapse spark session show", locals())


def cancel(livy_id, spark_pool_name, workspace_name, yes=None):
    '''
    Cancel a Spark session.

    Required Parameters:
    - livy_id -- The id of the Spark session job.
    - spark_pool_name -- The name of the Spark pool.
    - workspace_name -- The name of the workspace.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse spark session cancel", locals())


def reset_timeout(livy_id, spark_pool_name, workspace_name):
    '''
    Reset a Spark session timeout time.

    Required Parameters:
    - livy_id -- The id of the Spark session job.
    - spark_pool_name -- The name of the Spark pool.
    - workspace_name -- The name of the workspace.
    '''
    return _call_az("az synapse spark session reset-timeout", locals())

