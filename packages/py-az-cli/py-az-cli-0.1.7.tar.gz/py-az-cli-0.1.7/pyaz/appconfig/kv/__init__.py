'''
Manage key-values stored in an App Configuration.
'''
from ... pyaz_utils import _call_az

def set(key, auth_mode=None, connection_string=None, content_type=None, endpoint=None, label=None, name=None, tags=None, value=None, yes=None):
    '''
    Set a key-value.

    Required Parameters:
    - key -- Key to be set. Key cannot be a '.' or '..', or contain the '%' character.

    Optional Parameters:
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - content_type -- Content type of the keyvalue to be set.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - label -- If no label specified, set the key with null label by default
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - value -- Value of the keyvalue to be set.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az appconfig kv set", locals())


def delete(key, auth_mode=None, connection_string=None, endpoint=None, label=None, name=None, yes=None):
    '''
    Delete key-values.

    Required Parameters:
    - key -- Support star sign as filters, for instance * means all key and abc* means keys with abc as prefix.

    Optional Parameters:
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - label -- If no label specified, delete entry with null label. Support star sign as filters, for instance * means all label and abc* means labels with abc as prefix.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az appconfig kv delete", locals())


def show(key, auth_mode=None, connection_string=None, datetime=None, endpoint=None, label=None, name=None):
    '''
    Show all attributes of a key-value.

    Required Parameters:
    - key -- Key to be showed.

    Optional Parameters:
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - datetime -- Format: "YYYY-MM-DDThh:mm:ssZ". If no time zone specified, use UTC by default.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - label -- If no label specified, show entry with null label. Filtering is not supported.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    '''
    return _call_az("az appconfig kv show", locals())


def list(all=None, auth_mode=None, connection_string=None, datetime=None, endpoint=None, fields=None, key=None, label=None, name=None, resolve_keyvault=None, top=None):
    '''
    List key-values.

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
    - resolve_keyvault -- Resolve the content of key vault reference. This argument should NOT be specified along with --fields. Instead use --query for customized query.
    - top -- Maximum number of items to return. Must be a positive integer. Default to 100.
    '''
    return _call_az("az appconfig kv list", locals())


def lock(key, auth_mode=None, connection_string=None, endpoint=None, label=None, name=None, yes=None):
    '''
    Lock a key-value to prohibit write operations.

    Required Parameters:
    - key -- Key to be locked.

    Optional Parameters:
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - label -- If no label specified, lock entry with null label. Filtering is not supported.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az appconfig kv lock", locals())


def unlock(key, auth_mode=None, connection_string=None, endpoint=None, label=None, name=None, yes=None):
    '''
    Unlock a key-value to gain write operations.

    Required Parameters:
    - key -- Key to be unlocked.

    Optional Parameters:
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - label -- If no label specified, unlock entry with null label. Filtering is not supported.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az appconfig kv unlock", locals())


