from ..... pyaz_utils import _call_az

def show(account_name, policy_id, rule_id, resource_group=None):
    '''
    Show the properties of specified rule in Object Replication Service Policy.

    Required Parameters:
    - account_name -- The storage account name.
    - policy_id -- The ID of object replication policy or "default" if the policy ID is unknown. Policy Id will be auto-generated when setting on destination account. Required when setting on source account.
    - rule_id -- Rule Id is auto-generated for each new rule on destination account. It is required for put policy on source account.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account or-policy rule show", locals())


def list(account_name, policy_id, resource_group=None):
    '''
    List all the rules in the specified Object Replication Service Policy.

    Required Parameters:
    - account_name -- The storage account name.
    - policy_id -- The ID of object replication policy or "default" if the policy ID is unknown. Policy Id will be auto-generated when setting on destination account. Required when setting on source account.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account or-policy rule list", locals())


def add(account_name, destination_container, policy_id, source_container, min_creation_time=None, prefix_match=None, resource_group=None):
    '''
    Add rule to the specified Object Replication Service Policy.

    Required Parameters:
    - account_name -- The storage account name.
    - destination_container -- The destination storage container name.
    - policy_id -- The ID of object replication policy or "default" if the policy ID is unknown. Policy Id will be auto-generated when setting on destination account. Required when setting on source account.
    - source_container -- The source storage container name.

    Optional Parameters:
    - min_creation_time -- Blobs created after the time will be replicated to the destination. It must be in datetime format 'yyyy-MM-ddTHH:mm:ssZ'. Example: 2020-02-19T16:05:00Z
    - prefix_match -- Optional. Filter the results to replicate only blobs whose names begin with the specified prefix.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account or-policy rule add", locals())


def update(account_name, policy_id, rule_id, destination_container=None, min_creation_time=None, prefix_match=None, resource_group=None, source_container=None):
    '''
    Update rule properties to Object Replication Service Policy.

    Required Parameters:
    - account_name -- The storage account name.
    - policy_id -- The ID of object replication policy or "default" if the policy ID is unknown. Policy Id will be auto-generated when setting on destination account. Required when setting on source account.
    - rule_id -- Rule Id is auto-generated for each new rule on destination account. It is required for put policy on source account.

    Optional Parameters:
    - destination_container -- The destination storage container name.
    - min_creation_time -- Blobs created after the time will be replicated to the destination. It must be in datetime format 'yyyy-MM-ddTHH:mm:ssZ'. Example: 2020-02-19T16:05:00Z
    - prefix_match -- Optional. Filter the results to replicate only blobs whose names begin with the specified prefix.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source_container -- The source storage container name.
    '''
    return _call_az("az storage account or-policy rule update", locals())


def remove(account_name, policy_id, rule_id, resource_group=None):
    '''
    Remove the specified rule from the specified Object Replication Service Policy.

    Required Parameters:
    - account_name -- The storage account name.
    - policy_id -- The ID of object replication policy or "default" if the policy ID is unknown. Policy Id will be auto-generated when setting on destination account. Required when setting on source account.
    - rule_id -- Rule Id is auto-generated for each new rule on destination account. It is required for put policy on source account.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account or-policy rule remove", locals())

