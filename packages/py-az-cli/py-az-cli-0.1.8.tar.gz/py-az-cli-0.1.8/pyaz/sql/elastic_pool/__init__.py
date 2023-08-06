from ... pyaz_utils import _call_az
from . import op


def create(name, resource_group, server, capacity=None, db_dtu_max=None, db_dtu_min=None, family=None, license_type=None, maint_config_id=None, max_size=None, no_wait=None, tags=None, tier=None, zone_redundant=None):
    '''
    Create an elastic pool.

    Required Parameters:
    - name -- The name of the elastic pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - capacity -- The capacity component of the sku in integer number of DTUs or vcores.
    - db_dtu_max -- The maximum capacity (in DTUs or vcores) any one database can consume.
    - db_dtu_min -- The minumum capacity (in DTUs or vcores) each database is guaranteed.
    - family -- The compute generation component of the sku (for vcore skus only). Allowed values include: Gen4, Gen5.
    - license_type -- The license type to apply for this elastic pool. Possible values include: "LicenseIncluded", "BasePrice".
    - maint_config_id -- Specified maintenance configuration id or name for this resource.
    - max_size -- The max storage size. If no unit is specified, defaults to bytes (B).
    - no_wait -- Do not wait for the long-running operation to finish.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tier -- The edition component of the sku. Allowed values include: Basic, Standard, Premium, GeneralPurpose, BusinessCritical.
    - zone_redundant -- Specifies whether to enable zone redundancy
    '''
    return _call_az("az sql elastic-pool create", locals())


def delete(name, resource_group, server, no_wait=None):
    '''
    

    Required Parameters:
    - name -- The name of the elastic pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az sql elastic-pool delete", locals())


def show(name, resource_group, server):
    '''
    

    Required Parameters:
    - name -- The name of the elastic pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql elastic-pool show", locals())


def list(resource_group, server, skip=None):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - skip -- The number of elements in the collection to skip.
    '''
    return _call_az("az sql elastic-pool list", locals())


def update(name, resource_group, server, add=None, capacity=None, db_dtu_max=None, db_dtu_min=None, family=None, force_string=None, maint_config_id=None, max_size=None, no_wait=None, remove=None, set=None, tier=None, zone_redundant=None):
    '''
    Update an elastic pool.

    Required Parameters:
    - name -- The name of the elastic pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - capacity -- The capacity component of the sku in integer number of DTUs or vcores.
    - db_dtu_max -- The maximum capacity (in DTUs or vcores) any one database can consume.
    - db_dtu_min -- The minumum capacity (in DTUs or vcores) each database is guaranteed.
    - family -- The compute generation component of the sku (for vcore skus only). Allowed values include: Gen4, Gen5.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - maint_config_id -- Specified maintenance configuration id or name for this resource.
    - max_size -- The max storage size. If no unit is specified, defaults to bytes (B).
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tier -- The edition component of the sku. Allowed values include: Basic, Standard, Premium, GeneralPurpose, BusinessCritical.
    - zone_redundant -- Specifies whether to enable zone redundancy
    '''
    return _call_az("az sql elastic-pool update", locals())


def list_dbs(name, resource_group, server):
    '''
    

    Required Parameters:
    - name -- The name of the elastic pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql elastic-pool list-dbs", locals())


def list_editions(location, available=None, dtu=None, show_details=None, tier=None, vcores=None):
    '''
    List elastic pool editions available for the active subscription.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.

    Optional Parameters:
    - available -- If specified, show only results that are available in the specified region.
    - dtu -- Number of DTUs to search for. If unspecified, all DTU sizes are shown.
    - show_details -- List of additional details to include in output.
    - tier -- Edition to search for. If unspecified, all editions are shown.
    - vcores -- Number of vcores to search for. If unspecified, all vcore sizes are shown.
    '''
    return _call_az("az sql elastic-pool list-editions", locals())

