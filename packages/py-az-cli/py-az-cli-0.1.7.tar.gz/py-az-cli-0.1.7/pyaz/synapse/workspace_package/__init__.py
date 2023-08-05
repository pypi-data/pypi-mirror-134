from ... pyaz_utils import _call_az

def upload(package, workspace_name, no_progress=None):
    '''
    Upload a local workspace package file to an Azure Synapse workspace.

    Required Parameters:
    - package -- Specifies a local file path for a file to upload as workspace package.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_progress -- Include this flag to disable progress reporting for the command.
    '''
    return _call_az("az synapse workspace-package upload", locals())


def upload_batch(source, workspace_name, no_progress=None):
    '''
    Upload workspace package files from a local directory to an Azure Synapse workspace.

    Required Parameters:
    - source -- The directory where the files to be uploaded are located.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_progress -- Include this flag to disable progress reporting for the command.
    '''
    return _call_az("az synapse workspace-package upload-batch", locals())


def list(workspace_name):
    '''
    List workspace packages.

    Required Parameters:
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse workspace-package list", locals())


def show(package_name, workspace_name):
    '''
    Get a workspace package.

    Required Parameters:
    - package_name -- The workspace package name.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse workspace-package show", locals())


def delete(package_name, workspace_name, no_wait=None, yes=None):
    '''
    Delete a workspace package.

    Required Parameters:
    - package_name -- The workspace package name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse workspace-package delete", locals())

