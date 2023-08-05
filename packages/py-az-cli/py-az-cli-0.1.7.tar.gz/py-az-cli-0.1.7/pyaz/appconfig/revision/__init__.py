'''
Manage revisions for key-values stored in an App Configuration.
'''
from ... pyaz_utils import _call_az

def list(all=None, auth_mode=None, connection_string=None, datetime=None, endpoint=None, fields=None, key=None, label=None, name=None, top=None):
    '''
    Lists revision history of key-values.

    Optional Parameters:
    - all -- List all items.
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - datetime -- Format: "YYYY-MM-DDThh:mm:ssZ". If no time zone specified, use UTC by default.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - fields -- Space-separated customized output fields.
    - key -- If no key specified, return all keys by default. Support star sign as filters, for instance abc* means keys with abc as prefix.
    - label -- If no label specified, list all labels. Support star sign as filters, for instance abc* means labels with abc as prefix. Use '\0' for null label.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - top -- Maximum number of items to return. Must be a positive integer. Default to 100.
    '''
    return _call_az("az appconfig revision list", locals())

