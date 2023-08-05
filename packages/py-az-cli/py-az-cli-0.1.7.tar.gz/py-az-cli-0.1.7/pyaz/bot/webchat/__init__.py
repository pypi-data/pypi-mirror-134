'''
Manage the Webchat Channel on a bot.
'''
from ... pyaz_utils import _call_az

def show(name, resource_group, with_secrets=None):
    '''
    Get details of the Webchat Channel on a bot

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - with_secrets -- Show secrets in response for the channel.
    '''
    return _call_az("az bot webchat show", locals())

