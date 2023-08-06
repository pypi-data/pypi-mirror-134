from ... pyaz_utils import _call_az

def create(account_name, name, resource_group, cbcs_clear_tracks=None, cbcs_default_key_label=None, cbcs_default_key_policy_name=None, cbcs_fair_play_allow_persistent_license=None, cbcs_fair_play_template=None, cbcs_key_to_track_mappings=None, cbcs_play_ready_attributes=None, cbcs_play_ready_template=None, cbcs_protocols=None, cbcs_widevine_template=None, cenc_clear_tracks=None, cenc_default_key_label=None, cenc_default_key_policy_name=None, cenc_disable_play_ready=None, cenc_disable_widevine=None, cenc_key_to_track_mappings=None, cenc_play_ready_attributes=None, cenc_play_ready_template=None, cenc_protocols=None, cenc_widevine_template=None, default_content_key_policy_name=None, envelope_clear_tracks=None, envelope_default_key_label=None, envelope_default_key_policy_name=None, envelope_key_to_track_mappings=None, envelope_protocols=None, envelope_template=None, no_encryption_protocols=None):
    '''
    Create a streaming policy.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the streaming policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - cbcs_clear_tracks -- The JSON representing which tracks should not be encrypted. Use @{file} to load from a file. For further information about the JSON structure please refer to swagger documentation on https://docs.microsoft.com/rest/api/media/streamingpolicies/create#trackselection
    - cbcs_default_key_label -- Label to specify Default Content Key for an encryption scheme.
    - cbcs_default_key_policy_name -- Policy used by Default Content Key.
    - cbcs_fair_play_allow_persistent_license -- Allows the license to be persistent or not.
    - cbcs_fair_play_template -- The custom license acquisition URL template for a customer service to deliver keys to end users. Not needed when using Azure Media Services for issuing keys.
    - cbcs_key_to_track_mappings -- The JSON representing a list of StreamingPolicyContentKey. Use @{file} to load from a file. For further information about the JSON structure please refer to swagger documentation on https://docs.microsoft.com/rest/api/media/streamingpolicies/create#streamingpolicycontentkey
    - cbcs_play_ready_attributes -- Custom attributes for PlayReady.
    - cbcs_play_ready_template -- The custom license acquisition URL template for a customer service to deliver keys to end users. Not needed when using Azure Media Services for issuing keys.
    - cbcs_protocols -- Space-separated list of enabled protocols for Common Encryption CBCS. Allowed values: Download, Dash, HLS, SmoothStreaming.
    - cbcs_widevine_template -- The custom license acquisition URL template for a customer service to deliver keys to end users. Not needed when using Azure Media Services for issuing keys.
    - cenc_clear_tracks -- The JSON representing which tracks should not be encrypted. Use @{file} to load from a file. For further information about the JSON structure please refer to swagger documentation on https://docs.microsoft.com/rest/api/media/streamingpolicies/create#trackselection
    - cenc_default_key_label -- Label to specify Default Content Key for an encryption scheme.
    - cenc_default_key_policy_name -- Policy used by Default Content Key.
    - cenc_disable_play_ready -- If specified, no PlayReady cenc DRM will be configured. If --cenc-disable-play-ready is set, --cenc-disable-widevine cannot also be set.
    - cenc_disable_widevine -- If specified, no Widevine cenc DRM will be configured. If --cenc-disable-widevine is set, --cenc-disable-play-ready cannot also be set.
    - cenc_key_to_track_mappings -- The JSON representing a list of StreamingPolicyContentKey. Use @{file} to load from a file. For further information about the JSON structure please refer to swagger documentation on https://docs.microsoft.com/rest/api/media/streamingpolicies/create#streamingpolicycontentkey
    - cenc_play_ready_attributes -- Custom attributes for PlayReady.
    - cenc_play_ready_template -- The custom license acquisition URL template for a customer service to deliver keys to end users. Not needed when using Azure Media Services for issuing keys.
    - cenc_protocols -- Space-separated list of enabled protocols for Common Encryption CENC. Allowed values: Download, Dash, HLS, SmoothStreaming.
    - cenc_widevine_template -- The custom license acquisition URL template for a customer service to deliver keys to end users. Not needed when using Azure Media Services for issuing keys.
    - default_content_key_policy_name -- Default Content Key used by current streaming policy.
    - envelope_clear_tracks -- The JSON representing which tracks should not be encrypted. Use @{file} to load from a file. For further information about the JSON structure please refer to swagger documentation on https://docs.microsoft.com/rest/api/media/streamingpolicies/create#trackselection
    - envelope_default_key_label -- Label used to specify Content Key when creating a streaming locator.
    - envelope_default_key_policy_name -- Policy used by Default Key.
    - envelope_key_to_track_mappings -- The JSON representing a list of StreamingPolicyContentKey. Use @{file} to load from a file. For further information about the JSON structure please refer to swagger documentation on https://docs.microsoft.com/rest/api/media/streamingpolicies/create#streamingpolicycontentkey
    - envelope_protocols -- Space-separated list of enabled protocols for Envelope Encryption. Allowed values: Download, Dash, HLS, SmoothStreaming.
    - envelope_template -- The KeyAcquistionUrlTemplate is used to point to user specified service to delivery content keys.
    - no_encryption_protocols -- Space-separated list of enabled protocols for NoEncryption. Allowed values: Download, Dash, HLS, SmoothStreaming.
    '''
    return _call_az("az ams streaming-policy create", locals())


def list(account_name, resource_group, filter=None, orderby=None, top=None):
    '''
    List all the streaming policies within an Azure Media Services account.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - filter -- Restricts the set of items returned.
    - orderby -- Specifies the key by which the result collection should be ordered.
    - top -- Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
    '''
    return _call_az("az ams streaming-policy list", locals())


def show(account_name, name, resource_group):
    '''
    Show the details of a streaming policy.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the streaming policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams streaming-policy show", locals())


def delete(account_name, name, resource_group):
    '''
    

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the streaming policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams streaming-policy delete", locals())

