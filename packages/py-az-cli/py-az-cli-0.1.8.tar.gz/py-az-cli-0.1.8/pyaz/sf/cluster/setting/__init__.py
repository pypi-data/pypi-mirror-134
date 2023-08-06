'''
Manage a cluster's settings.
'''
from .... pyaz_utils import _call_az

def set(cluster_name, resource_group, parameter=None, section=None, settings_section_description=None, value=None):
    '''
    Update the settings of a cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - parameter -- parameter name
    - section -- section name
    - settings_section_description -- JSON encoded parameters configuration. Use @{file} to load from a file. For example: [{"section": "NamingService","parameter": "MaxOperationTimeout","value": 1000},{"section": "MaxFileOperationTimeout","parameter": "Max2","value": 1000]
    - value -- Specify the value
    '''
    return _call_az("az sf cluster setting set", locals())


def remove(cluster_name, resource_group, parameter=None, section=None, settings_section_description=None):
    '''
    Remove settings from a cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - parameter -- parameter name
    - section -- section name
    - settings_section_description -- JSON encoded parameters configuration. Use @{file} to load from a file. For example: [{"section": "NamingService","parameter": "MaxOperationTimeout"}]
    '''
    return _call_az("az sf cluster setting remove", locals())

