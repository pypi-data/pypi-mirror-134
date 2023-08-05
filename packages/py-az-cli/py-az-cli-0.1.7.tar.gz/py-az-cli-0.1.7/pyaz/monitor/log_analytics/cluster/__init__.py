from .... pyaz_utils import _call_az

def create(name, resource_group, sku_capacity, identity_type=None, location=None, no_wait=None, sku_name=None, tags=None):
    '''
    Create a cluster instance.

    Required Parameters:
    - name -- The name of the Log Analytics cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku_capacity -- The capacity of the SKU. It must be in the range of 1000-2000 per day and must be in multiples of 100. If you want to increase the limit, please contact LAIngestionRate@microsoft.com. It can be decreased only after 31 days.

    Optional Parameters:
    - identity_type -- The identity type. Supported values: SystemAssigned
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - sku_name -- The name of the SKU. Currently only support 'CapacityReservation'
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az monitor log-analytics cluster create", locals())


def update(name, resource_group, key_name=None, key_vault_uri=None, key_version=None, sku_capacity=None, tags=None):
    '''
    Update a cluster instance.

    Required Parameters:
    - name -- The name of the Log Analytics cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - key_name -- The name of the key associated with the Log Analytics cluster.
    - key_vault_uri -- The Key Vault uri which holds the key associated with the Log Analytics cluster.
    - key_version -- The version of the key associated with the Log Analytics cluster.
    - sku_capacity -- The capacity of the SKU. It must be in the range of 1000-2000 per day and must be in multiples of 100. If you want to increase the limit, please contact LAIngestionRate@microsoft.com. It can be decreased only after 31 days.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az monitor log-analytics cluster update", locals())


def show(name, resource_group):
    '''
    Show the properties of a cluster instance.

    Required Parameters:
    - name -- The name of the Log Analytics cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor log-analytics cluster show", locals())


def delete(name, resource_group, no_wait=None, yes=None):
    '''
    Delete a cluster instance.

    Required Parameters:
    - name -- The name of the Log Analytics cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az monitor log-analytics cluster delete", locals())


def list(resource_group=None):
    '''
    Gets all cluster instances in a resource group or in current subscription.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor log-analytics cluster list", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the cluster is met.

    Required Parameters:
    - name -- The name of the Log Analytics cluster.
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
    return _call_az("az monitor log-analytics cluster wait", locals())

