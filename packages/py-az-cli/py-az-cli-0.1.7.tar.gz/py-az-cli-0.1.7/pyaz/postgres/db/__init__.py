'''
Manage PostgreSQL databases on a server.
'''
from ... pyaz_utils import _call_az

def create(name, resource_group, server_name, charset=None, collation=None):
    '''
    Create a PostgreSQL database.

    Required Parameters:
    - name -- The name of the database
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.

    Optional Parameters:
    - charset -- The charset of the database
    - collation -- The collation of the database
    '''
    return _call_az("az postgres db create", locals())


def delete(name, resource_group, server_name, yes=None):
    '''
    Delete a database.

    Required Parameters:
    - name -- The name of the database
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az postgres db delete", locals())


def show(name, resource_group, server_name):
    '''
    Show the details of a database.

    Required Parameters:
    - name -- The name of the database
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    '''
    return _call_az("az postgres db show", locals())


def list(resource_group, server_name):
    '''
    List the databases for a server.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the Server.
    '''
    return _call_az("az postgres db list", locals())

