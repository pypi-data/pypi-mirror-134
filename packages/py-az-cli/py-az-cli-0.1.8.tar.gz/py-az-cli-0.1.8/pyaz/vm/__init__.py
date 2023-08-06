'''
Manage Linux or Windows virtual machines.
'''
from .. pyaz_utils import _call_az
from . import application, availability_set, boot_diagnostics, diagnostics, disk, encryption, extension, host, identity, image, nic, run_command, secret, unmanaged_disk, user


def capture(name, resource_group, vhd_name_prefix, overwrite=None, storage_container=None):
    '''
    Capture information for a stopped VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vhd_name_prefix -- None

    Optional Parameters:
    - overwrite -- None
    - storage_container -- None
    '''
    return _call_az("az vm capture", locals())


def create(name, resource_group, accelerated_networking=None, admin_password=None, admin_username=None, asgs=None, assign_identity=None, attach_data_disks=None, attach_os_disk=None, authentication_type=None, availability_set=None, boot_diagnostics_storage=None, capacity_reservation_group=None, computer_name=None, count=None, custom_data=None, data_disk_caching=None, data_disk_delete_option=None, data_disk_encryption_sets=None, data_disk_sizes_gb=None, edge_zone=None, enable_agent=None, enable_auto_update=None, enable_hibernation=None, enable_hotpatching=None, enable_secure_boot=None, enable_vtpm=None, encryption_at_host=None, ephemeral_os_disk=None, ephemeral_os_disk_placement=None, eviction_policy=None, generate_ssh_keys=None, host=None, host_group=None, image=None, license_type=None, location=None, max_price=None, nic_delete_option=None, nics=None, no_wait=None, nsg=None, nsg_rule=None, os_disk_caching=None, os_disk_delete_option=None, os_disk_encryption_set=None, os_disk_name=None, os_disk_size_gb=None, os_type=None, patch_mode=None, plan_name=None, plan_product=None, plan_promotion_code=None, plan_publisher=None, platform_fault_domain=None, ppg=None, priority=None, private_ip_address=None, public_ip_address=None, public_ip_address_allocation=None, public_ip_address_dns_name=None, public_ip_sku=None, role=None, scope=None, secrets=None, security_type=None, size=None, specialized=None, ssh_dest_key_path=None, ssh_key_name=None, ssh_key_values=None, storage_account=None, storage_container_name=None, storage_sku=None, subnet=None, subnet_address_prefix=None, tags=None, ultra_ssd_enabled=None, use_unmanaged_disk=None, user_data=None, validate=None, vmss=None, vnet_address_prefix=None, vnet_name=None, workspace=None, zone=None):
    '''
    Create an Azure Virtual Machine.

    Required Parameters:
    - name -- Name of the virtual machine.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - accelerated_networking -- enable accelerated networking. Unless specified, CLI will enable it based on machine image and size
    - admin_password -- Password for the VM if authentication type is 'Password'.
    - admin_username -- Username for the VM. Default value is current username of OS. If the default value is system reserved, then default value will be set to azureuser. Please refer to https://docs.microsoft.com/rest/api/compute/virtualmachines/createorupdate#osprofile to get a full list of reserved values.
    - asgs -- Space-separated list of existing application security groups to associate with the VM.
    - assign_identity -- accept system or user assigned identities separated by spaces. Use '[system]' to refer system assigned identity, or a resource id to refer user assigned identity. Check out help for more examples
    - attach_data_disks -- Attach existing data disks to the VM. Can use the name or ID of a managed disk or the URI to an unmanaged disk VHD.
    - attach_os_disk -- Attach an existing OS disk to the VM. Can use the name or ID of a managed disk or the URI to an unmanaged disk VHD.
    - authentication_type -- Type of authentication to use with the VM. Defaults to password for Windows and SSH public key for Linux. "all" enables both ssh and password authentication. 
    - availability_set -- Name or ID of an existing availability set to add the VM to. None by default.
    - boot_diagnostics_storage -- pre-existing storage account name or its blob uri to capture boot diagnostics. Its sku should be one of Standard_GRS, Standard_LRS and Standard_RAGRS
    - capacity_reservation_group -- The ID or name of the capacity reservation group that is used to allocate. Pass in "None" to disassociate the capacity reservation group. Please note that if you want to delete a VM/VMSS that has been associated with capacity reservation group, you need to disassociate the capacity reservation group first.
    - computer_name -- None
    - count -- Number of virtual machines to create. Value range is [2, 250], inclusive. Don't specify this parameter if you want to create a normal single VM. The VMs are created in parallel. The output of this command is an array of VMs instead of one single VM. Each VM has its own public IP, NIC. VNET and NSG are shared. It is recommended that no existing public IP, NIC, VNET and NSG are in resource group. When --count is specified, --attach-data-disks, --attach-os-disk, --boot-diagnostics-storage, --computer-name, --host, --host-group, --nics, --os-disk-name, --private-ip-address, --public-ip-address, --public-ip-address-dns-name, --storage-account, --storage-container-name, --subnet, --use-unmanaged-disk, --vnet-name are not allowed.
    - custom_data -- Custom init script file or text (cloud-init, cloud-config, etc..)
    - data_disk_caching -- storage caching type for data disk(s), including 'None', 'ReadOnly', 'ReadWrite', etc. Use a singular value to apply on all disks, or use `<lun>=<vaule1> <lun>=<value2>` to configure individual disk
    - data_disk_delete_option -- Specify whether data disk should be deleted or detached upon VM deletion.
    - data_disk_encryption_sets -- Names or IDs (space delimited) of disk encryption sets for data disks.
    - data_disk_sizes_gb -- space-separated empty managed data disk sizes in GB to create
    - edge_zone -- The name of edge zone.
    - enable_agent -- Indicates whether virtual machine agent should be provisioned on the virtual machine. When this property is not specified, default behavior is to set it to true. This will ensure that VM Agent is installed on the VM so that extensions can be added to the VM later
    - enable_auto_update -- Indicate whether Automatic Updates is enabled for the Windows virtual machine
    - enable_hibernation -- The flag that enable or disable hibernation capability on the VM.
    - enable_hotpatching -- Patch VMs without requiring a reboot. --enable-agent must be set and --patch-mode must be set to AutomaticByPlatform
    - enable_secure_boot -- Enable secure boot. It is part of trusted launch.
    - enable_vtpm -- Enable vTPM. It is part of trusted launch.
    - encryption_at_host -- Enable Host Encryption for the VM or VMSS. This will enable the encryption for all the disks including Resource/Temp disk at host itself.
    - ephemeral_os_disk -- Allows you to create an OS disk directly on the host node, providing local disk performance and faster VM/VMSS reimage time.
    - ephemeral_os_disk_placement -- Only applicable when used with `--ephemeral-os-disk`. Allows you to choose the Ephemeral OS disk provisioning location.
    - eviction_policy -- The eviction policy for the Spot priority virtual machine. Default eviction policy is Deallocate for a Spot priority virtual machine
    - generate_ssh_keys -- Generate SSH public and private key files if missing. The keys will be stored in the ~/.ssh directory
    - host -- ID of the dedicated host that the VM will reside in. --host and --host-group can't be used together.
    - host_group -- Name or ID of the dedicated host group that the VM will reside in. --host and --host-group can't be used together.
    - image -- None
    - license_type -- Specifies that the Windows image or disk was licensed on-premises. To enable Azure Hybrid Benefit for Windows Server, use 'Windows_Server'. To enable Multitenant Hosting Rights for Windows 10, use 'Windows_Client'. For more information see the Azure Windows VM online docs.
    - location -- Location in which to create VM and related resources. If default location is not configured, will default to the resource group's location
    - max_price -- The maximum price (in US Dollars) you are willing to pay for a Spot VM/VMSS. -1 indicates that the Spot VM/VMSS should not be evicted for price reasons
    - nic_delete_option -- Specify what happens to the network interface when the VM is deleted. Use a singular value to apply on all resources, or use <Name>=<Value> to configure the delete behavior for individual resources. Possible options are Delete and Detach.
    - nics -- Names or IDs of existing NICs to attach to the VM. The first NIC will be designated as primary. If omitted, a new NIC will be created. If an existing NIC is specified, do not specify subnet, VNet, public IP or NSG.
    - no_wait -- Do not wait for the long-running operation to finish.
    - nsg -- The name to use when creating a new Network Security Group (default) or referencing an existing one. Can also reference an existing NSG by ID or specify "" for none ('""' in Azure CLI using PowerShell or --% operator).
    - nsg_rule -- NSG rule to create when creating a new NSG. Defaults to open ports for allowing RDP on Windows and allowing SSH on Linux. NONE represents no NSG rule
    - os_disk_caching -- Storage caching type for the VM OS disk. Default: ReadWrite
    - os_disk_delete_option -- Specify the behavior of the managed disk when the VM gets deleted i.e whether the managed disk is deleted or detached.
    - os_disk_encryption_set -- Name or ID of disk encryption set for OS disk.
    - os_disk_name -- The name of the new VM OS disk.
    - os_disk_size_gb -- OS disk size in GB to create.
    - os_type -- Type of OS installed on a custom VHD. Do not use when specifying an URN or URN alias.
    - patch_mode -- Mode of in-guest patching to IaaS virtual machine. Allowed values for Windows VM: AutomaticByOS, AutomaticByPlatform, Manual. Allowed values for Linux VM: AutomaticByPlatform, ImageDefault. Manual - You control the application of patches to a virtual machine. You do this by applying patches manually inside the VM. In this mode, automatic updates are disabled; the paramater --enable-auto-update must be false. AutomaticByOS - The virtual machine will automatically be updated by the OS. The parameter --enable-auto-update must be true. AutomaticByPlatform - the virtual machine will automatically updated by the OS. ImageDefault - The virtual machine's default patching configuration is used. The parameter --enable-agent and --enable-auto-update must be true
    - plan_name -- plan name
    - plan_product -- plan product
    - plan_promotion_code -- plan promotion code
    - plan_publisher -- plan publisher
    - platform_fault_domain -- Specify the scale set logical fault domain into which the virtual machine will be created. By default, the virtual machine will be automatically assigned to a fault domain that best maintains balance across available fault domains. This is applicable only if the virtualMachineScaleSet property of this virtual machine is set. The virtual machine scale set that is referenced, must have platform fault domain count. This property cannot be updated once the virtual machine is created. Fault domain assignment can be viewed in the virtual machine instance view
    - ppg -- The name or ID of the proximity placement group the VM should be associated with.
    - priority -- Priority. Use 'Spot' to run short-lived workloads in a cost-effective way. 'Low' enum will be deprecated in the future. Please use 'Spot' to deploy Azure spot VM and/or VMSS. Default to Regular.
    - private_ip_address -- Static private IP address (e.g. 10.0.0.5).
    - public_ip_address -- Name of the public IP address when creating one (default) or referencing an existing one. Can also reference an existing public IP by ID or specify "" for None ('""' in Azure CLI using PowerShell or --% operator).
    - public_ip_address_allocation -- None
    - public_ip_address_dns_name -- Globally unique DNS name for a newly created public IP.
    - public_ip_sku -- Public IP SKU. It is set to Basic by default. The public IP is supported to be created on edge zone only when it is 'Standard'
    - role -- Role name or id the system assigned identity will have
    - scope -- Scope that the system assigned identity can access
    - secrets -- One or many Key Vault secrets as JSON strings or files via `@{path}` containing `[{ "sourceVault": { "id": "value" }, "vaultCertificates": [{ "certificateUrl": "value", "certificateStore": "cert store name (only on windows)"}] }]`
    - security_type -- Specify if the VM is Trusted Launch enabled. See https://docs.microsoft.com/azure/virtual-machines/trusted-launch.
    - size -- The VM size to be created. See https://azure.microsoft.com/pricing/details/virtual-machines/ for size info.
    - specialized -- Indicate whether the source image is specialized.
    - ssh_dest_key_path -- Destination file path on the VM for the SSH key. If the file already exists, the specified key(s) are appended to the file. Destination path for SSH public keys is currently limited to its default value "/home/username/.ssh/authorized_keys" due to a known issue in Linux provisioning agent.
    - ssh_key_name -- Use it as public key in virtual machine. It should be an existing SSH key resource in Azure.
    - ssh_key_values -- None
    - storage_account -- Only applicable when used with `--use-unmanaged-disk`. The name to use when creating a new storage account or referencing an existing one. If omitted, an appropriate storage account in the same resource group and location will be used, or a new one will be created.
    - storage_container_name -- Only applicable when used with `--use-unmanaged-disk`. Name of the storage container for the VM OS disk. Default: vhds
    - storage_sku -- The SKU of the storage account with which to persist VM. Use a singular sku that would be applied across all disks, or specify individual disks. Usage: [--storage-sku SKU | --storage-sku ID=SKU ID=SKU ID=SKU...], where each ID is "os" or a 0-indexed lun. Allowed values: Standard_LRS, Premium_LRS, StandardSSD_LRS, UltraSSD_LRS, Premium_ZRS, StandardSSD_ZRS.
    - subnet -- The name of the subnet when creating a new VNet or referencing an existing one. Can also reference an existing subnet by ID. If both vnet-name and subnet are omitted, an appropriate VNet and subnet will be selected automatically, or a new one will be created.
    - subnet_address_prefix -- The subnet IP address prefix to use when creating a new VNet in CIDR format.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - ultra_ssd_enabled -- Enables or disables the capability to have 1 or more managed data disks with UltraSSD_LRS storage account
    - use_unmanaged_disk -- Do not use managed disk to persist VM
    - user_data -- UserData for the VM. It can be passed in as file or string.
    - validate -- Generate and validate the ARM template without creating any resources.
    - vmss -- Name or ID of an existing virtual machine scale set that the virtual machine should be assigned to. None by default.
    - vnet_address_prefix -- The IP address prefix to use when creating a new VNet in CIDR format.
    - vnet_name -- Name of the virtual network when creating a new one or referencing an existing one.
    - workspace -- Name or ID of Log Analytics Workspace. If you specify the workspace through its name, the workspace should be in the same resource group with the vm, otherwise a new workspace will be created.
    - zone -- Availability zone into which to provision the resource.
    '''
    return _call_az("az vm create", locals())


