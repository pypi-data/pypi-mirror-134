'''
Manage the Slack Channel on a bot.
'''
from ... pyaz_utils import _call_az

def create(client_id, client_secret, name, resource_group, verification_token, add_disabled=None, landing_page_url=None):
    '''
    Create the Slack Channel on a bot.

    Required Parameters:
    - client_id -- The client ID from Slack.
    - client_secret -- The client secret from Slack.
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - verification_token -- The verification token from Slack.

    Optional Parameters:
    - add_disabled -- Add the channel in a disabled state.
    - landing_page_url -- The landing page url to redirect to after login.
    '''
    return _call_az("az bot slack create", locals())


def show(name, resource_group, with_secrets=None):
    '''
    Get details of the Slack Channel on a bot

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - with_secrets -- Show secrets in response for the channel.
    '''
    return _call_az("az bot slack show", locals())


def delete(name, resource_group):
    '''
    Delete the Slack Channel on a bot

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az bot slack delete", locals())

