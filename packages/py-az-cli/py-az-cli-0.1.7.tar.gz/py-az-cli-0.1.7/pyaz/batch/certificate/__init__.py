'''
Manage Batch certificates.
'''
from ... pyaz_utils import _call_az

def create(certificate_file, thumbprint, account_endpoint=None, account_key=None, account_name=None, password=None):
    '''
    Add a certificate to a Batch account.

    Required Parameters:
    - certificate_file -- The certificate file: cer file or pfx file.
    - thumbprint -- The certificate thumbprint.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- The Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- The Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - password -- The password to access the certificate's private key.
    '''
    return _call_az("az batch certificate create", locals())


def delete(thumbprint, abort=None, account_endpoint=None, account_key=None, account_name=None, yes=None):
    '''
    Delete a certificate from a Batch account.

    Required Parameters:
    - thumbprint -- The certificate thumbprint.

    Optional Parameters:
    - abort -- Cancel the failed certificate deletion operation.
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- The Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- The Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az batch certificate delete", locals())


def show(thumbprint, account_endpoint=None, account_key=None, account_name=None, select=None):
    '''
    

    Required Parameters:
    - thumbprint -- The certificate thumbprint.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - select -- An OData $select clause.
    '''
    return _call_az("az batch certificate show", locals())


def list(account_endpoint=None, account_key=None, account_name=None, filter=None, select=None):
    '''
    

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - filter -- An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-certificates.
    - select -- An OData $select clause.
    '''
    return _call_az("az batch certificate list", locals())

