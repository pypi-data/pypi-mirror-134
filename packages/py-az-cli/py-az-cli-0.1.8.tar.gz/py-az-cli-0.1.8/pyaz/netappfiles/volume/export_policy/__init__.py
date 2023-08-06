from .... pyaz_utils import _call_az

def add(account_name, allowed_clients, cifs, nfsv3, nfsv41, pool_name, resource_group, rule_index, unix_read_only, unix_read_write, volume_name, add=None, force_string=None, remove=None, set=None):
    '''
    Add a new rule to the export policy for a volume.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - allowed_clients -- None
    - cifs -- Indication that CIFS protocol is allowed
    - nfsv3 -- Indication that NFSv3 protocol is allowed
    - nfsv41 -- Indication that NFSv4.1 protocol is allowed
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_index -- None
    - unix_read_only -- Indication of read only access
    - unix_read_write -- Indication of read and write access
    - volume_name -- Name of the ANF volume.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az netappfiles volume export-policy add", locals())


def list(account_name, pool_name, resource_group, volume_name):
    '''
    List the export policy rules for a volume.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles volume export-policy list", locals())


def remove(account_name, pool_name, resource_group, rule_index, volume_name, add=None, force_string=None, remove=None, set=None):
    '''
    Remove a rule from the export policy for a volume by rule index. The current rules can be obtained by performing the subgroup list command.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_index -- None
    - volume_name -- Name of the ANF volume.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az netappfiles volume export-policy remove", locals())

