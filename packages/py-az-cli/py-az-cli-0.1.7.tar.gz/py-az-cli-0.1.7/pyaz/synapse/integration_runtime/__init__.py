from ... pyaz_utils import _call_az
from . import managed, self_hosted


def list(resource_group, workspace_name):
    '''
    List integration runtimes.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse integration-runtime list", locals())


def show(name, resource_group, workspace_name, if_none_match=None):
    '''
    Get an integration runtime.

    Required Parameters:
    - name -- The integration runtime name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - if_none_match -- ETag of the integration runtime entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned.
    '''
    return _call_az("az synapse integration-runtime show", locals())


def create(name, resource_group, type, workspace_name, compute_type=None, core_count=None, description=None, if_match=None, location=None, no_wait=None, time_to_live=None):
    '''
    Create an integration runtime.

    Required Parameters:
    - name -- The integration runtime name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - type -- The integration runtime type.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - compute_type -- Compute type of the data flow cluster which will execute data flow job.
    - core_count -- Core count of the data flow cluster which will execute data flow job.
    - description -- The integration runtime description.
    - if_match -- ETag of the integration runtime entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
    - location -- The integration runtime location.
    - no_wait -- Do not wait for the long-running operation to finish.
    - time_to_live -- Time to live (in minutes) setting of the data flow cluster which will execute data flow job.
    '''
    return _call_az("az synapse integration-runtime create", locals())


def delete(name, resource_group, workspace_name, no_wait=None, yes=None):
    '''
    Delete an integration runtime.

    Required Parameters:
    - name -- The integration runtime name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse integration-runtime delete", locals())


def update(auto_update, name, resource_group, update_delay_offset, workspace_name):
    '''
    Update an integration runtime.

    Required Parameters:
    - auto_update -- Enable or disable the self-hosted integration runtime auto-update.
    - name -- The integration runtime name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - update_delay_offset -- The time of the day for the self-hosted integration runtime auto-update.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse integration-runtime update", locals())


def start(name, resource_group, workspace_name, no_wait=None):
    '''
    start an SSIS integration runtime.

    Required Parameters:
    - name -- The integration runtime name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse integration-runtime start", locals())


def stop(name, resource_group, workspace_name, no_wait=None, yes=None):
    '''
    stop an SSIS integration runtime.

    Required Parameters:
    - name -- The integration runtime name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse integration-runtime stop", locals())


def upgrade(name, resource_group, workspace_name):
    '''
    Upgrade self-hosted integration runtime.

    Required Parameters:
    - name -- The integration runtime name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse integration-runtime upgrade", locals())


def list_auth_key(name, resource_group, workspace_name):
    '''
    Get keys for a self-hosted integration runtime.

    Required Parameters:
    - name -- The integration runtime name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse integration-runtime list-auth-key", locals())


def regenerate_auth_key(name, resource_group, workspace_name, key_name=None):
    '''
    Regenerate self-hosted integration runtime key.

    Required Parameters:
    - name -- The integration runtime name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - key_name -- The name of the authentication key to regenerate.
    '''
    return _call_az("az synapse integration-runtime regenerate-auth-key", locals())


def get_monitoring_data(name, resource_group, workspace_name):
    '''
    Get metric data for a self-hosted integration runtime.

    Required Parameters:
    - name -- The integration runtime name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse integration-runtime get-monitoring-data", locals())


def sync_credentials(name, resource_group, workspace_name):
    '''
    Synchronize credentials among integration runtime nodes.

    Required Parameters:
    - name -- The integration runtime name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse integration-runtime sync-credentials", locals())


def get_connection_info(name, resource_group, workspace_name):
    '''
    Get the integration runtime connection infomation.

    Required Parameters:
    - name -- The integration runtime name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse integration-runtime get-connection-info", locals())


def get_status(name, resource_group, workspace_name):
    '''
    Gets detailed status information for an integration runtime.

    Required Parameters:
    - name -- The integration runtime name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse integration-runtime get-status", locals())


def wait(name, resource_group, workspace_name, created=None, custom=None, deleted=None, exists=None, if_none_match=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of a integration runtime is met.

    Required Parameters:
    - name -- The integration runtime name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - if_none_match -- ETag of the integration runtime entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned.
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az synapse integration-runtime wait", locals())

