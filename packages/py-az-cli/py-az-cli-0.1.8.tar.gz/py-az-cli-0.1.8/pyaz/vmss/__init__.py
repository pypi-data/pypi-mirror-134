'''
Manage groupings of virtual machines in an Azure Virtual Machine Scale Set (VMSS).
'''
from .. pyaz_utils import _call_az
from . import application, diagnostics, disk, encryption, extension, identity, nic, rolling_upgrade, run_command


def create(name, resource_group, accelerated_networking=None, admin_password=None, admin_username=None, app_gateway=None, app_gateway_capacity=None, app_gateway_sku=None, app_gateway_subnet_address_prefix=None, asgs=None, assign_identity=None, authentication_type=None, automatic_repairs_grace_period=None, backend_pool_name=None, backend_port=None, capacity_reservation_group=None, computer_name_prefix=None, custom_data=None, data_disk_caching=None, data_disk_encryption_sets=None, data_disk_iops=None, data_disk_mbps=None, data_disk_sizes_gb=None, disable_overprovision=None, dns_servers=None, edge_zone=None, enable_agent=None, enable_auto_update=None, enable_cross_zone_upgrade=None, enable_spot_restore=None, encryption_at_host=None, ephemeral_os_disk=None, ephemeral_os_disk_placement=None, eviction_policy=None, generate_ssh_keys=None, health_probe=None, host_group=None, image=None, instance_count=None, lb_nat_pool_name=None, lb_sku=None, license_type=None, load_balancer=None, location=None, max_batch_instance_percent=None, max_price=None, max_unhealthy_instance_percent=None, max_unhealthy_upgraded_instance_percent=None, network_api_version=None, no_wait=None, nsg=None, orchestration_mode=None, os_disk_caching=None, os_disk_encryption_set=None, os_disk_name=None, os_disk_size_gb=None, os_type=None, patch_mode=None, pause_time_between_batches=None, plan_name=None, plan_product=None, plan_promotion_code=None, plan_publisher=None, platform_fault_domain_count=None, ppg=None, prioritize_unhealthy_instances=None, priority=None, public_ip_address=None, public_ip_address_allocation=None, public_ip_address_dns_name=None, public_ip_per_vm=None, role=None, scale_in_policy=None, scope=None, secrets=None, single_placement_group=None, specialized=None, spot_restore_timeout=None, ssh_dest_key_path=None, ssh_key_values=None, storage_container_name=None, storage_sku=None, subnet=None, subnet_address_prefix=None, tags=None, terminate_notification_time=None, ultra_ssd_enabled=None, upgrade_policy_mode=None, use_unmanaged_disk=None, user_data=None, validate=None, vm_domain_name=None, vm_sku=None, vnet_address_prefix=None, vnet_name=None, zones=None):
    '''
    Create an Azure Virtual Machine Scale Set.

    Required Parameters:
    - name -- Name of the virtual machine scale set.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - accelerated_networking -- enable accelerated networking. Unless specified, CLI will enable it based on machine image and size
    - admin_password -- Password for the VM if authentication type is 'Password'.
    - admin_username -- Username for the VM. Default value is current username of OS. If the default value is system reserved, then default value will be set to azureuser. Please refer to https://docs.microsoft.com/rest/api/compute/virtualmachines/createorupdate#osprofile to get a full list of reserved values.
    - app_gateway -- Name to use when creating a new application gateway (default) or referencing an existing one. Can also reference an existing application gateway by ID or specify "" for none.
    - app_gateway_capacity -- The number of instances to use when creating a new application gateway.
    - app_gateway_sku -- SKU when creating a new application gateway.
    - app_gateway_subnet_address_prefix -- The subnet IP address prefix to use when creating a new application gateway in CIDR format.
    - asgs -- Space-separated list of existing application security groups to associate with the VM.
    - assign_identity -- accept system or user assigned identities separated by spaces. Use '[system]' to refer system assigned identity, or a resource id to refer user assigned identity. Check out help for more examples
    - authentication_type -- Type of authentication to use with the VM. Defaults to password for Windows and SSH public key for Linux. "all" enables both ssh and password authentication. 
    - automatic_repairs_grace_period -- The amount of time (in minutes, between 30 and 90) for which automatic repairs are suspended due to a state change on VM.
    - backend_pool_name -- Name to use for the backend pool when creating a new load balancer or application gateway.
    - backend_port -- When creating a new load balancer, backend port to open with NAT rules (Defaults to 22 on Linux and 3389 on Windows). When creating an application gateway, the backend port to use for the backend HTTP settings.
    - capacity_reservation_group -- The ID or name of the capacity reservation group that is used to allocate. Pass in "None" to disassociate the capacity reservation group. Please note that if you want to delete a VM/VMSS that has been associated with capacity reservation group, you need to disassociate the capacity reservation group first.
    - computer_name_prefix -- Computer name prefix for all of the virtual machines in the scale set. Computer name prefixes must be 1 to 15 characters long
    - custom_data -- Custom init script file or text (cloud-init, cloud-config, etc..)
    - data_disk_caching -- storage caching type for data disk(s), including 'None', 'ReadOnly', 'ReadWrite', etc. Use a singular value to apply on all disks, or use `<lun>=<vaule1> <lun>=<value2>` to configure individual disk
    - data_disk_encryption_sets -- Names or IDs (space delimited) of disk encryption sets for data disks.
    - data_disk_iops -- Specify the Read-Write IOPS (space delimited) for the managed disk. Should be used only when StorageAccountType is UltraSSD_LRS. If not specified, a default value would be assigned based on diskSizeGB.
    - data_disk_mbps -- Specify the bandwidth in MB per second (space delimited) for the managed disk. Should be used only when StorageAccountType is UltraSSD_LRS. If not specified, a default value would be assigned based on diskSizeGB.
    - data_disk_sizes_gb -- space-separated empty managed data disk sizes in GB to create
    - disable_overprovision -- Overprovision option (see https://azure.microsoft.com/documentation/articles/virtual-machine-scale-sets-overview/ for details).
    - dns_servers -- space-separated IP addresses of DNS servers, e.g. 10.0.0.5 10.0.0.6
    - edge_zone -- The name of edge zone.
    - enable_agent -- Indicate whether virtual machine agent should be provisioned on the virtual machine. When this property is not specified, default behavior is to set it to true. This will ensure that VM Agent is installed on the VM so that extensions can be added to the VM later
    - enable_auto_update -- Indicate whether Automatic Updates is enabled for the Windows virtual machine
    - enable_cross_zone_upgrade -- Set this Boolean property will allow VMSS to ignore AZ boundaries when constructing upgrade batches, and only consider Update Domain and maxBatchInstancePercent to determine the batch size
    - enable_spot_restore -- Enable the Spot-Try-Restore feature where evicted VMSS SPOT instances will be tried to be restored opportunistically based on capacity availability and pricing constraints
    - encryption_at_host -- Enable Host Encryption for the VM or VMSS. This will enable the encryption for all the disks including Resource/Temp disk at host itself.
    - ephemeral_os_disk -- Allows you to create an OS disk directly on the host node, providing local disk performance and faster VM/VMSS reimage time.
    - ephemeral_os_disk_placement -- Only applicable when used with `--ephemeral-os-disk`. Allows you to choose the Ephemeral OS disk provisioning location.
    - eviction_policy -- The eviction policy for virtual machines in a Spot priority scale set. Default eviction policy is Deallocate for a Spot priority scale set
    - generate_ssh_keys -- Generate SSH public and private key files if missing. The keys will be stored in the ~/.ssh directory
    - health_probe -- Probe name from the existing load balancer, mainly used for rolling upgrade or automatic repairs
    - host_group -- Name or ID of dedicated host group that the virtual machine scale set resides in
    - image -- None
    - instance_count -- Number of VMs in the scale set.
    - lb_nat_pool_name -- Name to use for the NAT pool when creating a new load balancer.
    - lb_sku -- Sku of the Load Balancer to create. Default to 'Standard' when single placement group is turned off; otherwise, default to 'Basic'. The public IP is supported to be created on edge zone only when it is 'Standard'
    - license_type -- Specifies that the Windows image or disk was licensed on-premises. To enable Azure Hybrid Benefit for Windows Server, use 'Windows_Server'. To enable Multitenant Hosting Rights for Windows 10, use 'Windows_Client'. For more information see the Azure Windows VM online docs.
    - load_balancer -- Name to use when creating a new load balancer (default) or referencing an existing one. Can also reference an existing load balancer by ID or specify "" for none.
    - location -- Location in which to create VM and related resources. If default location is not configured, will default to the resource group's location
    - max_batch_instance_percent -- The maximum percent of total virtual machine instances that will be upgraded simultaneously by the rolling upgrade in one batch. Default: 20%
    - max_price -- The maximum price (in US Dollars) you are willing to pay for a Spot VM/VMSS. -1 indicates that the Spot VM/VMSS should not be evicted for price reasons
    - max_unhealthy_instance_percent -- The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy. Default: 20%
    - max_unhealthy_upgraded_instance_percent -- The maximum percentage of upgraded virtual machine instances that can be found to be in an unhealthy state. Default: 20%
    - network_api_version -- Specify the Microsoft.Network API version used when creating networking resources in the Network Interface Configurations for Virtual Machine Scale Set with orchestration mode 'Flexible'. Default value is 2020-11-01.
    - no_wait -- Do not wait for the long-running operation to finish.
    - nsg -- Name or ID of an existing Network Security Group.
    - orchestration_mode -- Choose how virtual machines are managed by the scale set. In Uniform mode, you define a virtual machine model and Azure will generate identical instances based on that model. In Flexible mode, you manually create and add a virtual machine of any configuration to the scale set or generate identical instances based on virtual machine model defined for the scale set.
    - os_disk_caching -- Storage caching type for the VM OS disk. Default: ReadWrite
    - os_disk_encryption_set -- Name or ID of disk encryption set for OS disk.
    - os_disk_name -- The name of the new VM OS disk.
    - os_disk_size_gb -- OS disk size in GB to create.
    - os_type -- Type of OS installed on a custom VHD. Do not use when specifying an URN or URN alias.
    - patch_mode -- Mode of in-guest patching to IaaS virtual machine. Allowed values for Windows VM: AutomaticByOS, AutomaticByPlatform, Manual. Allowed values for Linux VM: AutomaticByPlatform, ImageDefault. Manual - You control the application of patches to a virtual machine. You do this by applying patches manually inside the VM. In this mode, automatic updates are disabled; the paramater --enable-auto-update must be false. AutomaticByOS - The virtual machine will automatically be updated by the OS. The parameter --enable-auto-update must be true. AutomaticByPlatform - the virtual machine will automatically updated by the OS. ImageDefault - The virtual machine's default patching configuration is used. The parameter --enable-agent and --enable-auto-update must be true
    - pause_time_between_batches -- The wait time between completing the update for all virtual machines in one batch and starting the next batch. Default: 0 seconds
    - plan_name -- plan name
    - plan_product -- plan product
    - plan_promotion_code -- plan promotion code
    - plan_publisher -- plan publisher
    - platform_fault_domain_count -- Fault Domain count for each placement group in the availability zone
    - ppg -- The name or ID of the proximity placement group the VMSS should be associated with.
    - prioritize_unhealthy_instances -- Set this Boolean property will lead to all unhealthy instances in a scale set getting upgraded before any healthy instances
    - priority -- Priority. Use 'Spot' to run short-lived workloads in a cost-effective way. 'Low' enum will be deprecated in the future. Please use 'Spot' to deploy Azure spot VM and/or VMSS. Default to Regular.
    - public_ip_address -- Name of the public IP address when creating one (default) or referencing an existing one. Can also reference an existing public IP by ID or specify "" for None ('""' in Azure CLI using PowerShell or --% operator).
    - public_ip_address_allocation -- None
    - public_ip_address_dns_name -- Globally unique DNS name for a newly created public IP.
    - public_ip_per_vm -- Each VM instance will have a public ip. For security, you can use '--nsg' to apply appropriate rules
    - role -- Role name or id the system assigned identity will have
    - scale_in_policy -- Specify the scale-in policy (space delimited) that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled-in.
    - scope -- Scope that the system assigned identity can access
    - secrets -- One or many Key Vault secrets as JSON strings or files via `@{path}` containing `[{ "sourceVault": { "id": "value" }, "vaultCertificates": [{ "certificateUrl": "value", "certificateStore": "cert store name (only on windows)"}] }]`
    - single_placement_group -- Limit the scale set to a single placement group. See https://docs.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups for details.
    - specialized -- Indicate whether the source image is specialized.
    - spot_restore_timeout -- Timeout value expressed as an ISO 8601 time duration after which the platform will not try to restore the VMSS SPOT instances
    - ssh_dest_key_path -- Destination file path on the VM for the SSH key. If the file already exists, the specified key(s) are appended to the file. Destination path for SSH public keys is currently limited to its default value "/home/username/.ssh/authorized_keys" due to a known issue in Linux provisioning agent.
    - ssh_key_values -- None
    - storage_container_name -- Only applicable when used with `--use-unmanaged-disk`. Name of the storage container for the VM OS disk. Default: vhds
    - storage_sku -- The SKU of the storage account with which to persist VM. Use a singular sku that would be applied across all disks, or specify individual disks. Usage: [--storage-sku SKU | --storage-sku ID=SKU ID=SKU ID=SKU...], where each ID is "os" or a 0-indexed lun. Allowed values: Standard_LRS, Premium_LRS, StandardSSD_LRS, UltraSSD_LRS, Premium_ZRS, StandardSSD_ZRS.
    - subnet -- The name of the subnet when creating a new VNet or referencing an existing one. Can also reference an existing subnet by ID. If both vnet-name and subnet are omitted, an appropriate VNet and subnet will be selected automatically, or a new one will be created.
    - subnet_address_prefix -- The subnet IP address prefix to use when creating a new VNet in CIDR format.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - terminate_notification_time -- Length of time (in minutes, between 5 and 15) a notification to be sent to the VM on the instance metadata server till the VM gets deleted
    - ultra_ssd_enabled -- Enables or disables the capability to have 1 or more managed data disks with UltraSSD_LRS storage account
    - upgrade_policy_mode -- None
    - use_unmanaged_disk -- Do not use managed disk to persist VM
    - user_data -- UserData for the virtual machines in the scale set. It can be passed in as file or string.
    - validate -- Generate and validate the ARM template without creating any resources.
    - vm_domain_name -- domain name of VM instances, once configured, the FQDN is `vm<vm-index>.<vm-domain-name>.<..rest..>`
    - vm_sku -- Size of VMs in the scale set. Default to "Standard_DS1_v2". See https://azure.microsoft.com/pricing/details/virtual-machines/ for size info.
    - vnet_address_prefix -- The IP address prefix to use when creating a new VNet in CIDR format.
    - vnet_name -- Name of the virtual network when creating a new one or referencing an existing one.
    - zones -- Space-separated list of availability zones into which to provision the resource.
    '''
    return _call_az("az vmss create", locals())


