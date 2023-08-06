'''
Manage OAuth connection settings on a bot.
'''
from ... pyaz_utils import _call_az

def list(name, resource_group):
    '''
    Show all OAuth connection settings on a bot.

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az bot authsetting list", locals())


def show(name, resource_group, setting_name):
    '''
    Show details of an OAuth connection setting on a bot.

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - setting_name -- Name of the oauth connection setting.
    '''
    return _call_az("az bot authsetting show", locals())


def delete(name, resource_group, setting_name):
    '''
    Delete an OAuth connection setting on a bot.

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - setting_name -- Name of the oauth connection setting.
    '''
    return _call_az("az bot authsetting delete", locals())


def create(client_id, client_secret, name, provider_scope_string, resource_group, service, setting_name, parameters=None):
    '''
    Create an OAuth connection setting on a bot.

    Required Parameters:
    - client_id -- Client ID associated with the service provider setting.
    - client_secret -- Client secret associated with the service provider setting.
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - provider_scope_string -- The scope string associated with the service provider setting.The string should be delimited as needed for the service provider.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service -- Name of the service provider. For a list of all service providers, use `az bot connection listserviceproviders`.
    - setting_name -- Name of the oauth connection setting.

    Optional Parameters:
    - parameters -- Parameter values for service provider parameters. Usage: --parameters key=value key1=value1.
    '''
    return _call_az("az bot authsetting create", locals())


def list_providers(provider_name=None):
    '''
    List details for all service providers available for creating OAuth connection settings.

    Optional Parameters:
    - provider_name -- Service provider name for which to fetch details.
    '''
    return _call_az("az bot authsetting list-providers", locals())

