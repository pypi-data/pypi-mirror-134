'''
Manage data warehouses.
'''
from ... pyaz_utils import _call_az

def create(name, resource_group, server, backup_storage_redundancy=None, collation=None, max_size=None, no_wait=None, service_objective=None, tags=None, zone_redundant=None):
    '''
    Create a data warehouse.

    Required Parameters:
    - name -- Name of the data warehouse.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - backup_storage_redundancy -- Backup storage redundancy used to store backups. Allowed values include: Local, Zone, Geo.
    - collation -- The collation of the data warehouse.
    - max_size -- The max storage size. If no unit is specified, defaults to bytes (B).
    - no_wait -- Do not wait for the long-running operation to finish.
    - service_objective -- The service objective for the new database. For example: DW100, DW1000c
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - zone_redundant -- Specifies whether to enable zone redundancy
    '''
    return _call_az("az sql dw create", locals())


def show(name, resource_group, server):
    '''
    Get the details for a data warehouse.

    Required Parameters:
    - name -- Name of the data warehouse.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql dw show", locals())


def list(resource_group, server):
    '''
    List data warehouses for a server.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql dw list", locals())


def delete(name, resource_group, server, no_wait=None, yes=None):
    '''
    Delete a data warehouse.

    Required Parameters:
    - name -- Name of the data warehouse.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az sql dw delete", locals())


def pause(name, resource_group, server):
    '''
    

    Required Parameters:
    - name -- Name of the data warehouse.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql dw pause", locals())


def resume(name, resource_group, server):
    '''
    

    Required Parameters:
    - name -- Name of the data warehouse.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql dw resume", locals())


def update(name, resource_group, server, add=None, force_string=None, max_size=None, no_wait=None, remove=None, service_objective=None, set=None):
    '''
    Update a data warehouse.

    Required Parameters:
    - name -- Name of the data warehouse.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - max_size -- The max storage size. If no unit is specified, defaults to bytes (B).
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - service_objective -- The service objective of the data warehouse. For example: DW100, DW1000c
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az sql dw update", locals())

