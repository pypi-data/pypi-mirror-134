'''
Support data box edge device and management
'''
from .. pyaz_utils import _call_az
from . import alert, bandwidth_schedule, device, order


def show_job(device_name, name, resource_group):
    '''
    Get the details of a specified job on a Data Box Edge/Data Box Gateway device.

    Required Parameters:
    - device_name -- The device name.
    - name -- The job name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az databoxedge show-job", locals())


def list_node(device_name, resource_group):
    '''
    Get all the nodes currently configured under this Data Box Edge device.

    Required Parameters:
    - device_name -- The device name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az databoxedge list-node", locals())


def list_sku(filter=None):
    '''
    List all the available Skus in the region and information related to them.

    Optional Parameters:
    - filter -- Specify $filter='location eq <location>' to filter on location.
    '''
    return _call_az("az databoxedge list-sku", locals())

