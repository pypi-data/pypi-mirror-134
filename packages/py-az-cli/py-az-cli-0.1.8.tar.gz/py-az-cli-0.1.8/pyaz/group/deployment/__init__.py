'''
Manage Azure Resource Manager deployments.
'''
from ... pyaz_utils import _call_az
from . import operation


def create(resource_group, aux_subs=None, aux_tenants=None, handle_extended_json_format=None, mode=None, name=None, no_prompt=None, no_wait=None, parameters=None, rollback_on_error=None, template_file=None, template_uri=None):
    '''
    Start a deployment.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - aux_subs -- Auxiliary subscriptions which will be used during deployment across tenants.
    - aux_tenants -- Auxiliary tenants which will be used during deployment across tenants.
    - handle_extended_json_format -- Support to handle extended template content including multiline and comments in deployment
    - mode -- Incremental (only add resources to resource group) or Complete (remove extra resources from resource group)
    - name -- The deployment name. Default to template file base name
    - no_prompt -- The option to disable the prompt of missing parameters for ARM template. When the value is true, the prompt requiring users to provide missing parameter will be ignored. The default value is false.
    - no_wait -- Do not wait for the long-running operation to finish.
    - parameters -- the deployment parameters
    - rollback_on_error -- The name of a deployment to roll back to on error, or use as a flag to roll back to the last successful deployment.
    - template_file -- a path to a template file or Bicep file in the file system
    - template_uri -- a uri to a remote template file
    '''
    return _call_az("az group deployment create", locals())


def list(resource_group, filter=None, top=None):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - filter -- The filter to apply on the operation. For example, you can use $filter=provisioningState eq '{state}'.
    - top -- The number of results to get. If null is passed, returns all deployments.
    '''
    return _call_az("az group deployment list", locals())


def show(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The deployment name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az group deployment show", locals())


def delete(name, resource_group, no_wait=None):
    '''
    

    Required Parameters:
    - name -- The deployment name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az group deployment delete", locals())


def validate(resource_group, handle_extended_json_format=None, mode=None, no_prompt=None, parameters=None, rollback_on_error=None, template_file=None, template_uri=None):
    '''
    Validate whether a template is syntactically correct.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - handle_extended_json_format -- Support to handle extended template content including multiline and comments in deployment
    - mode -- Incremental (only add resources to resource group) or Complete (remove extra resources from resource group)
    - no_prompt -- The option to disable the prompt of missing parameters for ARM template. When the value is true, the prompt requiring users to provide missing parameter will be ignored. The default value is false.
    - parameters -- the deployment parameters
    - rollback_on_error -- The name of a deployment to roll back to on error, or use as a flag to roll back to the last successful deployment.
    - template_file -- a path to a template file or Bicep file in the file system
    - template_uri -- a uri to a remote template file
    '''
    return _call_az("az group deployment validate", locals())


def export(name, resource_group):
    '''
    Export the template used for a deployment.

    Required Parameters:
    - name -- The deployment name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az group deployment export", locals())


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
    return _call_az("az group deployment wait", locals())


def cancel(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The deployment name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az group deployment cancel", locals())

