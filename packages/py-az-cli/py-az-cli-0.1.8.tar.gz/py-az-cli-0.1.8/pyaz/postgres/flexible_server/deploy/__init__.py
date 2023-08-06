from .... pyaz_utils import _call_az

def setup(admin_password, admin_user, database_name, repo, resource_group, server_name, sql_file, action_name=None, allow_push=None, branch=None):
    '''
    Create github action workflow file for PostgreSQL server.

    Required Parameters:
    - admin_password -- The password of the administrator. Minimum 8 characters and maximum 128 characters. Password must contain characters from three of the following categories: English uppercase letters, English lowercase letters, numbers, and non-alphanumeric characters.
    - admin_user -- Administrator username for the server. Once set, it cannot be changed. 
    - database_name -- The name of the database to be created when provisioning the database server
    - repo -- The name of your github username and repository e.g., Azure/azure-cli 
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - sql_file -- The path of the sql file. The sql file should be already in the repository

    Optional Parameters:
    - action_name -- The name of the github action
    - allow_push -- Push the action yml file to the remote repository. The changes will be pushed to origin repository, speicified branch or current branch if not specified.
    - branch -- The name of the branch you want upload github action file. The default will be your current branch.
    '''
    return _call_az("az postgres flexible-server deploy setup", locals())


def run(action_name, branch):
    '''
    Run an existing workflow in your github repository

    Required Parameters:
    - action_name -- The name of the github action
    - branch -- The name of the branch you want upload github action file. The default will be your current branch.
    '''
    return _call_az("az postgres flexible-server deploy run", locals())

