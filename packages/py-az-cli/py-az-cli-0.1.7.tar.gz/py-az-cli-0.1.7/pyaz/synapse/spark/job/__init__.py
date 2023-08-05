'''
Manage Synapse Spark batch jobs.
'''
from .... pyaz_utils import _call_az

def submit(executor_size, executors, main_definition_file, name, spark_pool_name, workspace_name, archives=None, arguments=None, configuration=None, language=None, main_class_name=None, reference_files=None, tags=None):
    '''
    Submit a Spark job.

    Required Parameters:
    - executor_size -- The executor size
    - executors -- The number of executors.
    - main_definition_file -- The main file used for the job.
    - name -- The Spark job name.
    - spark_pool_name -- The name of the Spark pool.
    - workspace_name -- The name of the workspace.

    Optional Parameters:
    - archives -- The array of archives.
    - arguments -- Optional arguments to the job (Note: please use storage URIs for file arguments).
    - configuration -- The configuration of Spark job.
    - language -- The Spark job language.
    - main_class_name -- The fully-qualified identifier or the main class that is in the main definition file.
    - reference_files -- Additional files used for reference in the main definition file.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az synapse spark job submit", locals())


def list(spark_pool_name, workspace_name, from_index=None, size=None):
    '''
    List all Spark jobs.

    Required Parameters:
    - spark_pool_name -- The name of the Spark pool.
    - workspace_name -- The name of the workspace.

    Optional Parameters:
    - from_index -- Optional parameter specifying which index the list should begin from.
    - size -- The size of the returned list.By default it is 20 and that is the maximum.
    '''
    return _call_az("az synapse spark job list", locals())


def show(livy_id, spark_pool_name, workspace_name):
    '''
    Get a Spark job.

    Required Parameters:
    - livy_id -- The id of the Spark job.
    - spark_pool_name -- The name of the Spark pool.
    - workspace_name -- The name of the workspace.
    '''
    return _call_az("az synapse spark job show", locals())


def cancel(livy_id, spark_pool_name, workspace_name, yes=None):
    '''
    Cancel a Spark job.

    Required Parameters:
    - livy_id -- The id of the Spark job.
    - spark_pool_name -- The name of the Spark pool.
    - workspace_name -- The name of the workspace.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse spark job cancel", locals())

