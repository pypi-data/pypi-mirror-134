'''
Manage the Directline Channel on a bot.
'''
from ... pyaz_utils import _call_az

def create(name, resource_group, add_disabled=None, disablev1=None, disablev3=None, enable_enhanced_auth=None, trusted_origins=None):
    '''
    Create the DirectLine Channel on a bot with only v3 protocol enabled.

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add_disabled -- Add the channel in a disabled state.
    - disablev1 -- If true, v1 protocol will be disabled on the channel
    - disablev3 -- If true, v3 protocol will be disabled on the channel.
    - enable_enhanced_auth -- If true, enables enhanced authentication features. Must be true for --trusted-origins parameters to work.
    - trusted_origins -- Space separated Trusted Origins URLs (must use HTTPS) e.g. --trusted-origins https://mybotsite1.azurewebsites.net https://mybotsite2.azurewebsites.net
    '''
    return _call_az("az bot directline create", locals())


def update(name, resource_group, add_disabled=None, disablev1=None, disablev3=None, enable_enhanced_auth=None, trusted_origins=None):
    '''
    Update the DirectLine Channel on a bot with only v3 protocol enabled.

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add_disabled -- Add the channel in a disabled state.
    - disablev1 -- If true, v1 protocol will be disabled on the channel
    - disablev3 -- If true, v3 protocol will be disabled on the channel.
    - enable_enhanced_auth -- If true, enables enhanced authentication features. Must be true for --trusted-origins parameters to work.
    - trusted_origins -- Space separated Trusted Origins URLs (must use HTTPS) e.g. --trusted-origins https://mybotsite1.azurewebsites.net https://mybotsite2.azurewebsites.net
    '''
    return _call_az("az bot directline update", locals())


def show(name, resource_group, with_secrets=None):
    '''
    Get details of the Directline Channel on a bot

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - with_secrets -- Show secrets in response for the channel.
    '''
    return _call_az("az bot directline show", locals())


def delete(name, resource_group):
    '''
    Delete the Directline Channel on a bot

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az bot directline delete", locals())

