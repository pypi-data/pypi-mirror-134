'''
Manage Azure Kusto clusters.
'''
from ... pyaz_utils import _call_az

def create(name, resource_group, sku, capacity=None, location=None, no_wait=None):
    '''
    Create a Kusto cluster.

    Required Parameters:
    - name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku -- The name of the sku.

    Optional Parameters:
    - capacity -- The instance number of the VM.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az kusto cluster create", locals())


def stop(name, resource_group, no_wait=None):
    '''
    Stop a Kusto cluster.

    Required Parameters:
    - name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az kusto cluster stop", locals())


def start(name, resource_group, no_wait=None):
    '''
    Start a Kusto cluster.

    Required Parameters:
    - name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az kusto cluster start", locals())


def list(resource_group):
    '''
    List a Kusto cluster.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az kusto cluster list", locals())


def show(name, resource_group):
    '''
    Get a Kusto cluster.

    Required Parameters:
    - name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az kusto cluster show", locals())


def delete(name, resource_group, yes=None):
    '''
    Delete a Kusto cluster.

    Required Parameters:
    - name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az kusto cluster delete", locals())


def update(name, resource_group, add=None, capacity=None, force_string=None, remove=None, set=None, sku=None):
    '''
    Update a Kusto cluster.

    Required Parameters:
    - name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - capacity -- The instance number of the VM.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sku -- The name of the sku.
    '''
    return _call_az("az kusto cluster update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Wait for a managed Kusto cluster to reach a desired state.

    Required Parameters:
    - name -- The name of the cluster.
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
    return _call_az("az kusto cluster wait", locals())

