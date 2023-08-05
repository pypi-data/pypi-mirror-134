'''
Manage Azure Kubernetes Services.
'''
from .. pyaz_utils import _call_az
from . import command, nodepool


def browse(name, resource_group, disable_browser=None, listen_address=None, listen_port=None):
    '''
    Show the dashboard for a Kubernetes cluster in a web browser.

    Required Parameters:
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - disable_browser -- None
    - listen_address -- None
    - listen_port -- None
    '''
    return _call_az("az aks browse", locals())


def create(name, resource_group, aad_admin_group_object_ids=None, aad_client_app_id=None, aad_server_app_id=None, aad_server_app_secret=None, aad_tenant_id=None, aci_subnet_name=None, admin_username=None, aks_custom_headers=None, api_server_authorized_ip_ranges=None, appgw_id=None, appgw_name=None, appgw_subnet_cidr=None, appgw_subnet_id=None, appgw_watch_namespace=None, assign_identity=None, assign_kubelet_identity=None, attach_acr=None, auto_upgrade_channel=None, client_secret=None, cluster_autoscaler_profile=None, disable_local_accounts=None, disable_public_fqdn=None, disable_rbac=None, dns_name_prefix=None, dns_service_ip=None, docker_bridge_address=None, edge_zone=None, enable_aad=None, enable_addons=None, enable_ahub=None, enable_azure_rbac=None, enable_cluster_autoscaler=None, enable_encryption_at_host=None, enable_managed_identity=None, enable_node_public_ip=None, enable_private_cluster=None, enable_rbac=None, enable_secret_rotation=None, enable_sgxquotehelper=None, enable_ultra_ssd=None, fqdn_subdomain=None, generate_ssh_keys=None, kubernetes_version=None, load_balancer_idle_timeout=None, load_balancer_managed_outbound_ip_count=None, load_balancer_outbound_ip_prefixes=None, load_balancer_outbound_ips=None, load_balancer_outbound_ports=None, load_balancer_sku=None, location=None, max_count=None, max_pods=None, min_count=None, network_plugin=None, network_policy=None, no_ssh_key=None, no_wait=None, node_count=None, node_osdisk_diskencryptionset_id=None, node_osdisk_size=None, node_osdisk_type=None, node_public_ip_prefix_id=None, node_vm_size=None, nodepool_labels=None, nodepool_name=None, nodepool_tags=None, os_sku=None, outbound_type=None, pod_cidr=None, ppg=None, private_dns_zone=None, rotation_poll_interval=None, service_cidr=None, service_principal=None, skip_subnet_role_assignment=None, ssh_key_value=None, tags=None, uptime_sla=None, vm_set_type=None, vnet_subnet_id=None, windows_admin_password=None, windows_admin_username=None, workspace_resource_id=None, yes=None, zones=None):
    '''
    Create a new managed Kubernetes cluster.

    Required Parameters:
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - aad_admin_group_object_ids -- None
    - aad_client_app_id -- None
    - aad_server_app_id -- None
    - aad_server_app_secret -- None
    - aad_tenant_id -- None
    - aci_subnet_name -- None
    - admin_username -- None
    - aks_custom_headers -- None
    - api_server_authorized_ip_ranges -- None
    - appgw_id -- None
    - appgw_name -- None
    - appgw_subnet_cidr -- None
    - appgw_subnet_id -- None
    - appgw_watch_namespace -- None
    - assign_identity -- None
    - assign_kubelet_identity -- None
    - attach_acr -- None
    - auto_upgrade_channel -- None
    - client_secret -- None
    - cluster_autoscaler_profile -- Space-separated list of key=value pairs for configuring cluster autoscaler. Pass an empty string to clear the profile.
    - disable_local_accounts -- None
    - disable_public_fqdn -- None
    - disable_rbac -- None
    - dns_name_prefix -- None
    - dns_service_ip -- None
    - docker_bridge_address -- None
    - edge_zone -- The name of edge zone.
    - enable_aad -- None
    - enable_addons -- None
    - enable_ahub -- None
    - enable_azure_rbac -- None
    - enable_cluster_autoscaler -- None
    - enable_encryption_at_host -- None
    - enable_managed_identity -- None
    - enable_node_public_ip -- None
    - enable_private_cluster -- None
    - enable_rbac -- None
    - enable_secret_rotation -- None
    - enable_sgxquotehelper -- None
    - enable_ultra_ssd -- None
    - fqdn_subdomain -- None
    - generate_ssh_keys -- None
    - kubernetes_version -- None
    - load_balancer_idle_timeout -- None
    - load_balancer_managed_outbound_ip_count -- None
    - load_balancer_outbound_ip_prefixes -- None
    - load_balancer_outbound_ips -- None
    - load_balancer_outbound_ports -- None
    - load_balancer_sku -- None
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - max_count -- None
    - max_pods -- None
    - min_count -- None
    - network_plugin -- None
    - network_policy -- None
    - no_ssh_key -- None
    - no_wait -- Do not wait for the long-running operation to finish.
    - node_count -- None
    - node_osdisk_diskencryptionset_id -- None
    - node_osdisk_size -- None
    - node_osdisk_type -- None
    - node_public_ip_prefix_id -- None
    - node_vm_size -- None
    - nodepool_labels -- space-separated labels: key[=value] [key[=value] ...]. See https://aka.ms/node-labels for syntax of labels.
    - nodepool_name -- Node pool name, up to 12 alphanumeric characters
    - nodepool_tags -- space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
    - os_sku -- None
    - outbound_type -- None
    - pod_cidr -- None
    - ppg -- None
    - private_dns_zone -- None
    - rotation_poll_interval -- None
    - service_cidr -- None
    - service_principal -- None
    - skip_subnet_role_assignment -- None
    - ssh_key_value -- None
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - uptime_sla -- None
    - vm_set_type -- None
    - vnet_subnet_id -- None
    - windows_admin_password -- None
    - windows_admin_username -- None
    - workspace_resource_id -- None
    - yes -- Do not prompt for confirmation.
    - zones -- Space-separated list of availability zones where agent nodes will be placed.
    '''
    return _call_az("az aks create", locals())


