'''
Manage Azure Data Migration Service (DMS) instances.
'''
from .. pyaz_utils import _call_az
from . import project


def check_name(location, name):
    '''
    Check if a given DMS instance name is available in a given region as well as the name's validity.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the Service.
    '''
    return _call_az("az dms check-name", locals())


def check_status(name, resource_group):
    '''
    Perform a health check and return the status of the service and virtual machine size.

    Required Parameters:
    - name -- The name of the Service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az dms check-status", locals())


def create(location, name, resource_group, sku_name, subnet, no_wait=None, tags=None):
    '''
    Create an instance of the Data Migration Service.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the Service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku_name -- None
    - subnet -- None

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - tags -- A space-delimited list of tags in "tag1[=value1]" format.
    '''
    return _call_az("az dms create", locals())


def delete(name, resource_group, delete_running_tasks=None, no_wait=None, yes=None):
    '''
    Delete an instance of the Data Migration Service.

    Required Parameters:
    - name -- The name of the Service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - delete_running_tasks -- None
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az dms delete", locals())


def list(resource_group=None):
    '''
    List the DMS instances within your currently configured subscription (to set this use "az account set"). If provided, only show the instances within a given resource group.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az dms list", locals())


def show(name, resource_group):
    '''
    Show the details for an instance of the Data Migration Service.

    Required Parameters:
    - name -- The name of the Service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az dms show", locals())


def start(name, resource_group, no_wait=None):
    '''
    Start an instance of the Data Migration Service. It can then be used to run data migrations.

    Required Parameters:
    - name -- The name of the Service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az dms start", locals())


def stop(name, resource_group, no_wait=None):
    '''
    Stop an instance of the Data Migration Service. While stopped, it can't be used to run data migrations and the owner won't be billed.

    Required Parameters:
    - name -- The name of the Service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az dms stop", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the DMS instance is met.

    Required Parameters:
    - name -- The name of the Service.
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
    return _call_az("az dms wait", locals())


def list_skus():
    '''
    List the SKUs that are supported by the Data Migration Service.
    '''
    return _call_az("az dms list-skus", locals())

