'''
Manage Synapse's pipelines.
'''
from ... pyaz_utils import _call_az

def create(file, name, workspace_name, no_wait=None):
    '''
    Create a pipeline.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The pipeline name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse pipeline create", locals())


def set(file, name, workspace_name, no_wait=None):
    '''
    Update an exist pipeline.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The pipeline name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse pipeline set", locals())


def update(file, name, workspace_name, no_wait=None):
    '''
    Update an exist pipeline.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The pipeline name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse pipeline update", locals())


def list(workspace_name):
    '''
    List pipelines.

    Required Parameters:
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse pipeline list", locals())


def show(name, workspace_name):
    '''
    Get a pipeline.

    Required Parameters:
    - name -- The pipeline name.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse pipeline show", locals())


def delete(name, workspace_name, no_wait=None, yes=None):
    '''
    Delete a pipeline.

    Required Parameters:
    - name -- The pipeline name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse pipeline delete", locals())


def create_run(name, workspace_name, is_recovery=None, parameters=None, reference_pipeline_run_id=None, start_activity_name=None):
    '''
    Creates a run of a pipeline.

    Required Parameters:
    - name -- The pipeline name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - is_recovery -- Recovery mode flag. If recovery mode is set to true, the specified referenced pipeline run and the new run will be grouped under the same groupId.
    - parameters -- Parameters for pipeline run. Can be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - reference_pipeline_run_id -- The pipeline run ID for rerun. If run ID is specified, the parameters of the specified run will be used to create a new run.
    - start_activity_name -- In recovery mode, the rerun will start from this activity. If not specified, all activities will run.
    '''
    return _call_az("az synapse pipeline create-run", locals())

