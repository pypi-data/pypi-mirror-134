'''
Manage the Kik Channel on a bot.
'''
from ... pyaz_utils import _call_az

def create(key, name, resource_group, user_name, add_disabled=None, is_validated=None):
    '''
    Create the Kik Channel on a bot.

    Required Parameters:
    - key -- The API key for the Kik account.
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - user_name -- Kik user name.

    Optional Parameters:
    - add_disabled -- Add the channel in a disabled state.
    - is_validated -- Whether or not the Kik account has been validated for use with the bot.
    '''
    return _call_az("az bot kik create", locals())


def show(name, resource_group, with_secrets=None):
    '''
    Get details of the Kik Channel on a bot

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - with_secrets -- Show secrets in response for the channel.
    '''
    return _call_az("az bot kik show", locals())


def delete(name, resource_group):
    '''
    Delete the Kik Channel on a bot

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az bot kik delete", locals())

