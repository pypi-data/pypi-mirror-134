from .... pyaz_utils import _call_az

def show(name, resource_group):
    '''
    Gets backup related properties of the Recovery Services vault.

    Required Parameters:
    - name -- Name of the Recovery services vault.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az backup vault backup-properties show", locals())


def set(name, resource_group, backup_storage_redundancy=None, cross_region_restore_flag=None, soft_delete_feature_state=None):
    '''
    Sets backup related properties of the Recovery Services vault.

    Required Parameters:
    - name -- Name of the Recovery services vault.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - backup_storage_redundancy -- Set backup storage properties for a Recovery Services vault.
    - cross_region_restore_flag -- Set cross-region-restore feature state for a Recovery Services Vault. Default: False.
    - soft_delete_feature_state -- Set soft-delete feature state for a Recovery Services Vault.
    '''
    return _call_az("az backup vault backup-properties set", locals())

