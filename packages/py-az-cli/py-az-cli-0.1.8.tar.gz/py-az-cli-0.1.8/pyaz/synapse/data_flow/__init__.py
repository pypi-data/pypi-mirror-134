from ... pyaz_utils import _call_az

def create(file, name, workspace_name, no_wait=None):
    '''
    Create a data flow.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The data flow name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse data-flow create", locals())


def set(file, name, workspace_name, no_wait=None):
    '''
    Set an exist data flow.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The data flow name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse data-flow set", locals())


def list(workspace_name):
    '''
    List data flows.

    Required Parameters:
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse data-flow list", locals())


def show(name, workspace_name):
    '''
    Get a data flow.

    Required Parameters:
    - name -- The data flow name.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse data-flow show", locals())


def delete(name, workspace_name, no_wait=None, yes=None):
    '''
    Delete a data flow.

    Required Parameters:
    - name -- The data flow name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse data-flow delete", locals())

