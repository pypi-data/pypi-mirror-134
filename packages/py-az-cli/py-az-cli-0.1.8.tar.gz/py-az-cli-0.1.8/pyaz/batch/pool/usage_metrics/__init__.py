from .... pyaz_utils import _call_az

def list(account_endpoint=None, account_key=None, account_name=None, end_time=None, filter=None, start_time=None):
    '''
    

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - end_time -- The latest time from which to include metrics. This must be at least two hours before the current time. If not specified this defaults to the end time of the last aggregation interval currently available.
    - filter -- An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-account-usage-metrics.
    - start_time -- The earliest time from which to include metrics. This must be at least two and a half hours before the current time. If not specified this defaults to the start time of the last aggregation interval currently available.
    '''
    return _call_az("az batch pool usage-metrics list", locals())

