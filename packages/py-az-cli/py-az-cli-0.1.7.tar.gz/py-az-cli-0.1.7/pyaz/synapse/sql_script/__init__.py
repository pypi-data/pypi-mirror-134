from ... pyaz_utils import _call_az

def list(workspace_name):
    '''
    List SQL scripts in a synapse workspace.

    Required Parameters:
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse sql-script list", locals())


def show(name, workspace_name):
    '''
    Get a SQL script.

    Required Parameters:
    - name -- The SQL script name
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse sql-script show", locals())


def delete(name, workspace_name, no_wait=None):
    '''
    Delete a SQL script.

    Required Parameters:
    - name -- The SQL script name
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse sql-script delete", locals())


def create(file, name, workspace_name, additional_properties=None, description=None, folder_name=None, no_wait=None, result_limit=None, sql_database_name=None, sql_pool_name=None):
    '''
    Create or update a SQL script.

    Required Parameters:
    - file -- The SQL query file path
    - name -- The SQL script name
    - workspace_name -- The workspace name.

    Optional Parameters:
    - additional_properties -- The SQL script additional properties
    - description -- The SQL script description
    - folder_name -- The folder that this SQL script is in. If not specified, this SQL script will appear at the root level. Eg: folder/subfolder1
    - no_wait -- Do not wait for the long-running operation to finish.
    - result_limit -- The SQL query results limit. Default is 5000. '-1' is no limit.
    - sql_database_name -- The SQL database name
    - sql_pool_name -- The SQL pool name
    '''
    return _call_az("az synapse sql-script create", locals())


def wait(name, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of a sql script is met.

    Required Parameters:
    - name -- The SQL script name
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
    return _call_az("az synapse sql-script wait", locals())


def export(output_folder, workspace_name, name=None):
    '''
    Export a SQL script.

    Required Parameters:
    - output_folder -- The SQL script export path
    - workspace_name -- The workspace name.

    Optional Parameters:
    - name -- The SQL script name
    '''
    return _call_az("az synapse sql-script export", locals())


def import_(file, name, workspace_name, additional_properties=None, description=None, folder_name=None, no_wait=None, result_limit=None, sql_database_name=None, sql_pool_name=None):
    '''
    Import a SQL script.

    Required Parameters:
    - file -- The SQL query file path
    - name -- The SQL script name
    - workspace_name -- The workspace name.

    Optional Parameters:
    - additional_properties -- The SQL script additional properties
    - description -- The SQL script description
    - folder_name -- The folder that this SQL script is in. If not specified, this SQL script will appear at the root level. Eg: folder/subfolder1
    - no_wait -- Do not wait for the long-running operation to finish.
    - result_limit -- The SQL query results limit. Default is 5000. '-1' is no limit.
    - sql_database_name -- The SQL database name
    - sql_pool_name -- The SQL pool name
    '''
    return _call_az("az synapse sql-script import", locals())

