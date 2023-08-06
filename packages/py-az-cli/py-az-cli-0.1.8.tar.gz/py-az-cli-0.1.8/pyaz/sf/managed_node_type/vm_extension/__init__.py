from .... pyaz_utils import _call_az

def add(cluster_name, extension_name, extension_type, publisher, resource_group, type_handler_version, auto_upgrade_minor_version=None, force_update_tag=None, protected_setting=None, provision_after_extension=None, setting=None):
    '''
    Add an extension to the node type.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - extension_name -- extension name.
    - extension_type -- Specifies the type of the extension; an example is "CustomScriptExtension".
    - publisher -- The name of the extension handler publisher.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    - type_handler_version -- Specifies the version of the script handler.

    Optional Parameters:
    - auto_upgrade_minor_version -- Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true.
    - force_update_tag -- If a value is provided and is different from the previous value, the extension handler will be forced to update even if the extension configuration has not changed.
    - protected_setting -- The extension can contain either protectedSettings or protectedSettingsFromKeyVault or no protected settings at all.
    - provision_after_extension -- Collection of extension names after which this extension needs to be provisioned.
    - setting -- Json formatted public settings for the extension.
    '''
    return _call_az("az sf managed-node-type vm-extension add", locals())


def delete(cluster_name, extension_name, resource_group):
    '''
    Delete an extension to the node type.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - extension_name -- extension name.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf managed-node-type vm-extension delete", locals())

