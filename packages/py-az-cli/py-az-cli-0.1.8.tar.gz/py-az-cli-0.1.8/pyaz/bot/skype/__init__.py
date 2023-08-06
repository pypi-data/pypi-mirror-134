'''
Manage the Skype Channel on a bot.
'''
from ... pyaz_utils import _call_az

def create(name, resource_group, add_disabled=None, calling_web_hook=None, enable_calling=None, enable_groups=None, enable_media_cards=None, enable_messaging=None, enable_screen_sharing=None, enable_video=None, groups_mode=None):
    '''
    Create the Skype Channel on a bot.

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add_disabled -- Add the channel in a disabled state.
    - calling_web_hook -- The calling web hook to use on Skype.
    - enable_calling -- Enable calling on Skype.
    - enable_groups -- Enable groups on Skype.
    - enable_media_cards -- Enable media cards on Skype.
    - enable_messaging -- Enable messaging on Skype.
    - enable_screen_sharing -- Enable screen sharing on Skype.
    - enable_video -- Enable video on Skype.
    - groups_mode -- select groups mode on Skype.
    '''
    return _call_az("az bot skype create", locals())


def show(name, resource_group, with_secrets=None):
    '''
    Get details of the Skype Channel on a bot

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - with_secrets -- Show secrets in response for the channel.
    '''
    return _call_az("az bot skype show", locals())


def delete(name, resource_group):
    '''
    Delete the Skype Channel on a bot

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az bot skype delete", locals())

