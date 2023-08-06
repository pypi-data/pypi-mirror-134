from .... pyaz_utils import _call_az

def download(destination, node_id, pool_id, account_endpoint=None, account_key=None, account_name=None):
    '''
    

    Required Parameters:
    - destination -- The path to the destination file or directory.
    - node_id -- The ID of the Compute Node for which you want to get the Remote Desktop Protocol file.
    - pool_id -- The ID of the Pool that contains the Compute Node.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    '''
    return _call_az("az batch node remote-desktop download", locals())