def convert(name, resource_group):
    '''
    Convert a VM with unmanaged disks to use managed disks.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm convert", locals())


def deallocate(name, resource_group, hibernate=None, no_wait=None):
    '''
    Deallocate a VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - hibernate -- Optional parameter to hibernate a virtual machine. (Feature in Preview).
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vm deallocate", locals())


def delete(name, resource_group, force_deletion=None, no_wait=None, yes=None):
    '''
    Delete a VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - force_deletion -- Optional parameter to force delete virtual machines.(Feature in Preview).
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az vm delete", locals())


def generalize(name, resource_group, no_wait=None):
    '''
    Mark a VM as generalized, allowing it to be imaged for multiple deployments.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vm generalize", locals())


def get_instance_view(name, resource_group):
    '''
    Get instance information about a VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm get-instance-view", locals())


def list(resource_group=None, show_details=None):
    '''
    List details of Virtual Machines.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - show_details -- show public ip address, FQDN, and power states. command will run slow
    '''
    return _call_az("az vm list", locals())


def list_ip_addresses(name=None, resource_group=None):
    '''
    List IP addresses associated with a VM.

    Optional Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm list-ip-addresses", locals())


def list_sizes(location):
    '''
    List available sizes for VMs.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az vm list-sizes", locals())


def list_skus(all=None, location=None, resource_type=None, size=None, zone=None):
    '''
    Get details for compute-related resource SKUs.

    Optional Parameters:
    - all -- show all information including vm sizes not available under the current subscription
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - resource_type -- resource types e.g. "availabilitySets", "snapshots", "disks", etc
    - size -- size name, partial name is accepted
    - zone -- show skus supporting availability zones
    '''
    return _call_az("az vm list-skus", locals())


def list_usage(location):
    '''
    List available usage resources for VMs.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az vm list-usage", locals())


