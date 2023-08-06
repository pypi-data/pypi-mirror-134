'''
Manage web app snapshots.
'''
from .... pyaz_utils import _call_az

def list(name, resource_group, slot=None):
    '''
    List the restorable snapshots for a web app.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- The name of the slot.
    '''
    return _call_az("az webapp config snapshot list", locals())


def restore(name, resource_group, time, restore_content_only=None, slot=None, source_name=None, source_resource_group=None, source_slot=None):
    '''
    Restore a web app snapshot.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - time -- Timestamp of the snapshot to restore.

    Optional Parameters:
    - restore_content_only -- Restore the web app files without restoring the settings.
    - slot -- The name of the slot.
    - source_name -- Name of the web app to retrieve snapshot from.
    - source_resource_group -- Name of the resource group to retrieve snapshot from.
    - source_slot -- Name of the web app slot to retrieve snapshot from.
    '''
    return _call_az("az webapp config snapshot restore", locals())

