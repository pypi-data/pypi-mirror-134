'''
Manage Azure API Management services.
'''
from .. pyaz_utils import _call_az
from . import api, nv, product


def create(name, publisher_email, publisher_name, resource_group, enable_client_certificate=None, enable_managed_identity=None, location=None, no_wait=None, sku_capacity=None, sku_name=None, tags=None, virtual_network=None):
    '''
    Create an API Management service instance.

    Required Parameters:
    - name -- The name of the api management service instance
    - publisher_email -- The e-mail address to receive all system notifications.
    - publisher_name -- The name of your organization for use in the developer portal and e-mail notifications.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - enable_client_certificate -- Enforces a client certificate to be presented on each request to the gateway and also enables the ability to authenticate the certificate in the policy on the gateway.
    - enable_managed_identity -- Create a managed identity for the API Management service to access other Azure resources.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - sku_capacity -- The number of deployed units of the SKU.
    - sku_name -- The sku of the api management instance
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - virtual_network -- The virtual network type.
    '''
    return _call_az("az apim create", locals())


def show(name, resource_group):
    '''
    Show details of an API Management service instance.

    Required Parameters:
    - name -- The name of the api management service instance
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az apim show", locals())


def list(resource_group=None):
    '''
    List API Management service instances.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az apim list", locals())


def delete(name, resource_group, no_wait=None, yes=None):
    '''
    Deletes an API Management service.

    Required Parameters:
    - name -- The name of the api management service instance
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az apim delete", locals())


def update(name, resource_group, add=None, enable_client_certificate=None, enable_managed_identity=None, force_string=None, no_wait=None, publisher_email=None, publisher_name=None, remove=None, set=None, sku_capacity=None, sku_name=None, tags=None, virtual_network=None):
    '''
    Update an API Management service instance.

    Required Parameters:
    - name -- The name of the api management service instance
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - enable_client_certificate -- Enforces a client certificate to be presented on each request to the gateway and also enables the ability to authenticate the certificate in the policy on the gateway.
    - enable_managed_identity -- Create a managed identity for the API Management service to access other Azure resources.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - no_wait -- Do not wait for the long-running operation to finish.
    - publisher_email -- The e-mail address to receive all system notifications.
    - publisher_name -- The name of your organization for use in the developer portal and e-mail notifications.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sku_capacity -- The number of deployed units of the SKU.
    - sku_name -- The sku of the api management instance
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - virtual_network -- The virtual network type.
    '''
    return _call_az("az apim update", locals())


def check_name(name):
    '''
    

    Required Parameters:
    - name -- The name of the api management service instance
    '''
    return _call_az("az apim check-name", locals())


def backup(backup_name, name, resource_group, storage_account_container, storage_account_key, storage_account_name, no_wait=None):
    '''
    Creates a backup of the API Management service to the given Azure Storage Account. This is long running operation and could take several minutes to complete.

    Required Parameters:
    - backup_name -- The name of the backup file to create.
    - name -- The name of the api management service instance
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - storage_account_container -- The name of the storage account container used to place the backup.
    - storage_account_key -- The access key of the storage account used to place the backup.
    - storage_account_name -- The name of the storage account used to place the backup.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az apim backup", locals())


def restore(backup_name, name, resource_group, storage_account_container, storage_account_key, storage_account_name, no_wait=None):
    '''
    Restores a backup of an API Management service created using the ApiManagementService_Backup operation on the current service. This is a long running operation and could take several minutes to complete.

    Required Parameters:
    - backup_name -- The name of the backup file to restore.
    - name -- The name of the api management service instance
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - storage_account_container -- The name of the storage account container used to retrieve the backup from.
    - storage_account_key -- The access key of the storage account used to retrieve the backup from.
    - storage_account_name -- The name of the storage account used to retrieve the backup from.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az apim restore", locals())


def apply_network_updates(name, resource_group, location=None, no_wait=None):
    '''
    

    Required Parameters:
    - name -- The name of the api management service instance
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az apim apply-network-updates", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of an apim is met.

    Required Parameters:
    - name -- The name of the api management service instance
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az apim wait", locals())

