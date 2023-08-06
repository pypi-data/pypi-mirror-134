from ... pyaz_utils import _call_az

def list(resource_group, server_name, file_last_written=None, filename_contains=None, max_file_size=None):
    '''
    List log files for a server.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the Server.

    Optional Parameters:
    - file_last_written -- Integer in hours to indicate file last modify time, default value is 72.
    - filename_contains -- The pattern that file name should match.
    - max_file_size -- The file size limitation to filter files.
    '''
    return _call_az("az mariadb server-logs list", locals())


def download(name, resource_group, server_name):
    '''
    Download log files.

    Required Parameters:
    - name -- Space-separated list of log filenames on the server to download.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    '''
    return _call_az("az mariadb server-logs download", locals())

