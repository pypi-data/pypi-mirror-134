'''
Manage webhooks for Azure Container Registries.
'''
from ... pyaz_utils import _call_az

def list(registry, resource_group=None):
    '''
    List all of the webhooks for an Azure Container Registry.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr webhook list", locals())


def create(actions, name, registry, uri, headers=None, location=None, resource_group=None, scope=None, status=None, tags=None):
    '''
    Create a webhook for an Azure Container Registry.

    Required Parameters:
    - actions -- Space-separated list of actions that trigger the webhook to post notifications.
    - name -- The name of the webhook
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`
    - uri -- The service URI for the webhook to post notifications.

    Optional Parameters:
    - headers -- Space-separated custom headers in 'key[=value]' format that will be added to the webhook notifications. Use '' to clear existing headers.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scope -- The scope of repositories where the event can be triggered. For example, 'foo:*' means events for all tags under repository 'foo'. 'foo:bar' means events for 'foo:bar' only. 'foo' is equivalent to 'foo:latest'. Empty means events for all repositories.
    - status -- Indicates whether the webhook is enabled.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az acr webhook create", locals())


def delete(name, registry, resource_group=None):
    '''
    Delete a webhook from an Azure Container Registry.

    Required Parameters:
    - name -- The name of the webhook
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr webhook delete", locals())


def show(name, registry, resource_group=None):
    '''
    Get the details of a webhook.

    Required Parameters:
    - name -- The name of the webhook
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr webhook show", locals())


def get_config(name, registry, resource_group=None):
    '''
    Get the service URI and custom headers for the webhook.

    Required Parameters:
    - name -- The name of the webhook
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr webhook get-config", locals())


def list_events(name, registry, resource_group=None):
    '''
    List recent events for a webhook.

    Required Parameters:
    - name -- The name of the webhook
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr webhook list-events", locals())


def ping(name, registry, resource_group=None):
    '''
    Trigger a ping event for a webhook.

    Required Parameters:
    - name -- The name of the webhook
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr webhook ping", locals())


def update(name, registry, actions=None, add=None, force_string=None, headers=None, remove=None, resource_group=None, scope=None, set=None, status=None, tags=None, uri=None):
    '''
    Update a webhook.

    Required Parameters:
    - name -- The name of the webhook
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - actions -- Space-separated list of actions that trigger the webhook to post notifications.
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - headers -- Space-separated custom headers in 'key[=value]' format that will be added to the webhook notifications. Use '' to clear existing headers.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scope -- The scope of repositories where the event can be triggered. For example, 'foo:*' means events for all tags under repository 'foo'. 'foo:bar' means events for 'foo:bar' only. 'foo' is equivalent to 'foo:latest'. Empty means events for all repositories.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - status -- Indicates whether the webhook is enabled.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - uri -- The service URI for the webhook to post notifications.
    '''
    return _call_az("az acr webhook update", locals())

