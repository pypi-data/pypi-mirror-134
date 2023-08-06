from ... pyaz_utils import _call_az

def create(account_name, asset_name, name, resource_group, streaming_policy_name, alternative_media_id=None, content_key_policy_name=None, content_keys=None, end_time=None, filters=None, start_time=None, streaming_locator_id=None):
    '''
    Create a streaming locator.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - asset_name -- The name of the asset used by the streaming locator.
    - name -- The name of the streaming locator.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - streaming_policy_name -- The name of the streaming policy used by the streaming locator. You can either create one with `az ams streaming policy create` or use any of the predefined policies: Predefined_DownloadOnly, Predefined_ClearStreamingOnly, Predefined_DownloadAndClearStreaming, Predefined_ClearKey, Predefined_MultiDrmCencStreaming, Predefined_MultiDrmStreaming

    Optional Parameters:
    - alternative_media_id -- An alternative media identifier associated with the streaming locator.
    - content_key_policy_name -- The default content key policy name used by the streaming locator.
    - content_keys -- JSON string with the content keys to be used by the streaming locator. Use @{file} to load from a file. For further information about the JSON structure please refer to swagger documentation on https://docs.microsoft.com/rest/api/media/streaminglocators/create#streaminglocatorcontentkey
    - end_time -- The ISO 8601 DateTime end time (Y-m-d'T'H:M:S'Z') of the streaming locator.
    - filters -- A space-separated list of asset filter names and/or account filter names.
    - start_time -- The ISO 8601 DateTime start time (Y-m-d'T'H:M:S'Z') of the streaming locator.
    - streaming_locator_id -- The identifier of the streaming locator.
    '''
    return _call_az("az ams streaming-locator create", locals())


def list(account_name, resource_group, filter=None, orderby=None, top=None):
    '''
    List all the streaming locators within an Azure Media Services account.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - filter -- Restricts the set of items returned.
    - orderby -- Specifies the key by which the result collection should be ordered.
    - top -- Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
    '''
    return _call_az("az ams streaming-locator list", locals())


def show(account_name, name, resource_group):
    '''
    Show the details of a streaming locator.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the streaming locator.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams streaming-locator show", locals())


def delete(account_name, name, resource_group):
    '''
    

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the streaming locator.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams streaming-locator delete", locals())


def get_paths(account_name, name, resource_group):
    '''
    List paths supported by a streaming locator.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the streaming locator.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams streaming-locator get-paths", locals())


def list_content_keys(account_name, name, resource_group):
    '''
    List content keys used by a streaming locator.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the streaming locator.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams streaming-locator list-content-keys", locals())

