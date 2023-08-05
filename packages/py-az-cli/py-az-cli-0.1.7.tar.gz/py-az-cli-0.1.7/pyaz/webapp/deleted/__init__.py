'''
Manage deleted web apps.
'''
from ... pyaz_utils import _call_az

def list(name=None, resource_group=None, slot=None):
    '''
    List web apps that have been deleted.

    Optional Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - slot -- Name of the deleted web app slot.
    '''
    return _call_az("az webapp deleted list", locals())


def restore(deleted_id, name, resource_group, restore_content_only=None, slot=None):
    '''
    Restore a deleted web app.

    Required Parameters:
    - deleted_id -- Resource ID of the deleted web app
    - name -- name of the web app to restore the deleted content to
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - restore_content_only -- restore only deleted files without web app settings
    - slot -- slot to restore the deleted content to
    '''
    return _call_az("az webapp deleted restore", locals())

