'''
Manage HDInsight applications.
'''
from ... pyaz_utils import _call_az

def create(cluster_name, name, resource_group, script_action_name, script_uri, access_mode=None, destination_port=None, disable_gateway_auth=None, edgenode_size=None, marketplace_id=None, no_validation_timeout=None, script_parameters=None, ssh_password=None, ssh_public_key=None, ssh_user=None, sub_domain_suffix=None, subnet=None, tags=None, type=None, vnet_name=None):
    '''
    Create an application for a HDInsight cluster.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - name -- The constant value for the application name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - script_action_name -- The name of the script action.
    - script_uri -- The URI to the script.

    Optional Parameters:
    - access_mode -- The access mode for the application.
    - destination_port -- The destination port to connect to.
    - disable_gateway_auth -- Indicates whether to disable gateway authentication. Default is to enable gateway authentication. Default: false. 
    - edgenode_size -- The size of the node. See also: https://docs.microsoft.com/azure/hdinsight/hdinsight-hadoop-provision-linux-clusters#configure-cluster-size
    - marketplace_id -- The marketplace identifier.
    - no_validation_timeout -- Permit timeout error during argument validation phase. If omitted, validation timeout error will be permitted.
    - script_parameters -- The parameters for the script.
    - ssh_password -- SSH password for the cluster nodes.
    - ssh_public_key -- SSH public key for the cluster nodes.
    - ssh_user -- SSH username for the cluster nodes.
    - sub_domain_suffix -- The subdomain suffix of the application.
    - subnet -- The name or ID of subnet. If name is supplied, `--vnet-name` must be supplied.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - type -- The application type.
    - vnet_name -- The name of a virtual network.
    '''
    return _call_az("az hdinsight application create", locals())


def show(cluster_name, name, resource_group):
    '''
    

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - name -- The constant value for the application name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az hdinsight application show", locals())


def list(cluster_name, resource_group):
    '''
    

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az hdinsight application list", locals())


def wait(cluster_name, name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until an operation is complete.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - name -- The constant value for the application name.
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
    return _call_az("az hdinsight application wait", locals())


def delete(cluster_name, name, resource_group, no_wait=None, yes=None):
    '''
    

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - name -- The constant value for the application name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az hdinsight application delete", locals())

