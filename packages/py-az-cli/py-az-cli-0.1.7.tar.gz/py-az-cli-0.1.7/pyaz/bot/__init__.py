'''
Manage Microsoft Azure Bot Service.
'''
from .. pyaz_utils import _call_az
from . import authsetting, directline, email, facebook, kik, msteams, skype, slack, sms, telegram, webchat


def create(appid, kind, name, resource_group, cmk_key_vault_key_url=None, description=None, display_name=None, echo=None, lang=None, location=None, sku=None, tags=None):
    '''
    Create a new v4 SDK bot.

    Required Parameters:
    - appid -- The Microsoft account ID (MSA ID) to be used with the bot.
    - kind -- The kind of the bot.
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - cmk_key_vault_key_url -- The key vault key url to enable Customer Managed Keys encryption
    - description -- The description of the bot.
    - display_name -- The display name of the bot. If not specified, defaults to the name of the bot.
    - echo -- Deploy an Echo Bot template to the newly created v4 Web App Bot.
    - lang -- The language to be used to create the bot.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - sku -- The Sku of the bot.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az bot create", locals())


def publish(name, resource_group, code_dir=None, keep_node_modules=None, proj_file_path=None, timeout=None):
    '''
    Publish to a bot's associated app service.

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - code_dir -- The directory to upload bot code from.
    - keep_node_modules -- Keep node_modules folder and do not run `npm install` on the App Service. This can greatly speed up publish commands for Node.js SDK bots.
    - proj_file_path -- Path to the start up project file name. (E.g. "./EchoBotWithCounter.csproj")
    - timeout -- Configurable timeout in seconds for checking the status of deployment.
    '''
    return _call_az("az bot publish", locals())


def download(name, resource_group, save_path=None):
    '''
    Download an existing bot.

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - save_path -- The directory to download bot code to.
    '''
    return _call_az("az bot download", locals())


def prepare_publish(name, proj_file_path, resource_group, sln_name, code_dir=None):
    '''
    (Maintenance mode) Add scripts to your local source code directory to be able to publish back using `az bot publish` for v3 SDK bots.

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - proj_file_path -- Path to the start up project file name. (E.g. "./EchoBotWithCounter.csproj") Required only for C#.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sln_name -- Name of the start up solution file name. Required only for C#.

    Optional Parameters:
    - code_dir -- The directory to download deployment scripts to.
    '''
    return _call_az("az bot prepare-publish", locals())


def prepare_deploy(lang, code_dir=None, proj_file_path=None):
    '''
    Add scripts/config files for publishing with `az webapp deployment`.

    Required Parameters:
    - lang -- The language or runtime of the bot.

    Optional Parameters:
    - code_dir -- The directory to place the generated deployment files in. Defaults to the current directory the command is called from.
    - proj_file_path -- The path to the .csproj file relative to --code-dir.
    '''
    return _call_az("az bot prepare-deploy", locals())


def show(name, resource_group, msbot=None):
    '''
    Get an existing bot.

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - msbot -- Show the output as JSON compatible with a .bot file.
    '''
    return _call_az("az bot show", locals())


def delete(name, resource_group):
    '''
    Delete an existing bot.

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az bot delete", locals())


def update(name, resource_group, app_insights_api_key=None, app_insights_app_id=None, app_insights_key=None, cmk_key_vault_key_url=None, cmk_off=None, description=None, display_name=None, endpoint=None, icon_url=None, sku=None, tags=None):
    '''
    Update an existing bot.

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - app_insights_api_key -- Azure Application Insights API Key used to read bot analytics data. Provide a key if you want to view analytics about your bot in the Analytics blade.
    - app_insights_app_id -- Azure Application Insights Application ID used to read bot analytics data. Provide an Id if you want to view analytics about your bot in the Analytics blade.
    - app_insights_key -- Azure Application Insights Key used to write bot analytics data. Provide a key if you want to receive bot analytics.
    - cmk_key_vault_key_url -- The key vault key url to enable Customer Managed Keys encryption
    - cmk_off -- Set encryption to Microsoft-Managed Keys
    - description -- The bot's new description.
    - display_name -- The bot's new display name.
    - endpoint -- The new endpoint of the bot. Must start with "https://"
    - icon_url -- Icon URL for bot avatar. Accepts PNG files with file size limit of 30KB.
    - sku -- The Sku of the bot.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az bot update", locals())

