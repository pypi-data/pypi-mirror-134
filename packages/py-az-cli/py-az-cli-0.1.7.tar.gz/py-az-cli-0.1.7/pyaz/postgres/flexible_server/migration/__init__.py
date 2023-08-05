from .... pyaz_utils import _call_az

def create(name, properties, resource_group, migration_name=None):
    '''
    Create a new migration workflow for a flexible server.

    Required Parameters:
    - name -- Migration target server name.
    - properties -- Request properties. Use double or no quotes to pass in filepath as argument.
    - resource_group -- Resource Group Name of the migration target server.

    Optional Parameters:
    - migration_name -- Name of the migration.
    '''
    return _call_az("az postgres flexible-server migration create", locals())


def show(migration_name, name, resource_group, level=None):
    '''
    Get the details of a specific migration.

    Required Parameters:
    - migration_name -- Name of the migration.
    - name -- Migration target server name.
    - resource_group -- Resource Group Name of the migration target server.

    Optional Parameters:
    - level -- Specify the level of migration details requested. Valid values are Active and All. Active is the default.
    '''
    return _call_az("az postgres flexible-server migration show", locals())


def list(name, resource_group, filter=None):
    '''
    List the migrations of a flexible server.

    Required Parameters:
    - name -- Migration target server name.
    - resource_group -- Resource Group Name of the migration target server.

    Optional Parameters:
    - filter -- Indicate whether all the migrations or just the Active migrations are returned. Active is the default. Valid values are: Active, All.
    '''
    return _call_az("az postgres flexible-server migration list", locals())


def update(migration_name, name, resource_group, cutover=None, db_names=None, overwrite_dbs=None, setup_replication=None, start_data_migration=None):
    '''
    Update a specific migration.

    Required Parameters:
    - migration_name -- Name of the migration.
    - name -- Migration target server name.
    - resource_group -- Resource Group Name of the migration target server.

    Optional Parameters:
    - cutover -- Cut-over the data migration. After this is complete, subsequent updates to the source DB will not be migrated to the target.
    - db_names -- Space-separated list of DBs to migrate. A minimum of 1 and a maximum of 8 DBs can be specified. You can migrate more DBs concurrently using additional migrations. Note that each additional DB affects the performance of the source server.
    - overwrite_dbs -- Allow the migration workflow to overwrite the DB on the target.
    - setup_replication -- Allow the migration workflow to setup logical replication on the source. Note that this command will restart the source server.
    - start_data_migration -- Reschedule the data migration to start right now.
    '''
    return _call_az("az postgres flexible-server migration update", locals())


def delete(migration_name, name, resource_group, yes=None):
    '''
    Delete a specific migration.

    Required Parameters:
    - migration_name -- Name of the migration.
    - name -- Migration target server name.
    - resource_group -- Resource Group Name of the migration target server.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az postgres flexible-server migration delete", locals())


def check_name_availability(migration_name, name, resource_group):
    '''
    Checks if the provided migration-name can be used.

    Required Parameters:
    - migration_name -- Name of the migration.
    - name -- Migration target server name.
    - resource_group -- Resource Group Name of the migration target server.
    '''
    return _call_az("az postgres flexible-server migration check-name-availability", locals())