def list_vm_resize_options(name, resource_group):
    '''
    List available resizing options for VMs.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm list-vm-resize-options", locals())


def open_port(name, port, resource_group, apply_to_subnet=None, nsg_name=None, priority=None):
    '''
    Opens a VM to inbound traffic on specified ports.

    Required Parameters:
    - name -- The name of the virtual machine to open inbound traffic on.
    - port -- The port or port range (ex: 80-100) to open inbound traffic to. Use '*' to allow traffic to all ports. Use comma separated values to specify more than one port or port range.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - apply_to_subnet -- Allow inbound traffic on the subnet instead of the NIC
    - nsg_name -- The name of the network security group to create if one does not exist. Ignored if an NSG already exists.
    - priority -- Rule priority, between 100 (highest priority) and 4096 (lowest priority). Must be unique for each rule in the collection.
    '''
    return _call_az("az vm open-port", locals())


def perform_maintenance(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm perform-maintenance", locals())


def redeploy(name, resource_group, no_wait=None):
    '''
    Redeploy an existing VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vm redeploy", locals())


def resize(name, resource_group, size, no_wait=None):
    '''
    Update a VM's size.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - size -- None

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vm resize", locals())


def restart(name, resource_group, force=None, no_wait=None):
    '''
    Restart VMs.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - force -- Force the VM to restart by redeploying it. Use if the VM is unresponsive.
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vm restart", locals())


