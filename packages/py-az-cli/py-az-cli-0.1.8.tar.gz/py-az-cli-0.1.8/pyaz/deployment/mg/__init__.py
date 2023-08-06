'''
Manage Azure Resource Manager template deployment at management group.
'''
from ... pyaz_utils import _call_az

def list(management_group_id, filter=None):
    '''
    List deployments at management group.

    Required Parameters:
    - management_group_id -- The management group id.

    Optional Parameters:
    - filter -- Filter expression using OData notation. You can use --filter "provisioningState eq '{state}'" to filter provisioningState. To get more information, please visit https://docs.microsoft.com/rest/api/resources/deployments/listatsubscriptionscope#uri-parameters
    '''
    return _call_az("az deployment mg list", locals())


def show(management_group_id, name):
    '''
    Show a deployment at management group.

    Required Parameters:
    - management_group_id -- The management group id.
    - name -- The deployment name.
    '''
    return _call_az("az deployment mg show", locals())


def delete(management_group_id, name, no_wait=None):
    '''
    Delete a deployment at management group.

    Required Parameters:
    - management_group_id -- The management group id.
    - name -- The deployment name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az deployment mg delete", locals())


def validate(location, management_group_id, handle_extended_json_format=None, name=None, no_prompt=None, parameters=None, query_string=None, template_file=None, template_spec=None, template_uri=None):
    '''
    Validate whether a template is valid at management group.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - management_group_id -- The management group id.

    Optional Parameters:
    - handle_extended_json_format -- Support to handle extended template content including multiline and comments in deployment
    - name -- The deployment name. Default to template file base name
    - no_prompt -- The option to disable the prompt of missing parameters for ARM template. When the value is true, the prompt requiring users to provide missing parameter will be ignored. The default value is false.
    - parameters -- the deployment parameters
    - query_string -- The query string (a SAS token) to be used with the template-uri in the case of linked templates.
    - template_file -- a path to a template file or Bicep file in the file system
    - template_spec -- The template spec resource id.
    - template_uri -- a uri to a remote template file
    '''
    return _call_az("az deployment mg validate", locals())


def create(location, management_group_id, confirm_with_what_if=None, handle_extended_json_format=None, name=None, no_prompt=None, no_wait=None, parameters=None, proceed_if_no_change=None, query_string=None, template_file=None, template_spec=None, template_uri=None, what_if=None, what_if_exclude_change_types=None, what_if_result_format=None):
    '''
    Start a deployment at management group.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - management_group_id -- The management group id.

    Optional Parameters:
    - confirm_with_what_if -- Instruct the command to run deployment What-If before executing the deployment. It then prompts you to acknowledge resource changes before it continues.
    - handle_extended_json_format -- Support to handle extended template content including multiline and comments in deployment
    - name -- The deployment name. Default to template file base name
    - no_prompt -- The option to disable the prompt of missing parameters for ARM template. When the value is true, the prompt requiring users to provide missing parameter will be ignored. The default value is false.
    - no_wait -- Do not wait for the long-running operation to finish.
    - parameters -- the deployment parameters
    - proceed_if_no_change -- Instruct the command to execute the deployment if the What-If result contains no resource changes. Applicable when --confirm-with-what-if is set.
    - query_string -- The query string (a SAS token) to be used with the template-uri in the case of linked templates.
    - template_file -- a path to a template file or Bicep file in the file system
    - template_spec -- The template spec resource id.
    - template_uri -- a uri to a remote template file
    - what_if -- Instruct the command to run deployment What-If.
    - what_if_exclude_change_types -- Space-separated list of resource change types to be excluded from What-If results. Applicable when --confirm-with-what-if is set.
    - what_if_result_format -- None
    '''
    return _call_az("az deployment mg create", locals())


def what_if(location, management_group_id, exclude_change_types=None, name=None, no_pretty_print=None, no_prompt=None, parameters=None, query_string=None, result_format=None, template_file=None, template_spec=None, template_uri=None):
    '''
    Execute a deployment What-If operation at management group scope.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - management_group_id -- The management group id.

    Optional Parameters:
    - exclude_change_types -- Space-separated list of resource change types to be excluded from What-If results.
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
    return _call_az("az deployment mg what-if", locals())


def export(management_group_id, name):
    '''
    Export the template used for a deployment.

    Required Parameters:
    - management_group_id -- The management group id.
    - name -- The deployment name.
    '''
    return _call_az("az deployment mg export", locals())


def wait(management_group_id, name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a deployment condition is met.

    Required Parameters:
    - management_group_id -- The management group id.
    - name -- The deployment name.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az deployment mg wait", locals())


def cancel(management_group_id, name):
    '''
    Cancel a deployment at management group.

    Required Parameters:
    - management_group_id -- The management group id.
    - name -- The deployment name.
    '''
    return _call_az("az deployment mg cancel", locals())

