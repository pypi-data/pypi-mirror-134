from ... pyaz_utils import _call_az

def create(file, name, workspace_name, no_wait=None):
    '''
    Create a linked service.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The linked service name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse linked-service create", locals())


def set(file, name, workspace_name, no_wait=None):
    '''
    Update an exist linked service.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The linked service name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse linked-service set", locals())


def update(file, name, workspace_name, no_wait=None):
    '''
    Update an exist linked service.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The linked service name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse linked-service update", locals())


def list(workspace_name):
    '''
    List linked services.

    Required Parameters:
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse linked-service list", locals())


def show(name, workspace_name):
    '''
    Get a linked service.

    Required Parameters:
    - name -- The linked service name.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse linked-service show", locals())


def delete(name, workspace_name, no_wait=None, yes=None):
    '''
    Delete a linked service.

    Required Parameters:
    - name -- The linked service name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse linked-service delete", locals())

