'''
Manage Azure Red Hat OpenShift 3.11 clusters.
'''
from .. pyaz_utils import _call_az
from . import monitor


def create(name, resource_group, aad_client_app_id=None, aad_client_app_secret=None, aad_tenant_id=None, compute_count=None, compute_vm_size=None, customer_admin_group_id=None, location=None, no_wait=None, subnet_prefix=None, tags=None, vnet_peer=None, vnet_prefix=None, workspace_id=None):
    '''
    Create a new Azure Red Hat OpenShift 3.11 cluster.

    Required Parameters:
    - name -- Name of the managed OpenShift cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - aad_client_app_id -- None
    - aad_client_app_secret -- None
    - aad_tenant_id -- None
    - compute_count -- None
    - compute_vm_size -- None
    - customer_admin_group_id -- None
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - subnet_prefix -- None
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vnet_peer -- None
    - vnet_prefix -- None
    - workspace_id -- None
    '''
    return _call_az("az openshift create", locals())


def delete(name, resource_group, no_wait=None, yes=None):
    '''
    Delete an Azure Red Hat OpenShift 3.11 cluster.

    Required Parameters:
    - name -- Name of the managed OpenShift cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az openshift delete", locals())


def scale(compute_count, name, resource_group, no_wait=None):
    '''
    Scale the compute pool in an Azure Red Hat OpenShift 3.11 cluster.

    Required Parameters:
    - compute_count -- None
    - name -- Name of the managed OpenShift cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az openshift scale", locals())


def show(name, resource_group):
    '''
    Show the details for an Azure Red Hat OpenShift 3.11 cluster.

    Required Parameters:
    - name -- Name of the managed OpenShift cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az openshift show", locals())


def list(resource_group=None):
    '''
    List Azure Red Hat OpenShift 3.11 clusters.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az openshift list", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Wait for an Azure Red Hat OpenShift 3.11 cluster to reach a desired state.

    Required Parameters:
    - name -- Name of the managed OpenShift cluster.
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
    return _call_az("az openshift wait", locals())

