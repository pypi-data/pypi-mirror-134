'''
Manage automatic scaling of Batch pools.
'''
from .... pyaz_utils import _call_az

def disable(pool_id, account_endpoint=None, account_key=None, account_name=None):
    '''
    

    Required Parameters:
    - pool_id -- The ID of the Pool on which to disable automatic scaling.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    '''
    return _call_az("az batch pool autoscale disable", locals())


def enable(pool_id, account_endpoint=None, account_key=None, account_name=None, auto_scale_evaluation_interval=None, auto_scale_formula=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None):
    '''
    

    Required Parameters:
    - pool_id -- The ID of the Pool on which to enable automatic scaling.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - auto_scale_evaluation_interval -- The default value is 15 minutes. The minimum and maximum value are 5 minutes and 168 hours respectively. If you specify a value less than 5 minutes or greater than 168 hours, the Batch service rejects the request with an invalid property value error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). If you specify a new interval, then the existing autoscale evaluation schedule will be stopped and a new autoscale evaluation schedule will be started, with its starting time being the time when this request was issued.
    - auto_scale_formula -- The formula is checked for validity before it is applied to the Pool. If the formula is not valid, the Batch service rejects the request with detailed error information. For more information about specifying this formula, see Automatically scale Compute Nodes in an Azure Batch Pool (https://azure.microsoft.com/en-us/documentation/articles/batch-automatic-scaling).
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    '''
    return _call_az("az batch pool autoscale enable", locals())


def evaluate(auto_scale_formula, pool_id, account_endpoint=None, account_key=None, account_name=None):
    '''
    

    Required Parameters:
    - auto_scale_formula -- The formula is validated and its results calculated, but it is not applied to the Pool. To apply the formula to the Pool, 'Enable automatic scaling on a Pool'. For more information about specifying this formula, see Automatically scale Compute Nodes in an Azure Batch Pool (https://azure.microsoft.com/en-us/documentation/articles/batch-automatic-scaling).
    - pool_id -- The ID of the Pool on which to evaluate the automatic scaling formula.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    '''
    return _call_az("az batch pool autoscale evaluate", locals())

