'''
Manage feature flags stored in an App Configuration.
'''
from ... pyaz_utils import _call_az
from . import filter


def set(auth_mode=None, connection_string=None, description=None, endpoint=None, feature=None, key=None, label=None, name=None, yes=None):
    '''
    Set a feature flag.

    Optional Parameters:
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - description -- Description of the feature flag to be set.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - feature -- Name of the feature flag to be set. Feature name cannot contain the '%' character.
    - key -- Key of the feature flag. Key must start with the ".appconfig.featureflag/" prefix. Key cannot contain the "%" character. Default key is the reserved prefix ".appconfig.featureflag/" + feature name.
    - label -- If no label specified, set the feature flag with null label by default
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az appconfig feature set", locals())


def delete(auth_mode=None, connection_string=None, endpoint=None, feature=None, key=None, label=None, name=None, yes=None):
    '''
    Delete feature flag.

    Optional Parameters:
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - feature -- Name of the feature to be deleted. If the feature flag key is different from the default key, provide the `--key` argument instead. Support star sign as filters, for instance * means all features and abc* means features with abc as prefix. Comma separated features are not supported. Please provide escaped string if your feature name contains comma.
    - key -- Key of the feature flag. Key must start with the ".appconfig.featureflag/" prefix. Key cannot contain the "%" character. If both key and feature arguments are provided, only key will be used. Support star sign as filters, for instance ".appconfig.featureflag/*" means all features and ".appconfig.featureflag/abc*" means features with abc as prefix. Comma separated features are not supported. Please provide escaped string if your feature name contains comma.
    - label -- If no label specified, delete the feature flag with null label by default. Support star sign as filters, for instance * means all labels and abc* means labels with abc as prefix.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az appconfig feature delete", locals())


def show(auth_mode=None, connection_string=None, endpoint=None, feature=None, fields=None, key=None, label=None, name=None):
    '''
    Show all attributes of a feature flag.

    Optional Parameters:
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - feature -- Name of the feature flag to be retrieved. If the feature flag key is different from the default key, provide the `--key` argument instead.
    - fields -- Customize output fields for Feature Flags.
    - key -- Key of the feature flag. Key must start with the ".appconfig.featureflag/" prefix. Key cannot contain the "%" character. If both key and feature arguments are provided, only key will be used. Default key is the reserved prefix ".appconfig.featureflag/" + feature name.
    - label -- If no label specified, show entry with null label. Filtering is not supported.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    '''
    return _call_az("az appconfig feature show", locals())


def list(all=None, auth_mode=None, connection_string=None, endpoint=None, feature=None, fields=None, key=None, label=None, name=None, top=None):
    '''
    List feature flags.

    Optional Parameters:
    - all -- List all feature flags.
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - feature -- Name of the feature to be listed. If the feature flag key is different from the default key, provide the `--key` argument instead. Support star sign as filters, for instance * means all features and abc* means features with abc as prefix. Comma separated features are not supported. Please provide escaped string if your feature name contains comma.
    - fields -- Customize output fields for Feature Flags.
    - key -- Key of the feature flag. Key must start with the ".appconfig.featureflag/" prefix. Key cannot contain the "%" character. If both key and feature arguments are provided, only key will be used. Support star sign as filters, for instance ".appconfig.featureflag/*" means all features and ".appconfig.featureflag/abc*" means features with abc as prefix. Comma separated features are not supported. Please provide escaped string if your feature name contains comma.
    - label -- If no label specified, list all labels. Support star sign as filters, for instance * means all labels and abc* means labels with abc as prefix. Use '\0' for null label.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - top -- Maximum number of items to return. Must be a positive integer. Default to 100.
    '''
    return _call_az("az appconfig feature list", locals())


def lock(auth_mode=None, connection_string=None, endpoint=None, feature=None, key=None, label=None, name=None, yes=None):
    '''
    Lock a feature flag to prohibit write operations.

    Optional Parameters:
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - feature -- Name of the feature to be locked. If the feature flag key is different from the default key, provide the `--key` argument instead.
    - key -- Key of the feature flag. Key must start with the ".appconfig.featureflag/" prefix. Key cannot contain the "%" character. If both key and feature arguments are provided, only key will be used. Default key is the reserved prefix ".appconfig.featureflag/" + feature name.
    - label -- If no label specified, lock the feature flag with null label by default.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az appconfig feature lock", locals())


def unlock(auth_mode=None, connection_string=None, endpoint=None, feature=None, key=None, label=None, name=None, yes=None):
    '''
    Unlock a feature to gain write operations.

    Optional Parameters:
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - feature -- Name of the feature to be unlocked. If the feature flag key is different from the default key, provide the `--key` argument instead.
    - key -- Key of the feature flag. Key must start with the ".appconfig.featureflag/" prefix. Key cannot contain the "%" character. If both key and feature arguments are provided, only key will be used. Default key is the reserved prefix ".appconfig.featureflag/" + feature name.
    - label -- If no label specified, unlock the feature flag with null label by default.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az appconfig feature unlock", locals())


def enable(auth_mode=None, connection_string=None, endpoint=None, feature=None, key=None, label=None, name=None, yes=None):
    '''
    Enable a feature flag to turn it ON for use.

    Optional Parameters:
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - feature -- Name of the feature to be enabled. If the feature flag key is different from the default key, provide the `--key` argument instead.
    - key -- Key of the feature flag. Key must start with the ".appconfig.featureflag/" prefix. Key cannot contain the "%" character. If both key and feature arguments are provided, only key will be used. Default key is the reserved prefix ".appconfig.featureflag/" + feature name.
    - label -- If no label specified, enable the feature flag with null label by default.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az appconfig feature enable", locals())


def disable(auth_mode=None, connection_string=None, endpoint=None, feature=None, key=None, label=None, name=None, yes=None):
    '''
    Disable a feature flag to turn it OFF for use.

    Optional Parameters:
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - feature -- Name of the feature to be disabled. If the feature flag key is different from the default key, provide the `--key` argument instead.
    - key -- Key of the feature flag. Key must start with the ".appconfig.featureflag/" prefix. Key cannot contain the "%" character. If both key and feature arguments are provided, only key will be used. Default key is the reserved prefix ".appconfig.featureflag/" + feature name.
    - label -- If no label specified, disable the feature flag with null label by default.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az appconfig feature disable", locals())

