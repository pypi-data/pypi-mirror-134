from .... pyaz_utils import _call_az

def create(resource_group, server_name, charset=None, collation=None, database_name=None):
    '''
    Create a PostgreSQL database on a flexible server.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.

    Optional Parameters:
    - charset -- The charset of the database. The default value is UTF8
    - collation -- The collation of the database.
    - database_name -- The name of the database to be created when provisioning the database server
    '''
    return _call_az("az postgres flexible-server db create", locals())


def delete(database_name=None, resource_group=None, server_name=None, yes=None):
    '''
    Delete a database on a flexible server.

    Optional Parameters:
    - database_name -- The name of the database to be created when provisioning the database server
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az postgres flexible-server db delete", locals())


def show(database_name, resource_group, server_name):
    '''
    Show the details of a database.

    Required Parameters:
    - database_name -- The name of the database to be created when provisioning the database server
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    '''
    return _call_az("az postgres flexible-server db show", locals())


def list(resource_group, server_name):
    '''
    List the databases for a flexible server.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    '''
    return _call_az("az postgres flexible-server db list", locals())

