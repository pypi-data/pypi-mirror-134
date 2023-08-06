'''
View all Adaptive Network Hardening resources
'''
from ... pyaz_utils import _call_az

def show(adaptive_network_hardenings_resource_name, resource_group, resource_name, resource_namespace, resource_type):
    '''
    Gets a single Adaptive Network Hardening resource.

    Required Parameters:
    - adaptive_network_hardenings_resource_name -- Adaptive Network Hardening resource name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_name -- Name of the resource
    - resource_namespace -- The Namespace of the resource
    - resource_type -- The type of the resource
    '''
    return _call_az("az security adaptive_network_hardenings show", locals())


def list(resource_group, resource_name, resource_namespace, resource_type):
    '''
    Gets a list of Adaptive Network Hardenings resources in scope of an extended resource.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_name -- Name of the resource
    - resource_namespace -- The Namespace of the resource
    - resource_type -- The type of the resource
    '''
    return _call_az("az security adaptive_network_hardenings list", locals())

