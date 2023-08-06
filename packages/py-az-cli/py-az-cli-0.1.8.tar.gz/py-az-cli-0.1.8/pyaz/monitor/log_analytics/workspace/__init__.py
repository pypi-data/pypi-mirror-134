from .... pyaz_utils import _call_az
from . import data_export, linked_service, linked_storage, pack, saved_search, table


def create(resource_group, workspace_name, capacity_reservation_level=None, ingestion_access=None, location=None, no_wait=None, query_access=None, quota=None, retention_time=None, sku=None, tags=None):
    '''
    Create a workspace instance

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.

    Optional Parameters:
    - capacity_reservation_level -- The capacity reservation level for this workspace, when CapacityReservation sku is selected. The maximum value is 1000 and must be in multiples of 100. If you want to increase the limit, please contact LAIngestionRate@microsoft.com.
    - ingestion_access -- The public network access type to access workspace ingestion.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - query_access -- The public network access type to access workspace query.
    - quota -- The workspace daily quota for ingestion in gigabytes. The minimum value is 0.023 and default is -1 which means unlimited.
    - retention_time -- The workspace data retention in days.
    - sku -- The supported value: PerGB2018, CapacityReservation.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az monitor log-analytics workspace create", locals())


def update(resource_group, workspace_name, add=None, capacity_reservation_level=None, force_string=None, ingestion_access=None, query_access=None, quota=None, remove=None, retention_time=None, set=None, tags=None):
    '''
    Update a workspace instance

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - capacity_reservation_level -- The capacity reservation level for this workspace, when CapacityReservation sku is selected. The maximum value is 1000 and must be in multiples of 100. If you want to increase the limit, please contact LAIngestionRate@microsoft.com.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - ingestion_access -- The public network access type to access workspace ingestion.
    - query_access -- The public network access type to access workspace query.
    - quota -- The workspace daily quota for ingestion in gigabytes. The minimum value is 0.023 and default is -1 which means unlimited.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - retention_time -- The workspace data retention in days.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az monitor log-analytics workspace update", locals())


def show(resource_group, workspace_name):
    '''
    Show a workspace instance.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace show", locals())


def delete(resource_group, workspace_name, force=None, yes=None):
    '''
    Delete a workspace instance.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.

    Optional Parameters:
    - force -- Deletes the workspace without the recovery option. A workspace that was deleted with this flag cannot be recovered.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az monitor log-analytics workspace delete", locals())


def list(resource_group=None):
    '''
    Get a list of workspaces under a resource group or a subscription.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor log-analytics workspace list", locals())


def list_deleted_workspaces(resource_group=None):
    '''
    Get a list of deleted workspaces that can be recovered in a subscription or a resource group.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor log-analytics workspace list-deleted-workspaces", locals())


def recover(workspace_name, no_wait=None, resource_group=None):
    '''
    Recover a workspace in a soft-delete state within 14 days.

    Required Parameters:
    - workspace_name -- Name of the Log Analytics Workspace.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor log-analytics workspace recover", locals())


def get_schema(resource_group, workspace_name):
    '''
    Get the schema for a given workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace get-schema", locals())


def list_usages(resource_group, workspace_name):
    '''
    Get a list of usage metrics for a workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace list-usages", locals())


def list_management_groups(resource_group, workspace_name):
    '''
    Get a list of management groups connected to a workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace list-management-groups", locals())


def get_shared_keys(resource_group, workspace_name):
    '''
    Get the shared keys for a workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace get-shared-keys", locals())

