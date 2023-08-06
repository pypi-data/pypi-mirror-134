from ... pyaz_utils import _call_az

def list(workspace_name):
    '''
    List spark job definitions.

    Required Parameters:
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse spark-job-definition list", locals())


def show(name, workspace_name):
    '''
    Get a spark job definition.

    Required Parameters:
    - name -- The spark job definition name
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse spark-job-definition show", locals())


def delete(name, workspace_name, no_wait=None):
    '''
    Delete a spark job definition.

    Required Parameters:
    - name -- The spark job definition name
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse spark-job-definition delete", locals())


def create(file, name, workspace_name, folder_path=None, no_wait=None):
    '''
    Create a spark job definition.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The spark job definition name
    - workspace_name -- The workspace name.

    Optional Parameters:
    - folder_path -- The folder that this spark job definition is in. If not specified, it will appear at the root level. Eg: folder/subfolder1
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse spark-job-definition create", locals())


def wait(name, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of a spark job definition is met.

    Required Parameters:
    - name -- The spark job definition name
    - workspace_name -- The workspace name.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az synapse spark-job-definition wait", locals())


def update(file, name, workspace_name, folder_path=None, no_wait=None):
    '''
    Update a spark job definition.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The spark job definition name
    - workspace_name -- The workspace name.

    Optional Parameters:
    - folder_path -- The folder that this spark job definition is in. If not specified, it will appear at the root level. Eg: folder/subfolder1
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse spark-job-definition update", locals())