def deallocate(name, resource_group, instance_ids=None, no_wait=None):
    '''
    Deallocate VMs within a VMSS.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - instance_ids -- Space-separated list of IDs (ex: 1 2 3 ...) or * for all instances. If not provided, the action will be applied on the scaleset itself
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vmss deallocate", locals())


def delete(name, resource_group, force_deletion=None, no_wait=None):
    '''
    

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - force_deletion -- Optional parameter to force delete a VM scale set. (Feature in Preview).
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vmss delete", locals())


def delete_instances(instance_ids, name, resource_group, no_wait=None):
    '''
    Delete VMs within a VMSS.

    Required Parameters:
    - instance_ids -- Space-separated list of IDs (ex: 1 2 3 ...) or * for all instances.
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vmss delete-instances", locals())


def get_instance_view(name, resource_group, instance_id=None):
    '''
    View an instance of a VMSS.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - instance_id -- None
    '''
    return _call_az("az vmss get-instance-view", locals())


def list(resource_group=None):
    '''
    List VMSS.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vmss list", locals())


def list_instances(name, resource_group, expand=None, filter=None, select=None):
    '''
    Get a list of all virtual machines in a VM scale sets.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- The expand expression to apply to the operation. Allowed values are 'instanceView'.
    - filter -- The filter to apply to the operation. Allowed values are 'startswith(instanceView/statuses/code, 'PowerState') eq true', 'properties/latestModelApplied eq true', 'properties/latestModelApplied eq false'.
    - select -- The list parameters. Allowed values are 'instanceView', 'instanceView/statuses'.
    '''
    return _call_az("az vmss list-instances", locals())


