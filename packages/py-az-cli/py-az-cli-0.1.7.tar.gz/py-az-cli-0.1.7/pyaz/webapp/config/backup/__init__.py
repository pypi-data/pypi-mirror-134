'''
Manage backups for web apps.
'''
from .... pyaz_utils import _call_az

def list(resource_group, webapp_name, slot=None):
    '''
    List backups of a web app.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - webapp_name -- The name of the web app

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config backup list", locals())


def show(resource_group, webapp_name, slot=None):
    '''
    Show the backup schedule for a web app.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - webapp_name -- The name of the web app

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config backup show", locals())


def create(container_url, resource_group, webapp_name, backup_name=None, db_connection_string=None, db_name=None, db_type=None, slot=None):
    '''
    Create a backup of a web app.

    Required Parameters:
    - container_url -- URL with SAS token to the blob storage container
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - webapp_name -- The name of the web app

    Optional Parameters:
    - backup_name -- Name of the backup. If unspecified, the backup will be named with the web app name and a timestamp
    - db_connection_string -- Connection string for the database in the backup
    - db_name -- Name of the database in the backup
    - db_type -- Type of database in the backup
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config backup create", locals())


def update(resource_group, webapp_name, backup_name=None, container_url=None, db_connection_string=None, db_name=None, db_type=None, frequency=None, retain_one=None, retention=None, slot=None):
    '''
    Configure a new backup schedule for a web app.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - webapp_name -- The name of the web app

    Optional Parameters:
    - backup_name -- Name of the backup. If unspecified, the backup will be named with the web app name and a timestamp
    - container_url -- URL with SAS token to the blob storage container
    - db_connection_string -- Connection string for the database in the backup
    - db_name -- Name of the database in the backup
    - db_type -- Type of database in the backup
    - frequency -- How often to backup. Use a number followed by d or h, e.g. 5d = 5 days, 2h = 2 hours
    - retain_one -- Always keep one backup, regardless of how old it is
    - retention -- How many days to keep a backup before automatically deleting it. Set to 0 for indefinite retention
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config backup update", locals())


def restore(backup_name, container_url, resource_group, webapp_name, db_connection_string=None, db_name=None, db_type=None, ignore_hostname_conflict=None, overwrite=None, slot=None, target_name=None):
    '''
    Restore a web app from a backup.

    Required Parameters:
    - backup_name -- Name of the backup to restore
    - container_url -- URL with SAS token to the blob storage container
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - webapp_name -- The name of the web app

    Optional Parameters:
    - db_connection_string -- Connection string for the database in the backup
    - db_name -- Name of the database in the backup
    - db_type -- Type of database in the backup
    - ignore_hostname_conflict -- Ignores custom hostnames stored in the backup
    - overwrite -- Overwrite the source web app, if --target-name is not specified
    - slot -- the name of the slot. Default to the productions slot if not specified
    - target_name -- The name to use for the restored web app. If unspecified, will default to the name that was used when the backup was created
    '''
    return _call_az("az webapp config backup restore", locals())

