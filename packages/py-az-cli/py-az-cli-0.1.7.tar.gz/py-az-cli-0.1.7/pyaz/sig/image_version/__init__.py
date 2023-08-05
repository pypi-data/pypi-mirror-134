from ... pyaz_utils import _call_az

def delete(gallery_image_definition, gallery_image_version, gallery_name, resource_group):
    '''
    

    Required Parameters:
    - gallery_image_definition -- gallery image definition
    - gallery_image_version -- Gallery image version in semantic version pattern. The allowed characters are digit and period. Digits must be within the range of a 32-bit integer, e.g. `<MajorVersion>.<MinorVersion>.<Patch>`
    - gallery_name -- gallery name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sig image-version delete", locals())


def show(gallery_image_definition, gallery_image_version, gallery_name, resource_group, expand=None):
    '''
    

    Required Parameters:
    - gallery_image_definition -- gallery image definition
    - gallery_image_version -- Gallery image version in semantic version pattern. The allowed characters are digit and period. Digits must be within the range of a 32-bit integer, e.g. `<MajorVersion>.<MinorVersion>.<Patch>`
    - gallery_name -- gallery name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- The expand expression to apply on the operation, e.g. 'ReplicationStatus'
    '''
    return _call_az("az sig image-version show", locals())


def list(gallery_image_definition, gallery_name, resource_group):
    '''
    

    Required Parameters:
    - gallery_image_definition -- gallery image definition
    - gallery_name -- gallery name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sig image-version list", locals())


def create(gallery_image_definition, gallery_image_version, gallery_name, resource_group, data_snapshot_luns=None, data_snapshots=None, data_vhds_luns=None, data_vhds_storage_accounts=None, data_vhds_uris=None, end_of_life_date=None, exclude_from_latest=None, location=None, managed_image=None, no_wait=None, os_snapshot=None, os_vhd_storage_account=None, os_vhd_uri=None, replica_count=None, replication_mode=None, storage_account_type=None, tags=None, target_region_encryption=None, target_regions=None):
    '''
    create a new image version

    Required Parameters:
    - gallery_image_definition -- gallery image definition
    - gallery_image_version -- Gallery image version in semantic version pattern. The allowed characters are digit and period. Digits must be within the range of a 32-bit integer, e.g. `<MajorVersion>.<MinorVersion>.<Patch>`
    - gallery_name -- gallery name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - data_snapshot_luns -- Logical unit numbers (space-delimited) of data disk snapshots
    - data_snapshots -- Names or IDs (space-delimited) of data disk snapshots
    - data_vhds_luns -- Logical unit numbers (space-delimited) of source VHD URIs of data disks
    - data_vhds_storage_accounts -- Names or IDs (space-delimited) of storage accounts of source VHD URIs of data disks
    - data_vhds_uris -- Source VHD URIs (space-delimited) of data disks
    - end_of_life_date -- the end of life date, e.g. '2020-12-31'
    - exclude_from_latest -- The flag means that if it is set to true, people deploying VMs with version omitted will not use this version.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - managed_image -- image name(if in the same resource group) or resource id
    - no_wait -- Do not wait for the long-running operation to finish.
    - os_snapshot -- Name or ID of OS disk snapshot
    - os_vhd_storage_account -- Name or ID of storage account of source VHD URI of OS disk
    - os_vhd_uri -- Source VHD URI of OS disk
    - replica_count -- The default number of replicas to be created per region. To set regional replication counts, use --target-regions
    - replication_mode -- Optional parameter which specifies the mode to be used for replication. This property is not updatable.
    - storage_account_type -- The default storage account type to be used per region. To set regional storage account types, use --target-regions
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - target_region_encryption -- Space-separated list of customer managed keys for encrypting the OS and data disks in the gallery artifact for each region. Format for each region: `<os_des>,<lun1>,<lun1_des>,<lun2>,<lun2_des>`. Use "null" as a placeholder.
    - target_regions -- Space-separated list of regions and their replica counts. Use `<region>[=<replica count>][=<storage account type>]` to optionally set the replica count and/or storage account type for each region. If a replica count is not specified, the default replica count will be used. If a storage account type is not specified, the default storage account type will be used
    '''
    return _call_az("az sig image-version create", locals())


def update(gallery_image_definition, gallery_image_version, gallery_name, resource_group, add=None, force_string=None, no_wait=None, remove=None, replica_count=None, set=None, target_regions=None):
    '''
    update a share image version

    Required Parameters:
    - gallery_image_definition -- gallery image definition
    - gallery_image_version -- Gallery image version in semantic version pattern. The allowed characters are digit and period. Digits must be within the range of a 32-bit integer, e.g. `<MajorVersion>.<MinorVersion>.<Patch>`
    - gallery_name -- gallery name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - replica_count -- The default number of replicas to be created per region. To set regional replication counts, use --target-regions
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - target_regions -- Space-separated list of regions and their replica counts. Use `<region>[=<replica count>][=<storage account type>]` to optionally set the replica count and/or storage account type for each region. If a replica count is not specified, the default replica count will be used. If a storage account type is not specified, the default storage account type will be used
    '''
    return _call_az("az sig image-version update", locals())


def wait(gallery_image_definition, gallery_image_version, gallery_name, resource_group, created=None, custom=None, deleted=None, exists=None, expand=None, interval=None, timeout=None, updated=None):
    '''
    wait for image version related operation

    Required Parameters:
    - gallery_image_definition -- gallery image definition
    - gallery_image_version -- Gallery image version in semantic version pattern. The allowed characters are digit and period. Digits must be within the range of a 32-bit integer, e.g. `<MajorVersion>.<MinorVersion>.<Patch>`
    - gallery_name -- gallery name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - expand -- The expand expression to apply on the operation.
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az sig image-version wait", locals())


def list_shared(gallery_image_definition, gallery_unique_name, location, shared_to=None):
    '''
    List VM Image Versions in a gallery shared directly to your subscription or tenant (preview).

    Required Parameters:
    - gallery_image_definition -- The name of the Shared Gallery Image Definition from which the Image Versions are to be listed.
    - gallery_unique_name -- The unique name of the Shared Gallery.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.

    Optional Parameters:
    - shared_to -- The query parameter to decide what shared galleries to fetch when doing listing operations. If not specified, list by subscription id.
    '''
    return _call_az("az sig image-version list-shared", locals())


def show_shared(gallery_image_definition, gallery_image_version, gallery_unique_name, location):
    '''
    Get an image version in a gallery shared directly to your subscription or tenant (preview).

    Required Parameters:
    - gallery_image_definition -- The name of the Shared Gallery Image Definition from which the Image Versions are to be listed.
    - gallery_image_version -- The name of the gallery image version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>
    - gallery_unique_name -- The unique name of the Shared Gallery.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az sig image-version show-shared", locals())