def show(name, resource_group, include_user_data=None, show_details=None):
    '''
    Get the details of a VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - include_user_data -- Include the user data properties in the query result.
    - show_details -- show public ip address, FQDN, and power states. command will run slow
    '''
    return _call_az("az vm show", locals())


def simulate_eviction(name, resource_group):
    '''
    Simulate the eviction of a Spot VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm simulate-eviction", locals())


def start(name, resource_group, no_wait=None):
    '''
    Start a stopped VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vm start", locals())


def stop(name, resource_group, no_wait=None, skip_shutdown=None):
    '''
    Power off (stop) a running VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - skip_shutdown -- Skip shutdown and power-off immediately.
    '''
    return _call_az("az vm stop", locals())


def reapply(name, resource_group, no_wait=None):
    '''
    Reapply VMs.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vm reapply", locals())


def update(name, resource_group, add=None, capacity_reservation_group=None, disk_caching=None, enable_hibernation=None, enable_secure_boot=None, enable_vtpm=None, ephemeral_os_disk_placement=None, force_string=None, host=None, host_group=None, license_type=None, max_price=None, no_wait=None, os_disk=None, ppg=None, priority=None, remove=None, set=None, size=None, ultra_ssd_enabled=None, user_data=None, workspace=None, write_accelerator=None):
    '''
    Update the properties of a VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - capacity_reservation_group -- The ID or name of the capacity reservation group that is used to allocate. Pass in "None" to disassociate the capacity reservation group. Please note that if you want to delete a VM/VMSS that has been associated with capacity reservation group, you need to disassociate the capacity reservation group first.
    - disk_caching -- Use singular value to apply across, or specify individual disks, e.g. 'os=ReadWrite 0=None 1=ReadOnly' should enable update os disk and 2 data disks
    - enable_hibernation -- The flag that enable or disable hibernation capability on the VM.
    - enable_secure_boot -- Enable secure boot.
    - enable_vtpm -- Enable vTPM.
    - ephemeral_os_disk_placement -- Only applicable when used with `--size`. Allows you to choose the Ephemeral OS disk provisioning location.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - host -- ID of the dedicated host that the VM will reside in. --host and --host-group can't be used together. You should deallocate the VM before update, and start the VM after update. Please check out help for more examples.
    - host_group -- Name or ID of the dedicated host group that the VM will reside in. --host and --host-group can't be used together. You should deallocate the VM before update, and start the VM after update. Please check out help for more examples.
    - license_type -- Specifies that the Windows image or disk was licensed on-premises. To enable Azure Hybrid Benefit for Windows Server, use 'Windows_Server'. To enable Multitenant Hosting Rights for Windows 10, use 'Windows_Client'. For more information see the Azure Windows VM online docs.
    - max_price -- The maximum price (in US Dollars) you are willing to pay for a Spot VM/VMSS. -1 indicates that the Spot VM/VMSS should not be evicted for price reasons
    - no_wait -- Do not wait for the long-running operation to finish.
    - os_disk -- Managed OS disk ID or name to swap to
    - ppg -- The name or ID of the proximity placement group the VM should be associated with.
    - priority -- Priority. Use 'Spot' to run short-lived workloads in a cost-effective way. 'Low' enum will be deprecated in the future. Please use 'Spot' to deploy Azure spot VM and/or VMSS. Default to Regular.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - size -- The new size of the virtual machine. See https://azure.microsoft.com/pricing/details/virtual-machines/ for size info.
    - ultra_ssd_enabled -- Enables or disables the capability to have 1 or more managed data disks with UltraSSD_LRS storage account
    - user_data -- UserData for the VM. It can be passed in as file or string. If empty string is passed in, the existing value will be deleted.
    - workspace -- Name or ID of Log Analytics Workspace. If you specify the workspace through its name, the workspace should be in the same resource group with the vm, otherwise a new workspace will be created.
    - write_accelerator -- enable/disable disk write accelerator. Use singular value 'true/false' to apply across, or specify individual disks, e.g.'os=true 1=true 2=true' for os disk and data disks with lun of 1 & 2
    '''
    return _call_az("az vm update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the VM is met.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
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
    return _call_az("az vm wait", locals())


def auto_shutdown(name, resource_group, email=None, location=None, off=None, time=None, webhook=None):
    '''
    Manage auto-shutdown for VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - email -- The email recipient to send notifications to (can be a list of semi-colon separated email addresses)
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - off -- Turn off auto-shutdown for VM. Configuration will be cleared.
    - time -- The UTC time of day the schedule will occur every day. Format: hhmm. Example: 1730
    - webhook -- The webhook URL to which the notification will be sent
    '''
    return _call_az("az vm auto-shutdown", locals())


def assess_patches(name, resource_group):
    '''
    Assess patches on a VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm assess-patches", locals())


