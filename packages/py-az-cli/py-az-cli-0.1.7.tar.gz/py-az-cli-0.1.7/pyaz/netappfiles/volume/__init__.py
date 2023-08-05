'''
Manage Azure NetApp Files (ANF) Volume Resources.
'''
from ... pyaz_utils import _call_az
from . import backup, export_policy, replication


def show(account_name, pool_name, resource_group, volume_name):
    '''
    Get the specified ANF volume.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles volume show", locals())


def list(account_name, pool_name, resource_group):
    '''
    List the ANF Pools for the specified account.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az netappfiles volume list", locals())


def delete(account_name, pool_name, resource_group, volume_name):
    '''
    Delete the specified ANF volume.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles volume delete", locals())


def create(account_name, file_path, location, pool_name, resource_group, usage_threshold, vnet, volume_name, allowed_clients=None, avs_data_store=None, backup_enabled=None, backup_id=None, backup_policy_id=None, chown_mode=None, cifs=None, cool_access=None, coolness_period=None, default_group_quota=None, default_user_quota=None, encryption_key_source=None, endpoint_type=None, has_root_access=None, is_def_quota_enabled=None, kerberos5_r=None, kerberos5_rw=None, kerberos5i_r=None, kerberos5i_rw=None, kerberos5p_r=None, kerberos5p_rw=None, kerberos_enabled=None, ldap_enabled=None, network_features=None, policy_enforced=None, protocol_types=None, remote_volume_resource_id=None, replication_schedule=None, rule_index=None, security_style=None, service_level=None, smb_continuously_avl=None, smb_encryption=None, snapshot_dir_visible=None, snapshot_id=None, snapshot_policy_id=None, subnet=None, tags=None, throughput_mibps=None, unix_permissions=None, unix_read_only=None, unix_read_write=None, vault_id=None, volume_type=None):
    '''
    Create a new Azure NetApp Files (ANF) volume. Export policies are applied with the subgroup commands but note that volumes are always created with a default export policy

    Required Parameters:
    - account_name -- Name of the ANF account.
    - file_path -- None
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - usage_threshold -- Required. Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB. Specified in bytes.
    - vnet -- None
    - volume_name -- Name of the ANF volume.

    Optional Parameters:
    - allowed_clients -- None
    - avs_data_store -- Specifies whether the volume is enabled for Azure VMware Solution (AVS) datastore purpose. Possible values include: "Enabled", "Disabled". Default value: "Disabled".
    - backup_enabled -- None
    - backup_id -- UUID v4 or resource identifier used to identify the Backup.
    - backup_policy_id -- None
    - chown_mode -- None
    - cifs -- None
    - cool_access -- Specifies whether Cool Access(tiering) is enabled for the volume.
    - coolness_period -- Specifies the number of days after which data that is not accessed by clients will be tiered.
    - default_group_quota -- None
    - default_user_quota -- None
    - encryption_key_source -- Encryption Key Source. Possible values are: 'Microsoft.NetApp'.
    - endpoint_type -- None
    - has_root_access -- None
    - is_def_quota_enabled -- None
    - kerberos5_r -- None
    - kerberos5_rw -- None
    - kerberos5i_r -- None
    - kerberos5i_rw -- None
    - kerberos5p_r -- None
    - kerberos5p_rw -- None
    - kerberos_enabled -- Describe if a volume is KerberosEnabled. To be use with swagger version 2020-05-01 or later.
    - ldap_enabled -- Specifies whether LDAP is enabled or not for a given NFS volume.
    - network_features -- Basic network, or Standard features available to the volume. Possible values include: "Basic", "Standard". Default value: "Basic".
    - policy_enforced -- None
    - protocol_types -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - remote_volume_resource_id -- None
    - replication_schedule -- None
    - rule_index -- None
    - security_style -- The security style of volume, default unix, defaults to ntfs for dual protocol or CIFS protocol. Possible values include: "ntfs", "unix". Default value: "unix".
    - service_level -- Service level
    - smb_continuously_avl -- None
    - smb_encryption -- Enables encryption for in-flight smb3 data. Only applicable for SMB/DualProtocol volume. To be used with swagger version 2020-08-01 or later.
    - snapshot_dir_visible -- None
    - snapshot_id -- UUID v4 or resource identifier used to identify the Snapshot.
    - snapshot_policy_id -- None
    - subnet -- None
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - throughput_mibps -- Maximum throughput in Mibps that can be achieved by this volume.
    - unix_permissions -- UNIX permissions for NFS volume accepted in octal 4 digit format. First digit selects the set user ID(4), set group ID (2) and sticky (1) attributes. Second digit selects permission for the owner of the file: read (4), write (2) and execute (1). Third selects permissions for other users in the same group. the fourth for other users not in the group. 0755 - gives read/write/execute permissions to owner and read/execute to group and other users.
    - unix_read_only -- None
    - unix_read_write -- None
    - vault_id -- None
    - volume_type -- What type of volume is this. For destination volumes in Cross Region Replication, set type to DataProtection.
    '''
    return _call_az("az netappfiles volume create", locals())


def update(account_name, pool_name, resource_group, volume_name, add=None, backup_enabled=None, backup_policy_id=None, default_group_quota=None, default_user_quota=None, force_string=None, is_def_quota_enabled=None, policy_enforced=None, remove=None, service_level=None, set=None, snapshot_policy_id=None, tags=None, throughput_mibps=None, usage_threshold=None, vault_id=None):
    '''
    Update the specified ANF volume with the values provided. Unspecified values will remain unchanged. Export policies are amended/created with the subgroup commands

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - backup_enabled -- None
    - backup_policy_id -- None
    - default_group_quota -- None
    - default_user_quota -- None
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - is_def_quota_enabled -- None
    - policy_enforced -- None
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - service_level -- Service level
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - snapshot_policy_id -- None
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - throughput_mibps -- Maximum throughput in Mibps that can be achieved by this volume.
    - usage_threshold -- Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB. Specified in bytes.
    - vault_id -- None
    '''
    return _call_az("az netappfiles volume update", locals())


def revert(account_name, pool_name, resource_group, snapshot_id, volume_name):
    '''
    Revert a volume to one of its snapshots.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - snapshot_id -- Resource id of the snapshot
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles volume revert", locals())


def pool_change(account_name, new_pool_resource_id, pool_name, resource_group, volume_name):
    '''
    Change pool for an Azure NetApp Files (ANF) volume.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - new_pool_resource_id -- Resource id of the new pool
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles volume pool-change", locals())

