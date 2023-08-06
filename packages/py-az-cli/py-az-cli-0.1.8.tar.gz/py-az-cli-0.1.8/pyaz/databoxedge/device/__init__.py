'''
Manage device with databoxedge
'''
from ... pyaz_utils import _call_az

def list(expand=None, resource_group=None):
    '''
    Get all the Data Box Edge/Data Box Gateway devices in a resource group or in a subscription.

    Optional Parameters:
    - expand -- Specify $expand=details to populate additional fields related to the resource or Specify $skipToken=<token> to populate the next page in the list.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az databoxedge device list", locals())


def show(name, resource_group):
    '''
    Get the properties of the Data Box Edge/Data Box Gateway device.

    Required Parameters:
    - name -- The device name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az databoxedge device show", locals())


def create(name, resource_group, description=None, etag=None, friendly_name=None, location=None, model_description=None, no_wait=None, sku=None, status=None, tags=None):
    '''
    Create a Data Box Edge/Data Box Gateway resource.

    Required Parameters:
    - name -- The device name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - description -- The Description of the Data Box Edge/Gateway device.
    - etag -- The etag for the devices.
    - friendly_name -- The Data Box Edge/Gateway device name.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - model_description -- The description of the Data Box Edge/Gateway device model.
    - no_wait -- Do not wait for the long-running operation to finish.
    - sku -- The SKU type.
    - status -- The status of the Data Box Edge/Gateway device.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az databoxedge device create", locals())


def update(name, resource_group, tags=None):
    '''
    Modify a Data Box Edge/Data Box Gateway resource.

    Required Parameters:
    - name -- The device name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az databoxedge device update", locals())


def delete(name, resource_group, no_wait=None, yes=None):
    '''
    Delete the Data Box Edge/Data Box Gateway device.

    Required Parameters:
    - name -- The device name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az databoxedge device delete", locals())


def download_update(name, resource_group, no_wait=None):
    '''
    Download the updates on a Data Box Edge/Data Box Gateway device.

    Required Parameters:
    - name -- The device name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az databoxedge device download-update", locals())


def install_update(name, resource_group, no_wait=None):
    '''
    Install the updates on the Data Box Edge/Data Box Gateway device.

    Required Parameters:
    - name -- The device name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az databoxedge device install-update", locals())


def scan_for_update(name, resource_group, no_wait=None):
    '''
    Scan for updates on a Data Box Edge/Data Box Gateway device.

    Required Parameters:
    - name -- The device name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az databoxedge device scan-for-update", locals())


def show_update_summary(name, resource_group):
    '''
    Get information about the availability of updates based on the last scan of the device. It also gets information about any ongoing download or install jobs on the device.

    Required Parameters:
    - name -- The device name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az databoxedge device show-update-summary", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the databoxedge device is met.

    Required Parameters:
    - name -- The device name.
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
    return _call_az("az databoxedge device wait", locals())