def restore(datetime, auth_mode=None, connection_string=None, endpoint=None, key=None, label=None, name=None, yes=None):
    '''
    Restore key-values.

    Required Parameters:
    - datetime -- Format: "YYYY-MM-DDThh:mm:ssZ". If no time zone specified, use UTC by default.

    Optional Parameters:
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - key -- If no key specified, restore all keys by default. Support star sign as filters, for instance abc* means keys with abc as prefix.
    - label -- If no label specified, restore all key-value pairs with all labels. Support star sign as filters, for instance abc* means labels with abc as prefix. Use '\0' for null label.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az appconfig kv restore", locals())


def import_(source, appservice_account=None, auth_mode=None, connection_string=None, content_type=None, depth=None, endpoint=None, format=None, label=None, name=None, path=None, prefix=None, preserve_labels=None, profile=None, separator=None, skip_features=None, src_auth_mode=None, src_connection_string=None, src_endpoint=None, src_key=None, src_label=None, src_name=None, yes=None):
    '''
    Import configurations into your App Configuration from another place.

    Required Parameters:
    - source -- The source of importing. Note that importing feature flags from appservice is not supported.

    Optional Parameters:
    - appservice_account -- ARM ID for AppService OR the name of the AppService, assuming it is in the same subscription and resource group as the App Configuration. Required for AppService arguments
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - content_type -- Content type of all imported items.
    - depth -- Depth for flattening the json or yaml file to key-value pairs. Flatten to the deepest level by default if --separator is provided. Not applicable for property files or feature flags.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - format -- Imported file format. Required for file arguments. Currently, feature flags are not supported in properties format.
    - label -- Imported KVs and feature flags will be assigned with this label. If no label specified, will assign null label.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - path -- Local configuration file path. Required for file arguments.
    - prefix -- This prefix will be appended to the front of imported keys. Prefix will be ignored for feature flags.
    - preserve_labels -- Flag to preserve labels from source AppConfig. This argument should NOT be specified along with --label.
    - profile -- Import profile to be used for importing the key-values. Options 'depth', 'separator', 'content-type', 'label', 'skip-features' and, 'prefix' are not supported when using 'appconfig/kvset' profile.
    - separator -- Delimiter for flattening the json or yaml file to key-value pairs. Separator will be ignored for property files and feature flags. Supported values: '.', ',', ';', '-', '_', '__', '/', ':' 
    - skip_features -- Import only key values and exclude all feature flags. By default, all feature flags will be imported from file or appconfig. Not applicable for appservice.
    - src_auth_mode -- Auth mode for connecting to source App Configuration. For details, refer to "--auth-mode" argument.
    - src_connection_string -- Combination of access key and endpoint of the source store.
    - src_endpoint -- If --src-auth-mode is "login", provide endpoint URL of the source App Configuration.
    - src_key -- If no key specified, import all keys by default. Support star sign as filters, for instance abc* means keys with abc as prefix. Key filtering not applicable for feature flags. By default, all feature flags with specified label will be imported.
    - src_label -- Only keys with this label in source AppConfig will be imported. If no value specified, import keys with null label by default. Support star sign as filters, for instance * means all labels, abc* means labels with abc as prefix.
    - src_name -- The name of the source App Configuration.
    - yes -- Do not prompt for preview.
    '''
    return _call_az("az appconfig kv import", locals())


def export(destination, appservice_account=None, auth_mode=None, connection_string=None, dest_auth_mode=None, dest_connection_string=None, dest_endpoint=None, dest_label=None, dest_name=None, endpoint=None, format=None, key=None, label=None, name=None, naming_convention=None, path=None, prefix=None, preserve_labels=None, profile=None, resolve_keyvault=None, separator=None, skip_features=None, skip_keyvault=None, yes=None):
    '''
    Export configurations to another place from your App Configuration.

    Required Parameters:
    - destination -- The destination of exporting. Note that exporting feature flags to appservice is not supported.

    Optional Parameters:
    - appservice_account -- ARM ID for AppService OR the name of the AppService, assuming it is in the same subscription and resource group as the App Configuration. Required for AppService arguments
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - dest_auth_mode -- Auth mode for connecting to destination App Configuration. For details, refer to "--auth-mode" argument.
    - dest_connection_string -- Combination of access key and endpoint of the destination store.
    - dest_endpoint -- If --dest-auth-mode is "login", provide endpoint URL of the destination App Configuration.
    - dest_label -- Exported KVs will be labeled with this destination label. If neither --dest-label nor --preserve-labels is specified, will assign null label.
    - dest_name -- The name of the destination App Configuration.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - format -- File format exporting to. Required for file arguments. Currently, feature flags are not supported in properties format.
    - key -- If no key specified, return all keys by default. Support star sign as filters, for instance abc* means keys with abc as prefix. Key filtering not applicable for feature flags. By default, all feature flags with specified label will be exported.
    - label -- Only keys and feature flags with this label will be exported. If no label specified, export keys and feature flags with null label by default. Only when export destination is appconfig, we support star sign as filters, for instance * means all labels and abc* means labels with abc as prefix. Label filters are not supported when exporting to file or appservice.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - naming_convention -- Naming convention to be used for "Feature Management" section of file. Example: pascal = FeatureManagement, camel = featureManagement, underscore = feature_management, hyphen = feature-management.
    - path -- Local configuration file path. Required for file arguments.
    - prefix -- Prefix to be trimmed from keys. Prefix will be ignored for feature flags.
    - preserve_labels -- Flag to preserve labels from source AppConfig. This argument should NOT be specified along with --dest-label.
    - profile -- Export profile to be used for exporting the key-values. Options 'depth', 'separator', 'naming-convention', 'prefix', 'dest-label' and, 'resolve-keyvault' are not supported when using 'appconfig/kvset' profile
    - resolve_keyvault -- Resolve the content of key vault reference.
    - separator -- Delimiter for flattening the key-value pairs to json or yaml file. Required for exporting hierarchical structure. Separator will be ignored for property files and feature flags. Supported values: '.', ',', ';', '-', '_', '__', '/', ':' 
    - skip_features -- Export items excluding all feature flags. By default, all features with the specified label will be exported to file or appconfig. Not applicable for appservice.
    - skip_keyvault -- Export items excluding all key vault references. By default, all key vault references with the specified label will be exported.
    - yes -- Do not prompt for preview.
    '''
    return _call_az("az appconfig kv export", locals())


def set_keyvault(key, secret_identifier, auth_mode=None, connection_string=None, endpoint=None, label=None, name=None, tags=None, yes=None):
    '''
    Set a keyvault reference.

    Required Parameters:
    - key -- Key to be set. Key cannot be a '.' or '..', or contain the '%' character.
    - secret_identifier -- ID of the Key Vault object. Can be found using 'az keyvault {collection} show' command, where collection is key, secret or certificate. To set reference to the latest version of your secret, remove version information from secret identifier.

    Optional Parameters:
    - auth_mode -- This parameter can be used for indicating how a data operation is to be authorized. If the auth mode is "key", provide connection string or store name and your account access keys will be retrieved for authorization. If the auth mode is "login", provide the store endpoint or store name and your "az login" credentials will be used for authorization. You can configure the default auth mode using `az configure --defaults appconfig_auth_mode=<auth_mode>`. For more information, see https://docs.microsoft.com/azure/azure-app-configuration/concept-enable-rbac
    - connection_string -- Combination of access key and endpoint of App Configuration. Can be found using 'az appconfig credential list'. Users can preset it using `az configure --defaults appconfig_connection_string=<connection_string>` or environment variable with the name AZURE_APPCONFIG_CONNECTION_STRING.
    - endpoint -- If auth mode is "login", provide endpoint URL of the App Configuration. The endpoint can be retrieved using "az appconfig show" command. You can configure the default endpoint using `az configure --defaults appconfig_endpoint=<endpoint>`
    - label -- If no label specified, set the key with null label by default
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az appconfig kv set-keyvault", locals())

