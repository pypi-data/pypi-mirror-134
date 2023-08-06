'''
Manage Synapse's datasets.
'''
from ... pyaz_utils import _call_az

def create(file, name, workspace_name, no_wait=None):
    '''
    Create a dataset.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The dataset name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse dataset create", locals())


def set(file, name, workspace_name, no_wait=None):
    '''
    Update an exist dataset.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The dataset name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse dataset set", locals())


def update(file, name, workspace_name, no_wait=None):
    '''
    Update an exist dataset.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The dataset name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse dataset update", locals())


def list(workspace_name):
    '''
    List datasets.

    Required Parameters:
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse dataset list", locals())


def show(name, workspace_name):
    '''
    Get a dataset.

    Required Parameters:
    - name -- The dataset name.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse dataset show", locals())


def delete(name, workspace_name, no_wait=None, yes=None):
    '''
    Delete a dataset.

    Required Parameters:
    - name -- The dataset name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse dataset delete", locals())

