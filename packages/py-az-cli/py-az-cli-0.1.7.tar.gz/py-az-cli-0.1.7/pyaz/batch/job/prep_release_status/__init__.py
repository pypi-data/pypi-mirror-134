from .... pyaz_utils import _call_az

def list(job_id, account_endpoint=None, account_key=None, account_name=None, filter=None, select=None):
    '''
    

    Required Parameters:
    - job_id -- The ID of the Job.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - filter -- An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-job-preparation-and-release-status.
    - select -- An OData $select clause.
    '''
    return _call_az("az batch job prep-release-status list", locals())

