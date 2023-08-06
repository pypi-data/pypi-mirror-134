'''
Manage Azure Resource Manager template deployment at resource group.
'''
from ... pyaz_utils import _call_az

def list(resource_group, filter=None):
    '''
    List deployments at resource group.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - filter -- Filter expression using OData notation. You can use --filter "provisioningState eq '{state}'" to filter provisioningState. To get more information, please visit https://docs.microsoft.com/rest/api/resources/deployments/listatsubscriptionscope#uri-parameters
    '''
    return _call_az("az deployment group list", locals())


def show(name, resource_group):
    '''
    Show a deployment at resource group.

    Required Parameters:
    - name -- The deployment name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az deployment group show", locals())


def delete(name, resource_group, no_wait=None):
    '''
    Delete a deployment at resource group.

    Required Parameters:
    - name -- The deployment name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az deployment group delete", locals())


def validate(resource_group, handle_extended_json_format=None, mode=None, name=None, no_prompt=None, parameters=None, query_string=None, rollback_on_error=None, template_file=None, template_spec=None, template_uri=None):
    '''
    Validate whether a template is valid at resource group.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - handle_extended_json_format -- Support to handle extended template content including multiline and comments in deployment
    - mode -- Incremental (only add resources to resource group) or Complete (remove extra resources from resource group)
    - name -- The deployment name. Default to template file base name
    - no_prompt -- The option to disable the prompt of missing parameters for ARM template. When the value is true, the prompt requiring users to provide missing parameter will be ignored. The default value is false.
    - parameters -- the deployment parameters
    - query_string -- The query string (a SAS token) to be used with the template-uri in the case of linked templates.
    - rollback_on_error -- The name of a deployment to roll back to on error, or use as a flag to roll back to the last successful deployment.
    - template_file -- a path to a template file or Bicep file in the file system
    - template_spec -- The template spec resource id.
    - template_uri -- a uri to a remote template file
    '''
    return _call_az("az deployment group validate", locals())


def create(resource_group, aux_subs=None, aux_tenants=None, confirm_with_what_if=None, handle_extended_json_format=None, mode=None, name=None, no_prompt=None, no_wait=None, parameters=None, proceed_if_no_change=None, query_string=None, rollback_on_error=None, template_file=None, template_spec=None, template_uri=None, what_if=None, what_if_exclude_change_types=None, what_if_result_format=None):
    '''
    Start a deployment at resource group.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - aux_subs -- Auxiliary subscriptions which will be used during deployment across tenants.
    - aux_tenants -- Auxiliary tenants which will be used during deployment across tenants.
    - confirm_with_what_if -- Instruct the command to run deployment What-If before executing the deployment. It then prompts you to acknowledge resource changes before it continues.
    - handle_extended_json_format -- Support to handle extended template content including multiline and comments in deployment
    - mode -- Incremental (only add resources to resource group) or Complete (remove extra resources from resource group)
    - name -- The deployment name. Default to template file base name
    - no_prompt -- The option to disable the prompt of missing parameters for ARM template. When the value is true, the prompt requiring users to provide missing parameter will be ignored. The default value is false.
    - no_wait -- Do not wait for the long-running operation to finish.
    - parameters -- the deployment parameters
    - proceed_if_no_change -- Instruct the command to execute the deployment if the What-If result contains no resource changes. Applicable when --confirm-with-what-if is set.
    - query_string -- The query string (a SAS token) to be used with the template-uri in the case of linked templates.
    - rollback_on_error -- The name of a deployment to roll back to on error, or use as a flag to roll back to the last successful deployment.
    - template_file -- a path to a template file or Bicep file in the file system
    - template_spec -- The template spec resource id.
    - template_uri -- a uri to a remote template file
    - what_if -- Instruct the command to run deployment What-If.
    - what_if_exclude_change_types -- Space-separated list of resource change types to be excluded from What-If results. Applicable when --confirm-with-what-if is set.
    - what_if_result_format -- None
    '''
    return _call_az("az deployment group create", locals())


def what_if(resource_group, aux_tenants=None, exclude_change_types=None, mode=None, name=None, no_pretty_print=None, no_prompt=None, parameters=None, query_string=None, result_format=None, template_file=None, template_spec=None, template_uri=None):
    '''
    Execute a deployment What-If operation at resource group scope.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - aux_tenants -- Auxiliary tenants which will be used during deployment across tenants.
    - exclude_change_types -- Space-separated list of resource change types to be excluded from What-If results.
    - mode -- Incremental (only add resources to resource group) or Complete (remove extra resources from resource group)
    - name -- The deployment name. Default to template file base name
    - no_pretty_print -- Disable pretty-print for What-If results. When set, the output format type will be used.
    - no_prompt -- The option to disable the prompt of missing parameters for ARM template. When the value is true, the prompt requiring users to provide missing parameter will be ignored. The default value is false.
    - parameters -- the deployment parameters
    - query_string -- The query string (a SAS token) to be used with the template-uri in the case of linked templates.
    - result_format -- None
    - template_file -- a path to a template file or Bicep file in the file system
    - template_spec -- The template spec resource id.
    - template_uri -- a uri to a remote template file
    '''
    return _call_az("az deployment group what-if", locals())


def export(name, resource_group):
    '''
    Export the template used for a deployment.

    Required Parameters:
    - name -- The deployment name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az deployment group export", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a deployment condition is met.

    Required Parameters:
    - name -- The deployment name.
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
    return _call_az("az deployment group wait", locals())


def cancel(name, resource_group):
    '''
    Cancel a deployment at resource group.

    Required Parameters:
    - name -- The deployment name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az deployment group cancel", locals())

