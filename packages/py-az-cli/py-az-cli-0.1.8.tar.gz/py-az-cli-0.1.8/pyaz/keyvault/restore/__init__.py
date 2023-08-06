'''
Manage full HSM restore.
'''
from ... pyaz_utils import _call_az

def start(backup_folder, storage_container_SAS_token, blob_container_name=None, hsm_name=None, id=None, storage_account_name=None, storage_resource_uri=None):
    '''
    Restore a full backup of a HSM.

    Required Parameters:
    - backup_folder -- Name of the blob container which contains the backup
    - storage_container_SAS_token -- The SAS token pointing to an Azure Blob storage container

    Optional Parameters:
    - blob_container_name -- Name of Blob Container.
    - hsm_name -- Name of the HSM. Can be omitted if --id is specified.
    - id -- Full URI of the HSM.
    - storage_account_name -- Name of Azure Storage Account.
    - storage_resource_uri -- Azure Blob storage container Uri. If specified all other 'Storage Id' arguments should be omitted
    '''
    return _call_az("az keyvault restore start", locals())

