'''
Manage Azure EventHubs Cluster for namespace
'''
from .... pyaz_utils import _call_az

def list(name, resource_group):
    '''
    List of Namespaces within given Cluster.

    Required Parameters:
    - name -- Name of Cluster
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs cluster namespace list", locals())

