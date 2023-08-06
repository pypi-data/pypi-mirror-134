from .... pyaz_utils import _call_az

def show(node_id, pool_id, account_endpoint=None, account_key=None, account_name=None):
    '''
    

    Required Parameters:
    - node_id -- The ID of the Compute Node for which to obtain the remote login settings.
    - pool_id -- The ID of the Pool that contains the Compute Node.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    '''
    return _call_az("az batch node remote-login-settings show", locals())

