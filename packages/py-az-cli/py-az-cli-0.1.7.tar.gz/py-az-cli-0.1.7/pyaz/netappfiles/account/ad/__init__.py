'''
Manage Azure NetApp Files (ANF) Account active directories.
'''
from .... pyaz_utils import _call_az

def add(dns, domain, name, password, resource_group, smb_server_name, username, ad_name=None, add=None, administrators=None, aes_encryption=None, allow_local_ldap_users=None, backup_operators=None, force_string=None, kdc_ip=None, ldap_over_tls=None, ldap_signing=None, organizational_unit=None, remove=None, security_operators=None, server_root_ca_cert=None, set=None, tags=None):
    '''
    Add an active directory to the account.

    Required Parameters:
    - dns -- None
    - domain -- None
    - name -- Name of the ANF account.
    - password -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - smb_server_name -- None
    - username -- None

    Optional Parameters:
    - ad_name -- None
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - administrators -- None
    - aes_encryption -- None
    - allow_local_ldap_users -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - backup_operators -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - kdc_ip -- None
    - ldap_over_tls -- None
    - ldap_signing -- None
    - organizational_unit -- None
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - security_operators -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - server_root_ca_cert -- None
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az netappfiles account ad add", locals())


def list(name, resource_group):
    '''
    List the active directories of an account.

    Required Parameters:
    - name -- The name of the ANF account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az netappfiles account ad list", locals())


def remove(active_directory, name, resource_group):
    '''
    Remove an active directory from the account.

    Required Parameters:
    - active_directory -- None
    - name -- Name of the ANF account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az netappfiles account ad remove", locals())