def install_patches(maximum_duration, name, reboot_setting, resource_group, classifications_to_include_linux=None, classifications_to_include_win=None, exclude_kbs_requiring_reboot=None, kb_numbers_to_exclude=None, kb_numbers_to_include=None, no_wait=None, package_name_masks_to_exclude=None, package_name_masks_to_include=None):
    '''
    Install patches on a VM.

    Required Parameters:
    - maximum_duration -- Specify the maximum amount of time that the operation will run. It must be an ISO 8601-compliant duration string such as PT4H (4 hours)
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - reboot_setting -- Define when it is acceptable to reboot a VM during a software update operation.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - classifications_to_include_linux -- Space-separated list of classifications to include for Linux VM.
    - classifications_to_include_win -- Space-separated list of classifications to include for Windows VM.
    - exclude_kbs_requiring_reboot -- Filter out KBs that don't have a reboot behavior of 'NeverReboots' when this is set. Applicable to Windows VM only
    - kb_numbers_to_exclude -- Space-separated list of KBs to exclude in the patch operation. Applicable to Windows VM only
    - kb_numbers_to_include -- Space-separated list of KBs to include in the patch operation. Applicable to Windows VM only
    - no_wait -- Do not wait for the long-running operation to finish.
    - package_name_masks_to_exclude -- Space-separated list of packages to exclude in the patch operation. Format: packageName_packageVersion. Applicable to Linux VM only
    - package_name_masks_to_include -- Space-separated list of packages to include in the patch operation. Format: packageName_packageVersion. Applicable to Linux VM only
    '''
    return _call_az("az vm install-patches", locals())

