'''
Manage Data Lake Store filesystem access and permissions.
'''
from .... pyaz_utils import _call_az

def set_permission(account, path, permission):
    '''
    Set the permissions for a file or folder in a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - path -- The path in the specified Data Lake Store account where the action should take place. In the format '/folder/file.txt', where the first '/' after the DNS indicates the root of the file system.
    - permission -- The octal representation of the permissions for user, group and mask (for example: 777 is full rwx for all entities)
    '''
    return _call_az("az dls fs access set-permission", locals())


def set_owner(account, path, group=None, owner=None):
    '''
    Set the owner information for a file or folder in a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - path -- The path in the specified Data Lake Store account where the action should take place. In the format '/folder/file.txt', where the first '/' after the DNS indicates the root of the file system.

    Optional Parameters:
    - group -- None
    - owner -- None
    '''
    return _call_az("az dls fs access set-owner", locals())


def show(account, path):
    '''
    Display the access control list (ACL).

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - path -- The path in the specified Data Lake Store account where the action should take place. In the format '/folder/file.txt', where the first '/' after the DNS indicates the root of the file system.
    '''
    return _call_az("az dls fs access show", locals())


def set_entry(account, acl_spec, path):
    '''
    Update the access control list for a file or folder.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - acl_spec --  The ACL specification to set on the path in the format '[default:]user|group|other:[entity id or UPN]:r|-w|-x|-,[default:]user|group|other:[entity id or UPN]:r|-w|-x|-,...'.
    - path -- The path in the specified Data Lake Store account where the action should take place. In the format '/folder/file.txt', where the first '/' after the DNS indicates the root of the file system.
    '''
    return _call_az("az dls fs access set-entry", locals())


def set(account, acl_spec, path):
    '''
    Replace the existing access control list for a file or folder.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - acl_spec --  The ACL specification to set on the path in the format '[default:]user|group|other:[entity id or UPN]:r|-w|-x|-,[default:]user|group|other:[entity id or UPN]:r|-w|-x|-,...'.
    - path -- The path in the specified Data Lake Store account where the action should take place. In the format '/folder/file.txt', where the first '/' after the DNS indicates the root of the file system.
    '''
    return _call_az("az dls fs access set", locals())


def remove_entry(account, acl_spec, path):
    '''
    Remove entries for the access control list of a file or folder.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - acl_spec --  The ACL specification to set on the path in the format '[default:]user|group|other:[entity id or UPN]:r|-w|-x|-,[default:]user|group|other:[entity id or UPN]:r|-w|-x|-,...'.
    - path -- The path in the specified Data Lake Store account where the action should take place. In the format '/folder/file.txt', where the first '/' after the DNS indicates the root of the file system.
    '''
    return _call_az("az dls fs access remove-entry", locals())


def remove_all(account, path, default_acl=None):
    '''
    Remove the access control list for a file or folder.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - path -- The path in the specified Data Lake Store account where the action should take place. In the format '/folder/file.txt', where the first '/' after the DNS indicates the root of the file system.

    Optional Parameters:
    - default_acl -- A switch that, if specified, indicates that the remove ACL operation should remove the default ACL of the folder. Otherwise the regular ACL is removed.
    '''
    return _call_az("az dls fs access remove-all", locals())

