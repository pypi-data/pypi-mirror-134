from .... pyaz_utils import _call_az

def upload(node_id, pool_id, account_endpoint=None, account_key=None, account_name=None, container_url=None, end_time=None, json_file=None, resource_id=None, start_time=None):
    '''
    

    Required Parameters:
    - node_id -- The ID of the Compute Node from which you want to upload the Azure Batch service log files.
    - pool_id -- The ID of the Pool that contains the Compute Node.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - container_url -- Required. If a user assigned managed identity is not being used, the URL must include a Shared Access Signature (SAS) granting write permissions to the container. The SAS duration must allow enough time for the upload to finish. The start time for SAS is optional and recommended to not be specified.
    - end_time -- Any log file containing a log message in the time range will be uploaded. This means that the operation might retrieve more logs than have been requested since the entire log file is always uploaded, but the operation should not retrieve fewer logs than have been requested. If omitted, the default is to upload all logs available after the startTime. Expected format is an ISO-8601 timestamp.
    - json_file -- A file containing the upload batch service logs configuration specification in JSON (formatted to match the respective REST API body). If this parameter is specified, all 'Upload Batch Service Logs Configuration Arguments' are ignored.
    - resource_id -- The ARM resource id of the user assigned identity.
    - start_time -- Required. Any log file containing a log message in the time range will be uploaded. This means that the operation might retrieve more logs than have been requested since the entire log file is always uploaded, but the operation should not retrieve fewer logs than have been requested. Expected format is an ISO-8601 timestamp.
    '''
    return _call_az("az batch node service-logs upload", locals())