def update(name, resource_group, aad_admin_group_object_ids=None, aad_tenant_id=None, aks_custom_headers=None, api_server_authorized_ip_ranges=None, assign_identity=None, attach_acr=None, auto_upgrade_channel=None, cluster_autoscaler_profile=None, detach_acr=None, disable_ahub=None, disable_azure_rbac=None, disable_cluster_autoscaler=None, disable_local_accounts=None, disable_public_fqdn=None, disable_secret_rotation=None, enable_aad=None, enable_ahub=None, enable_azure_rbac=None, enable_cluster_autoscaler=None, enable_local_accounts=None, enable_managed_identity=None, enable_public_fqdn=None, enable_secret_rotation=None, load_balancer_idle_timeout=None, load_balancer_managed_outbound_ip_count=None, load_balancer_outbound_ip_prefixes=None, load_balancer_outbound_ips=None, load_balancer_outbound_ports=None, max_count=None, min_count=None, no_uptime_sla=None, no_wait=None, nodepool_labels=None, rotation_poll_interval=None, tags=None, update_cluster_autoscaler=None, uptime_sla=None, windows_admin_password=None, yes=None):
    '''
    Update a managed Kubernetes cluster.

    Required Parameters:
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - aad_admin_group_object_ids -- None
    - aad_tenant_id -- None
    - aks_custom_headers -- None
    - api_server_authorized_ip_ranges -- None
    - assign_identity -- None
    - attach_acr -- None
    - auto_upgrade_channel -- None
    - cluster_autoscaler_profile -- Space-separated list of key=value pairs for configuring cluster autoscaler. Pass an empty string to clear the profile.
    - detach_acr -- None
    - disable_ahub -- None
    - disable_azure_rbac -- None
    - disable_cluster_autoscaler -- None
    - disable_local_accounts -- None
    - disable_public_fqdn -- None
    - disable_secret_rotation -- None
    - enable_aad -- None
    - enable_ahub -- None
    - enable_azure_rbac -- None
    - enable_cluster_autoscaler -- None
    - enable_local_accounts -- None
    - enable_managed_identity -- None
    - enable_public_fqdn -- None
    - enable_secret_rotation -- None
    - load_balancer_idle_timeout -- None
    - load_balancer_managed_outbound_ip_count -- None
    - load_balancer_outbound_ip_prefixes -- None
    - load_balancer_outbound_ips -- None
    - load_balancer_outbound_ports -- None
    - max_count -- None
    - min_count -- None
    - no_uptime_sla -- None
    - no_wait -- Do not wait for the long-running operation to finish.
    - nodepool_labels -- space-separated labels: key[=value] [key[=value] ...]. See https://aka.ms/node-labels for syntax of labels.
    - rotation_poll_interval -- None
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - update_cluster_autoscaler -- None
    - uptime_sla -- None
    - windows_admin_password -- None
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az aks update", locals())


def delete(name, resource_group, no_wait=None, yes=None):
    '''
    Delete a managed Kubernetes cluster.

    Required Parameters:
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az aks delete", locals())


def update_credentials(name, resource_group, aad_client_app_id=None, aad_server_app_id=None, aad_server_app_secret=None, aad_tenant_id=None, client_secret=None, no_wait=None, reset_aad=None, reset_service_principal=None, service_principal=None):
    '''
    Update credentials for a managed Kubernetes cluster, like service principal.

    Required Parameters:
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - aad_client_app_id -- None
    - aad_server_app_id -- None
    - aad_server_app_secret -- None
    - aad_tenant_id -- None
    - client_secret -- None
    - no_wait -- Do not wait for the long-running operation to finish.
    - reset_aad -- None
    - reset_service_principal -- None
    - service_principal -- None
    '''
    return _call_az("az aks update-credentials", locals())


