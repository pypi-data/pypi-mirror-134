from .... pyaz_utils import _call_az
from . import rule


def show(account_name, policy_id, resource_group=None):
    '''
    Show the properties of specified Object Replication Service Policy for storage account.

    Required Parameters:
    - account_name -- The storage account name.
    - policy_id -- The ID of object replication policy or "default" if the policy ID is unknown. Policy Id will be auto-generated when setting on destination account. Required when setting on source account.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account or-policy show", locals())


def list(account_name, resource_group=None):
    '''
    List Object Replication Service Policies associated with the specified storage account.

    Required Parameters:
    - account_name -- The storage account name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account or-policy list", locals())


def create(account_name, destination_account=None, destination_container=None, min_creation_time=None, policy=None, policy_id=None, prefix_match=None, resource_group=None, rule_id=None, source_account=None, source_container=None):
    '''
    Create Object Replication Service Policy for storage account.

    Required Parameters:
    - account_name -- The storage account name.

    Optional Parameters:
    - destination_account -- The destination storage account name or resource Id. Apply --account-name value as destination account when there is no destination account provided in --policy and --destination-account.
    - destination_container -- The destination storage container name. Required when no --policy provided.
    - min_creation_time -- Blobs created after the time will be replicated to the destination. It must be in datetime format 'yyyy-MM-ddTHH:mm:ssZ'. Example: 2020-02-19T16:05:00Z
    - policy -- The object replication policy definition between two storage accounts, in JSON format. Multiple rules can be defined in one policy.
    - policy_id -- The ID of object replication policy or "default" if the policy ID is unknown. Policy Id will be auto-generated when setting on destination account. Required when setting on source account.
    - prefix_match -- Optional. Filter the results to replicate only blobs whose names begin with the specified prefix.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_id -- Rule Id is auto-generated for each new rule on destination account. It is required for put policy on source account.
    - source_account -- The source storage account name or resource Id. Required when no --policy provided.
    - source_container -- The source storage container name. Required when no --policy provided.
    '''
    return _call_az("az storage account or-policy create", locals())


def update(account_name, add=None, destination_account=None, force_string=None, policy=None, policy_id=None, remove=None, resource_group=None, set=None, source_account=None):
    '''
    Update Object Replication Service Policy properties for storage account.

    Required Parameters:
    - account_name -- The storage account name.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - destination_account -- The destination storage account name or resource Id. Apply --account-name value as destination account when there is no destination account provided in --policy and --destination-account.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - policy -- The object replication policy definition between two storage accounts, in JSON format. Multiple rules can be defined in one policy.
    - policy_id -- The ID of object replication policy or "default" if the policy ID is unknown. Policy Id will be auto-generated when setting on destination account. Required when setting on source account.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - source_account -- The source storage account name or resource Id. Required when no --policy provided.
    '''
    return _call_az("az storage account or-policy update", locals())


def delete(account_name, policy_id, resource_group=None):
    '''
    Delete specified Object Replication Service Policy associated with the specified storage account.

    Required Parameters:
    - account_name -- The storage account name.
    - policy_id -- The ID of object replication policy or "default" if the policy ID is unknown. Policy Id will be auto-generated when setting on destination account. Required when setting on source account.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account or-policy delete", locals())

