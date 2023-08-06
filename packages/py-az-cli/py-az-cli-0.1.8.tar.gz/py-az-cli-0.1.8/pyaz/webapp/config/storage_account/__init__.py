from .... pyaz_utils import _call_az

def list(name, resource_group, slot=None):
    '''
    Get a web app's Azure storage account configurations. (Linux Web Apps and Windows Containers Web Apps Only)

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config storage-account list", locals())


def add(access_key, account_name, custom_id, name, resource_group, share_name, storage_type, mount_path=None, slot=None, slot_setting=None):
    '''
    Add an Azure storage account configuration to a web app. (Linux Web Apps and Windows Containers Web Apps Only)

    Required Parameters:
    - access_key -- storage account access key
    - account_name -- storage account name
    - custom_id -- name of the share configured within the web app
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - share_name -- name of the file share as given in the storage account
    - storage_type -- storage type

    Optional Parameters:
    - mount_path -- the path which the web app uses to read-write data ex: /share1 or /share2
    - slot -- the name of the slot. Default to the productions slot if not specified
    - slot_setting -- slot setting
    '''
    return _call_az("az webapp config storage-account add", locals())


def update(custom_id, name, resource_group, access_key=None, account_name=None, mount_path=None, share_name=None, slot=None, slot_setting=None, storage_type=None):
    '''
    Update an existing Azure storage account configuration on a web app. (Linux Web Apps and Windows Containers Web Apps Only)

    Required Parameters:
    - custom_id -- name of the share configured within the web app
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - access_key -- storage account access key
    - account_name -- storage account name
    - mount_path -- the path which the web app uses to read-write data ex: /share1 or /share2
    - share_name -- name of the file share as given in the storage account
    - slot -- the name of the slot. Default to the productions slot if not specified
    - slot_setting -- slot setting
    - storage_type -- storage type
    '''
    return _call_az("az webapp config storage-account update", locals())


def delete(custom_id, name, resource_group, slot=None):
    '''
    Delete a web app's Azure storage account configuration. (Linux Web Apps and Windows Containers Web Apps Only)

    Required Parameters:
    - custom_id -- name of the share configured within the web app
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config storage-account delete", locals())