def list_instance_connection_info(name, resource_group):
    '''
    Get the IP address and port number used to connect to individual VM instances within a set.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vmss list-instance-connection-info", locals())


def list_instance_public_ips(name, resource_group):
    '''
    List public IP addresses of VM instances within a set.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vmss list-instance-public-ips", locals())


def list_skus(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vmss list-skus", locals())


def reimage(name, resource_group, instance_id=None, no_wait=None):
    '''
    Reimage VMs within a VMSS.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - instance_id -- None
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vmss reimage", locals())


def perform_maintenance(name, resource_group, vm_instance_i_ds=None):
    '''
    

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - vm_instance_i_ds -- A list of virtual machine instance IDs from the VM scale set.
    '''
    return _call_az("az vmss perform-maintenance", locals())


def restart(name, resource_group, instance_ids=None, no_wait=None):
    '''
    Restart VMs within a VMSS.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - instance_ids -- Space-separated list of IDs (ex: 1 2 3 ...) or * for all instances. If not provided, the action will be applied on the scaleset itself
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vmss restart", locals())


def scale(name, new_capacity, resource_group, no_wait=None):
    '''
    Change the number of VMs within a VMSS.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - new_capacity -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vmss scale", locals())


def show(name, resource_group, include_user_data=None, instance_id=None):
    '''
    Get details on VMs within a VMSS.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - include_user_data -- Include the user data properties in the query result.
    - instance_id -- None
    '''
    return _call_az("az vmss show", locals())


def simulate_eviction(instance_id, name, resource_group):
    '''
    Simulate the eviction of a Spot virtual machine in a VM scale set.

    Required Parameters:
    - instance_id -- The instance ID of the virtual machine.
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vmss simulate-eviction", locals())


def start(name, resource_group, instance_ids=None, no_wait=None):
    '''
    Start VMs within a VMSS.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - instance_ids -- Space-separated list of IDs (ex: 1 2 3 ...) or * for all instances. If not provided, the action will be applied on the scaleset itself
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vmss start", locals())


def stop(name, resource_group, instance_ids=None, no_wait=None, skip_shutdown=None):
    '''
    Power off (stop) VMs within a VMSS.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - instance_ids -- Space-separated list of IDs (ex: 1 2 3 ...) or * for all instances. If not provided, the action will be applied on the scaleset itself
    - no_wait -- Do not wait for the long-running operation to finish.
    - skip_shutdown -- Skip shutdown and power-off immediately.
    '''
    return _call_az("az vmss stop", locals())


def update(name, resource_group, add=None, automatic_repairs_grace_period=None, capacity_reservation_group=None, enable_automatic_repairs=None, enable_cross_zone_upgrade=None, enable_spot_restore=None, enable_terminate_notification=None, ephemeral_os_disk_placement=None, force_string=None, instance_id=None, license_type=None, max_batch_instance_percent=None, max_price=None, max_unhealthy_instance_percent=None, max_unhealthy_upgraded_instance_percent=None, no_wait=None, pause_time_between_batches=None, ppg=None, prioritize_unhealthy_instances=None, priority=None, protect_from_scale_in=None, protect_from_scale_set_actions=None, remove=None, scale_in_policy=None, set=None, spot_restore_timeout=None, terminate_notification_time=None, ultra_ssd_enabled=None, user_data=None, vm_sku=None):
    '''
    Update a VMSS. Run 'az vmss update-instances' command to roll out the changes to VMs if you have not configured upgrade policy.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - automatic_repairs_grace_period -- The amount of time (in minutes, between 30 and 90) for which automatic repairs are suspended due to a state change on VM.
    - capacity_reservation_group -- The ID or name of the capacity reservation group that is used to allocate. Pass in "None" to disassociate the capacity reservation group. Please note that if you want to delete a VM/VMSS that has been associated with capacity reservation group, you need to disassociate the capacity reservation group first.
    - enable_automatic_repairs -- Enable automatic repairs
    - enable_cross_zone_upgrade -- Set this Boolean property will allow VMSS to ignore AZ boundaries when constructing upgrade batches, and only consider Update Domain and maxBatchInstancePercent to determine the batch size
    - enable_spot_restore -- Enable the Spot-Try-Restore feature where evicted VMSS SPOT instances will be tried to be restored opportunistically based on capacity availability and pricing constraints
    - enable_terminate_notification -- Enable terminate notification
    - ephemeral_os_disk_placement -- Only applicable when used with `--vm-sku`. Allows you to choose the Ephemeral OS disk provisioning location.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - instance_id -- Update the VM instance with this ID. If missing, Update the VMSS.
    - license_type -- Specifies that the Windows image or disk was licensed on-premises. To enable Azure Hybrid Benefit for Windows Server, use 'Windows_Server'. To enable Multitenant Hosting Rights for Windows 10, use 'Windows_Client'. For more information see the Azure Windows VM online docs.
    - max_batch_instance_percent -- The maximum percent of total virtual machine instances that will be upgraded simultaneously by the rolling upgrade in one batch. Default: 20%
    - max_price -- The maximum price (in US Dollars) you are willing to pay for a Spot VM/VMSS. -1 indicates that the Spot VM/VMSS should not be evicted for price reasons
    - max_unhealthy_instance_percent -- The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy. Default: 20%
    - max_unhealthy_upgraded_instance_percent -- The maximum percentage of upgraded virtual machine instances that can be found to be in an unhealthy state. Default: 20%
    - no_wait -- Do not wait for the long-running operation to finish.
    - pause_time_between_batches -- The wait time between completing the update for all virtual machines in one batch and starting the next batch. Default: 0 seconds
    - ppg -- The name or ID of the proximity placement group the VMSS should be associated with.
    - prioritize_unhealthy_instances -- Set this Boolean property will lead to all unhealthy instances in a scale set getting upgraded before any healthy instances
    - priority -- Priority. Use 'Spot' to run short-lived workloads in a cost-effective way. 'Low' enum will be deprecated in the future. Please use 'Spot' to deploy Azure spot VM and/or VMSS. Default to Regular.
    - protect_from_scale_in -- Protect the VM instance from scale-in operations.
    - protect_from_scale_set_actions -- Protect the VM instance from scale set actions (including scale-in).
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - scale_in_policy -- Specify the scale-in policy (space delimited) that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled-in.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - spot_restore_timeout -- Timeout value expressed as an ISO 8601 time duration after which the platform will not try to restore the VMSS SPOT instances
    - terminate_notification_time -- Length of time (in minutes, between 5 and 15) a notification to be sent to the VM on the instance metadata server till the VM gets deleted
    - ultra_ssd_enabled -- Enables or disables the capability to have 1 or more managed data disks with UltraSSD_LRS storage account
    - user_data -- UserData for the virtual machines in the scale set. It can be passed in as file or string. If empty string is passed in, the existing value will be deleted.
    - vm_sku -- The new size of the virtual machine instances in the scale set. Default to "Standard_DS1_v2". See https://azure.microsoft.com/pricing/details/virtual-machines/ for size info.
    '''
    return _call_az("az vmss update", locals())


def update_instances(instance_ids, name, resource_group, no_wait=None):
    '''
    Upgrade VMs within a VMSS.

    Required Parameters:
    - instance_ids -- Space-separated list of IDs (ex: 1 2 3 ...) or * for all instances.
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vmss update-instances", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, instance_id=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of a scale set is met.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - instance_id -- Wait on the VM instance with this ID. If missing, Wait on the VMSS.
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az vmss wait", locals())


def get_os_upgrade_history(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vmss get-os-upgrade-history", locals())


def set_orchestration_service_state(action, name, resource_group, service_name, no_wait=None):
    '''
    Change ServiceState property for a given service within a VMSS.

    Required Parameters:
    - action -- The action to be performed.
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the orchestration service.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vmss set-orchestration-service-state", locals())

