from .... pyaz_utils import _call_az

def list(name, resource_group, slot=None):
    '''
    Get a web app's connection strings.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config connection-string list", locals())


def set(connection_string_type, name, resource_group, settings=None, slot=None, slot_settings=None):
    '''
    Update a web app's connection strings.

    Required Parameters:
    - connection_string_type -- connection string type
    - name -- Name of the web app. You can configure the default using `az configure --defaults web=<name>`. If `--ids` is provided this should NOT be specified.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - settings -- space-separated connection-string in a format of `<name>=<value>`
    - slot -- the name of the slot. Default to the productions slot if not specified
    - slot_settings -- space-separated slot connection-string in a format of either `<name>=<value>` or `@<json_file>`
    '''
    return _call_az("az webapp config connection-string set", locals())


def delete(name, resource_group, setting_names, slot=None):
    '''
    Delete a web app's connection strings.

    Required Parameters:
    - name -- Name of the web app. You can configure the default using `az configure --defaults web=<name>`. If `--ids` is provided this should NOT be specified.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - setting_names -- space-separated connection-string names

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config connection-string delete", locals())