def disable_addons(addons, name, resource_group, no_wait=None):
    '''
    Disable Kubernetes addons.

    Required Parameters:
    - addons -- None
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az aks disable-addons", locals())


def enable_addons(addons, name, resource_group, appgw_id=None, appgw_name=None, appgw_subnet_cidr=None, appgw_subnet_id=None, appgw_watch_namespace=None, enable_secret_rotation=None, enable_sgxquotehelper=None, no_wait=None, rotation_poll_interval=None, subnet_name=None, workspace_resource_id=None):
    '''
    Enable Kubernetes addons.

    Required Parameters:
    - addons -- None
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - appgw_id -- None
    - appgw_name -- None
    - appgw_subnet_cidr -- None
    - appgw_subnet_id -- None
    - appgw_watch_namespace -- None
    - enable_secret_rotation -- None
    - enable_sgxquotehelper -- None
    - no_wait -- Do not wait for the long-running operation to finish.
    - rotation_poll_interval -- None
    - subnet_name -- Name of an existing subnet to use with the virtual-node add-on.
    - workspace_resource_id -- None
    '''
    return _call_az("az aks enable-addons", locals())


def get_credentials(name, resource_group, admin=None, context=None, file=None, overwrite_existing=None, public_fqdn=None):
    '''
    Get access credentials for a managed Kubernetes cluster.

    Required Parameters:
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - admin -- None
    - context -- If specified, overwrite the default context name.
    - file -- None
    - overwrite_existing -- None
    - public_fqdn -- None
    '''
    return _call_az("az aks get-credentials", locals())


def check_acr(acr, name, resource_group):
    '''
    Validate an ACR is accessible from an AKS cluster.

    Required Parameters:
    - acr -- None
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az aks check-acr", locals())


def get_upgrades(name, resource_group):
    '''
    Get the upgrade versions available for a managed Kubernetes cluster.

    Required Parameters:
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az aks get-upgrades", locals())


def install_cli(base_src_url=None, client_version=None, install_location=None, kubelogin_base_src_url=None, kubelogin_install_location=None, kubelogin_version=None):
    '''
    Download and install kubectl, the Kubernetes command-line tool. Download and install kubelogin, a client-go credential (exec) plugin implementing azure authentication.

    Optional Parameters:
    - base_src_url -- Base download source URL for kubectl releases.
    - client_version -- Version of kubectl to install.
    - install_location -- Path at which to install kubectl.
    - kubelogin_base_src_url -- Base download source URL for kubelogin releases.
    - kubelogin_install_location -- Path at which to install kubelogin.
    - kubelogin_version -- Version of kubelogin to install.
    '''
    return _call_az("az aks install-cli", locals())


def list(resource_group=None):
    '''
    List managed Kubernetes clusters.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az aks list", locals())


def remove_dev_spaces(name, resource_group, yes=None):
    '''
    Remove Azure Dev Spaces from a managed Kubernetes cluster.

    Required Parameters:
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation
    '''
    return _call_az("az aks remove-dev-spaces", locals())


def scale(name, node_count, resource_group, no_wait=None, nodepool_name=None):
    '''
    Scale the node pool in a managed Kubernetes cluster.

    Required Parameters:
    - name -- Name of the managed cluster.
    - node_count -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - nodepool_name -- Node pool name, up to 12 alphanumeric characters
    '''
    return _call_az("az aks scale", locals())


def show(name, resource_group):
    '''
    Show the details for a managed Kubernetes cluster.

    Required Parameters:
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az aks show", locals())


def upgrade(name, resource_group, control_plane_only=None, kubernetes_version=None, no_wait=None, node_image_only=None, yes=None):
    '''
    Upgrade a managed Kubernetes cluster to a newer version.

    Required Parameters:
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - control_plane_only -- None
    - kubernetes_version -- None
    - no_wait -- Do not wait for the long-running operation to finish.
    - node_image_only -- None
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az aks upgrade", locals())


def use_dev_spaces(name, resource_group, endpoint=None, space=None, update=None, yes=None):
    '''
    Use Azure Dev Spaces with a managed Kubernetes cluster.

    Required Parameters:
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - endpoint -- The endpoint type to be used for a Azure Dev Spaces controller.     See https://aka.ms/azds-networking for more information.
    - space -- Name of the new or existing dev space to select. Defaults to an     interactive selection experience.
    - update -- Update to the latest Azure Dev Spaces client components.
    - yes -- Do not prompt for confirmation. Requires --space.
    '''
    return _call_az("az aks use-dev-spaces", locals())


def rotate_certs(name, resource_group, no_wait=None, yes=None):
    '''
    Rotate certificates and keys on a managed Kubernetes cluster

    Required Parameters:
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az aks rotate-certs", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Wait for a managed Kubernetes cluster to reach a desired state.

    Required Parameters:
    - name -- Name of the managed cluster.
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
    return _call_az("az aks wait", locals())


def stop(name, resource_group, no_wait=None):
    '''
    

    Required Parameters:
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az aks stop", locals())


def start(name, resource_group, no_wait=None):
    '''
    

    Required Parameters:
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az aks start", locals())


def get_versions(location):
    '''
    Get the versions available for creating a managed Kubernetes cluster.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az aks get-versions", locals())

