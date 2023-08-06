'''
Manage app service plans.
'''
from ... pyaz_utils import _call_az

def create(name, resource_group, app_service_environment=None, hyper_v=None, is_linux=None, location=None, no_wait=None, number_of_workers=None, per_site_scaling=None, sku=None, tags=None, zone_redundant=None):
    '''
    Create an app service plan.

    Required Parameters:
    - name -- Name of the new app service plan
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - app_service_environment -- Name or ID of the app service environment
    - hyper_v -- Host web app on Windows container
    - is_linux -- host web app on Linux worker
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - number_of_workers -- Number of workers to be allocated.
    - per_site_scaling -- Enable per-app scaling at the App Service plan level to allow for scaling an app independently from the App Service plan that hosts it.
    - sku -- The pricing tiers, e.g., F1(Free), D1(Shared), B1(Basic Small), B2(Basic Medium), B3(Basic Large), S1(Standard Small), P1V2(Premium V2 Small), P1V3(Premium V3 Small), P2V3(Premium V3 Medium), P3V3(Premium V3 Large), PC2 (Premium Container Small), PC3 (Premium Container Medium), PC4 (Premium Container Large), I1 (Isolated Small), I2 (Isolated Medium), I3 (Isolated Large), I1v2 (Isolated V2 Small), I2v2 (Isolated V2 Medium), I3v2 (Isolated V2 Large)
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - zone_redundant -- Enable zone redundancy for high availability. Cannot be changed after plan creation. Minimum instance count is 3.
    '''
    return _call_az("az appservice plan create", locals())


def delete(name, resource_group, yes=None):
    '''
    Delete an app service plan.

    Required Parameters:
    - name -- The name of the app service plan
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az appservice plan delete", locals())


def list(resource_group=None):
    '''
    List app service plans.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az appservice plan list", locals())


def show(name, resource_group):
    '''
    Get the app service plans for a resource group or a set of resource groups.

    Required Parameters:
    - name -- The name of the app service plan
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az appservice plan show", locals())


def update(name, resource_group, add=None, force_string=None, no_wait=None, number_of_workers=None, remove=None, set=None, sku=None):
    '''
    Update an app service plan.

    Required Parameters:
    - name -- The name of the app service plan
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - no_wait -- Do not wait for the long-running operation to finish.
    - number_of_workers -- Number of workers to be allocated.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sku -- The pricing tiers, e.g., F1(Free), D1(Shared), B1(Basic Small), B2(Basic Medium), B3(Basic Large), S1(Standard Small), P1V2(Premium V2 Small), P1V3(Premium V3 Small), P2V3(Premium V3 Medium), P3V3(Premium V3 Large), PC2 (Premium Container Small), PC3 (Premium Container Medium), PC4 (Premium Container Large), I1 (Isolated Small), I2 (Isolated Medium), I3 (Isolated Large), I1v2 (Isolated V2 Small), I2v2 (Isolated V2 Medium), I3v2 (Isolated V2 Large)
    '''
    return _call_az("az appservice plan update", locals())

