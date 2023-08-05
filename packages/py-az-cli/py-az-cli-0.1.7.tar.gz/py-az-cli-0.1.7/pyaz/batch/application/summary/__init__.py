'''
View a summary of Batch application packages.
'''
from .... pyaz_utils import _call_az

def list(account_endpoint=None, account_key=None, account_name=None):
    '''
    Lists all of the applications available in the specified account.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    '''
    return _call_az("az batch application summary list", locals())


def show(application_id, account_endpoint=None, account_key=None, account_name=None):
    '''
    Gets information about the specified application.

    Required Parameters:
    - application_id -- The ID of the Application.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    '''
    return _call_az("az batch application summary show", locals())

