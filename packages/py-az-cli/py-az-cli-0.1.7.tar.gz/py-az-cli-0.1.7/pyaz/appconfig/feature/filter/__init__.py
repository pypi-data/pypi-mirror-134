'''
Manage filters associated with feature flags stored in an App Configuration.
'''
from .... pyaz_utils import _call_az

def add(filter_name, auth_mode=None, connection_string=None, endpoint=None, feature=None, filter_parameters=None, index=None, key=None, label=None, name=None, yes=None):
    '''
    Add a filter to a feature flag.

    Required Parameters:
    - filter_name -- Name of the filter to be added.

    Optional Parameters:
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - feature -- Name of the feature to which you want to add the filter. If the feature flag key is different from the default key, provide the `--key` argument instead.
    - filter_parameters -- Space-separated filter parameters in 'name[=value]' format. The value must be an escaped JSON string.
    - index -- Zero-based index in the list of filters where you want to insert the new filter. If no index is specified or index is invalid, filter will be added to the end of the list.
    - key -- Key of the feature flag. Key must start with the ".appconfig.featureflag/" prefix. Key cannot contain the "%" character. If both key and feature arguments are provided, only key will be used. Default key is the reserved prefix ".appconfig.featureflag/" + feature name.
    - label -- If no label specified, add to the feature flag with null label by default.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az appconfig feature filter add", locals())


def delete(all=None, auth_mode=None, connection_string=None, endpoint=None, feature=None, filter_name=None, index=None, key=None, label=None, name=None, yes=None):
    '''
    Delete a filter from a feature flag.

    Optional Parameters:
    - all -- Delete all filters associated with a feature flag.
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - feature -- Name of the feature from which you want to delete the filter. If the feature flag key is different from the default key, provide the `--key` argument instead.
    - filter_name -- Name of the filter to be deleted.
    - index -- Zero-based index of the filter to be deleted in case there are multiple instances with same filter name.
    - key -- Key of the feature flag. Key must start with the ".appconfig.featureflag/" prefix. Key cannot contain the "%" character. If both key and feature arguments are provided, only key will be used. Default key is the reserved prefix ".appconfig.featureflag/" + feature name.
    - label -- If no label specified, delete from the feature flag with null label by default.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az appconfig feature filter delete", locals())


def show(filter_name, auth_mode=None, connection_string=None, endpoint=None, feature=None, index=None, key=None, label=None, name=None):
    '''
    Show filters of a feature flag.

    Required Parameters:
    - filter_name -- Name of the filter to be displayed.

    Optional Parameters:
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - feature -- Name of the feature which contains the filter. If the feature flag key is different from the default key, provide the `--key` argument instead.
    - index -- Zero-based index of the filter to be displayed in case there are multiple instances with same filter name.
    - key -- Key of the feature flag. Key must start with the ".appconfig.featureflag/" prefix. Key cannot contain the "%" character. If both key and feature arguments are provided, only key will be used. Default key is the reserved prefix ".appconfig.featureflag/" + feature name.
    - label -- If no label specified, show the feature flag with null label by default.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    '''
    return _call_az("az appconfig feature filter show", locals())


def list(all=None, auth_mode=None, connection_string=None, endpoint=None, feature=None, key=None, label=None, name=None, top=None):
    '''
    List all filters for a feature flag.

    Optional Parameters:
    - all -- List all filters associated with a feature flag.
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - feature -- Name of the feature whose filters you want to be displayed. If the feature flag key is different from the default key, provide the `--key` argument instead.
    - key -- Key of the feature flag. Key must start with the ".appconfig.featureflag/" prefix. Key cannot contain the "%" character. If both key and feature arguments are provided, only key will be used. Default key is the reserved prefix ".appconfig.featureflag/" + feature name.
    - label -- If no label specified, display filters from the feature flag with null label by default.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - top -- Maximum number of items to return. Must be a positive integer. Default to 100.
    '''
    return _call_az("az appconfig feature filter list", locals())

