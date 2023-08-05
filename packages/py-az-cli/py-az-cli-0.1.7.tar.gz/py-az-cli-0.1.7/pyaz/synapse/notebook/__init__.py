'''
Manage Synapse's notebooks.
'''
from ... pyaz_utils import _call_az

def create(file, name, workspace_name, executor_count=None, executor_size=None, folder_path=None, no_wait=None, spark_pool_name=None):
    '''
    Create a notebook.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The notebook name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - executor_count -- Number of executors to be allocated in the specified Spark pool for the job.
    - executor_size -- Number of core and memory to be used for executors allocated in the specified Spark pool for the job.
    - folder_path -- The folder that this notebook is in. If not specified, this notebook will appear at the root level. Eg: folder/subfolder1
    - no_wait -- Do not wait for the long-running operation to finish.
    - spark_pool_name -- The name of the Spark pool.
    '''
    return _call_az("az synapse notebook create", locals())


def set(file, name, workspace_name, executor_count=None, executor_size=None, folder_path=None, no_wait=None, spark_pool_name=None):
    '''
    Set an exist notebook.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The notebook name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - executor_count -- Number of executors to be allocated in the specified Spark pool for the job.
    - executor_size -- Number of core and memory to be used for executors allocated in the specified Spark pool for the job.
    - folder_path -- The folder that this notebook is in. If not specified, this notebook will appear at the root level. Eg: folder/subfolder1
    - no_wait -- Do not wait for the long-running operation to finish.
    - spark_pool_name -- The name of the Spark pool.
    '''
    return _call_az("az synapse notebook set", locals())


def import_(file, name, workspace_name, executor_count=None, executor_size=None, folder_path=None, no_wait=None, spark_pool_name=None):
    '''
    Import a notebook.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The notebook name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - executor_count -- Number of executors to be allocated in the specified Spark pool for the job.
    - executor_size -- Number of core and memory to be used for executors allocated in the specified Spark pool for the job.
    - folder_path -- The folder that this notebook is in. If not specified, this notebook will appear at the root level. Eg: folder/subfolder1
    - no_wait -- Do not wait for the long-running operation to finish.
    - spark_pool_name -- The name of the Spark pool.
    '''
    return _call_az("az synapse notebook import", locals())


def list(workspace_name):
    '''
    List notebooks.

    Required Parameters:
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse notebook list", locals())


def show(name, workspace_name):
    '''
    Get a notebook.

    Required Parameters:
    - name -- The notebook name.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse notebook show", locals())


def export(output_folder, workspace_name, name=None):
    '''
    Export notebooks.

    Required Parameters:
    - output_folder -- The folder where the notebook should be placed.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - name -- The notebook name.
    '''
    return _call_az("az synapse notebook export", locals())


def delete(name, workspace_name, no_wait=None, yes=None):
    '''
    Delete a notebook.

    Required Parameters:
    - name -- The notebook name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse notebook delete", locals())

