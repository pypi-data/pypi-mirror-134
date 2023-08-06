'''
Manage App Service Plans for an Azure Function
'''
from ... pyaz_utils import _call_az

def create(name, resource_group, sku, is_linux=None, location=None, max_burst=None, number_of_workers=None, tags=None, zone_redundant=None):
    '''
    Create an App Service Plan for an Azure Function.

    Required Parameters:
    - name -- The name of the app service plan
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku -- The SKU of the app service plan. e.g., F1(Free), D1(Shared), B1(Basic Small), B2(Basic Medium), B3(Basic Large), S1(Standard Small), P1V2(Premium V2 Small), PC2 (Premium Container Small), PC3 (Premium Container Medium), PC4 (Premium Container Large), I1 (Isolated Small), I2 (Isolated Medium), I3 (Isolated Large), K1 (Kubernetes).

    Optional Parameters:
    - is_linux -- host function app on Linux worker
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - max_burst -- The maximum number of elastic workers for the plan.
    - number_of_workers -- The number of workers for the app service plan.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - zone_redundant -- Enable zone redundancy for high availability. Cannot be changed after plan creation. Minimum instance count is 3.
    '''
    return _call_az("az functionapp plan create", locals())


def update(name, resource_group, add=None, force_string=None, max_burst=None, number_of_workers=None, remove=None, set=None, sku=None):
    '''
    Update an App Service plan for an Azure Function.

    Required Parameters:
    - name -- The name of the app service plan
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - max_burst -- The maximum number of elastic workers for the plan.
    - number_of_workers -- The number of workers for the app service plan.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sku -- The SKU of the app service plan.
    '''
    return _call_az("az functionapp plan update", locals())


def delete(name, resource_group, yes=None):
    '''
    Delete an App Service Plan.

    Required Parameters:
    - name -- The name of the app service plan
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az functionapp plan delete", locals())


def list(resource_group=None):
    '''
    List App Service Plans.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az functionapp plan list", locals())


def show(name, resource_group):
    '''
    Get the App Service Plans for a resource group or a set of resource groups.

    Required Parameters:
    - name -- The name of the app service plan
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az functionapp plan show", locals())

