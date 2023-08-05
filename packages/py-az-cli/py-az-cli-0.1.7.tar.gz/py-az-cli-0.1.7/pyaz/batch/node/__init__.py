'''
Manage Batch compute nodes.
'''
from ... pyaz_utils import _call_az
from . import file, remote_desktop, remote_login_settings, scheduling, service_logs, user


def delete(pool_id, account_endpoint=None, account_key=None, account_name=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, json_file=None, node_deallocation_option=None, node_list=None, resize_timeout=None):
    '''
    

    Required Parameters:
    - pool_id -- The ID of the Pool from which you want to remove Compute Nodes.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    - json_file -- A file containing the node remove parameter specification in JSON (formatted to match the respective REST API body). If this parameter is specified, all 'Node Remove Arguments' are ignored.
    - node_deallocation_option -- Determines what to do with a Compute Node and its running task(s) after it has been selected for deallocation. The default value is requeue.
    - node_list -- Required. A maximum of 100 nodes may be removed per request. Space-separated values.
    - resize_timeout -- The default value is 15 minutes. The minimum value is 5 minutes. If you specify a value less than 5 minutes, the Batch service returns an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). Expected format is an ISO-8601 duration.
    '''
    return _call_az("az batch node delete", locals())


def show(node_id, pool_id, account_endpoint=None, account_key=None, account_name=None, select=None):
    '''
    

    Required Parameters:
    - node_id -- The ID of the Compute Node that you want to get information about.
    - pool_id -- The ID of the Pool that contains the Compute Node.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - select -- An OData $select clause.
    '''
    return _call_az("az batch node show", locals())


def list(pool_id, account_endpoint=None, account_key=None, account_name=None, filter=None, select=None):
    '''
    

    Required Parameters:
    - pool_id -- The ID of the Pool from which you want to list Compute Nodes.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - filter -- An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-nodes-in-a-pool.
    - select -- An OData $select clause.
    '''
    return _call_az("az batch node list", locals())


def reboot(node_id, pool_id, account_endpoint=None, account_key=None, account_name=None, node_reboot_option=None):
    '''
    

    Required Parameters:
    - node_id -- The ID of the Compute Node that you want to restart.
    - pool_id -- The ID of the Pool that contains the Compute Node.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - node_reboot_option -- The default value is requeue.
    '''
    return _call_az("az batch node reboot", locals())


def reimage(node_id, pool_id, account_endpoint=None, account_key=None, account_name=None, node_reimage_option=None):
    '''
    

    Required Parameters:
    - node_id -- The ID of the Compute Node that you want to restart.
    - pool_id -- The ID of the Pool that contains the Compute Node.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - node_reimage_option -- The default value is requeue.
    '''
    return _call_az("az batch node reimage", locals())

