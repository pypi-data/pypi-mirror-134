'''
Manage Azure Red Hat OpenShift clusters.
'''
from .. pyaz_utils import _call_az

def create(master_subnet, name, resource_group, worker_subnet, apiserver_visibility=None, client_id=None, client_secret=None, cluster_resource_group=None, domain=None, ingress_visibility=None, location=None, master_vm_size=None, no_wait=None, pod_cidr=None, pull_secret=None, service_cidr=None, tags=None, vnet=None, vnet_resource_group=None, worker_count=None, worker_vm_disk_size_gb=None, worker_vm_size=None):
    '''
    Create a cluster.

    Required Parameters:
    - master_subnet -- Name or ID of master vnet subnet.  If name is supplied, `--vnet` must be supplied.
    - name -- Name of cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - worker_subnet -- Name or ID of worker vnet subnet.  If name is supplied, `--vnet` must be supplied.

    Optional Parameters:
    - apiserver_visibility -- API server visibility.
    - client_id -- Client ID of cluster service principal.
    - client_secret -- Client secret of cluster service principal.
    - cluster_resource_group -- Resource group of cluster.
    - domain -- Domain of cluster.
    - ingress_visibility -- Ingress visibility.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - master_vm_size -- Size of master VMs.
    - no_wait -- Do not wait for the long-running operation to finish.
    - pod_cidr -- CIDR of pod network. Must be a minimum of /18 or larger.
    - pull_secret -- Pull secret of cluster.
    - service_cidr -- CIDR of service network. Must be a minimum of /18 or larger
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vnet -- Name or ID of vnet.  If name is supplied, `--vnet-resource-group` must be supplied.
    - vnet_resource_group -- Name of vnet resource group.
    - worker_count -- Count of worker VMs.
    - worker_vm_disk_size_gb -- Disk size in GB of worker VMs.
    - worker_vm_size -- Size of worker VMs.
    '''
    return _call_az("az aro create", locals())


def delete(name, resource_group, no_wait=None, yes=None):
    '''
    Delete a cluster.

    Required Parameters:
    - name -- Name of cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az aro delete", locals())


def list(resource_group=None):
    '''
    List clusters.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az aro list", locals())


def show(name, resource_group):
    '''
    Get the details of a cluster.

    Required Parameters:
    - name -- Name of cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az aro show", locals())


def update(name, resource_group, client_id=None, client_secret=None, no_wait=None, refresh_credentials=None):
    '''
    Update a cluster.

    Required Parameters:
    - name -- Name of cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - client_id -- Client ID of cluster service principal.
    - client_secret -- Client secret of cluster service principal.
    - no_wait -- Do not wait for the long-running operation to finish.
    - refresh_credentials -- Refresh cluster application credentials.
    '''
    return _call_az("az aro update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Wait for a cluster to reach a desired state.

    Required Parameters:
    - name -- Name of cluster.
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
    return _call_az("az aro wait", locals())


def list_credentials(name, resource_group):
    '''
    List credentials of a cluster.

    Required Parameters:
    - name -- Name of cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az aro list-credentials", locals())

