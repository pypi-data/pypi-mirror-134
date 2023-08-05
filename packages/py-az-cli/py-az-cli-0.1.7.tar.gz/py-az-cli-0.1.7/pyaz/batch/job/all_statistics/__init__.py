from .... pyaz_utils import _call_az

def show(account_endpoint=None, account_key=None, account_name=None):
    '''
    Get lifetime summary statistics for all of the jobs in a Batch account.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    '''
    return _call_az("az batch job all-statistics show", locals())

