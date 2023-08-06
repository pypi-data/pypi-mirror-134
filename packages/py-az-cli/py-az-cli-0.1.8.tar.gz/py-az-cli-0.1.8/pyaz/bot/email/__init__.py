'''
Manage the email Channel on a bot.
'''
from ... pyaz_utils import _call_az

def create(email_address, name, password, resource_group, add_disabled=None):
    '''
    Create the Email Channel on a bot.

    Required Parameters:
    - email_address -- The email address for the bot.
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - password -- The email password for the bot.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add_disabled -- Add the channel in a disabled state
    '''
    return _call_az("az bot email create", locals())


def show(name, resource_group, with_secrets=None):
    '''
    Get details of the email Channel on a bot

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - with_secrets -- Show secrets in response for the channel.
    '''
    return _call_az("az bot email show", locals())


def delete(name, resource_group):
    '''
    Delete the email Channel on a bot

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az bot email delete", locals())

