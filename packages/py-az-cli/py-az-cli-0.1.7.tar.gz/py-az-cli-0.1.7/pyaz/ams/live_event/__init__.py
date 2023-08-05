from ... pyaz_utils import _call_az

def create(account_name, ips, name, resource_group, streaming_protocol, access_token=None, alternative_media_id=None, auto_start=None, client_access_policy=None, cross_domain_policy=None, description=None, encoding_type=None, hostname_prefix=None, key_frame_interval=None, key_frame_interval_duration=None, no_wait=None, preset_name=None, preview_ips=None, preview_locator=None, stream_options=None, streaming_policy_name=None, stretch_mode=None, tags=None, transcription_lang=None, use_static_hostname=None):
    '''
    Create a live event.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - ips -- Space-separated IP addresses for access control. Allowed IP addresses can be specified as either a single IP address (e.g. "10.0.0.1") or as an IP range using an IP address and a CIDR subnet mask (e.g. "10.0.0.1/22"). Use "" to clear existing list. Use "AllowAll" to allow all IP addresses. Allowing all IPs is not recommended for production environments.
    - name -- The name of the live event.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - streaming_protocol -- The streaming protocol for the live event. This value is specified at creation time and cannot be updated.

    Optional Parameters:
    - access_token -- A unique identifier for a stream. This can be specified at creation time but cannot be updated. If omitted, the service will generate a unique value.
    - alternative_media_id -- An Alternative Media Identifier associated with the StreamingLocator created for the preview. This value is specified at creation time and cannot be updated. The identifier can be used in the CustomLicenseAcquisitionUrlTemplate or the CustomKeyAcquisitionUrlTemplate of the StreamingPolicy specified in the StreamingPolicyName field.
    - auto_start -- The flag indicates if the resource should be automatically started on creation.
    - client_access_policy -- Filepath to the clientaccesspolicy.xml used by Microsoft Silverlight and Adobe Flash. Use @{file} to load from a file.
    - cross_domain_policy -- Filepath to the crossdomain.xml used by Microsoft Silverlight and Adobe Flash. Use @{file} to load from a file.
    - description -- The live event description.
    - encoding_type -- The encoding type for live event. This value is specified at creation time and cannot be updated. Allowed values: Premium1080p, None, Standard.
    - hostname_prefix -- When useStaticHostname is set to true, hostname_prefix specifies the first part of the hostname assigned to the live event preview and ingest endpoints. The final hostname would be a combination of this prefix, the media service account name and a short code for the Azure Media Services data center.
    - key_frame_interval -- Use an ISO 8601 time value between 0.5 to 20 seconds to specify the output fragment length for the video and audiotracks of an encoding live event. For example, use PT2S to indicate 2 seconds. For the video track it also defines the key frame interval, or the length of a GoP (group of pictures). If this value is not set for anencoding live event, the fragment duration defaults to 2 seconds. The value cannot be set for pass-through live events.
    - key_frame_interval_duration -- ISO 8601 timespan duration of the key frame interval duration in seconds. The value should be an interger in the range of 1 (PT1S or 00:00:01) to 30 (PT30S or 00:00:30) seconds.
    - no_wait -- Do not wait for the long-running operation to finish.
    - preset_name -- The encoding preset name. This value is specified at creation time and cannot be updated.
    - preview_ips -- Space-separated IP addresses for access control. Allowed IP addresses can be specified as either a single IP address (e.g. "10.0.0.1") or as an IP range using an IP address and a CIDR subnet mask (e.g. "10.0.0.1/22"). Use "" to clear existing list. Use "AllowAll" to allow all IP addresses. Allowing all IPs is not recommended for production environments.
    - preview_locator -- The identifier of the preview locator in Guid format. Specifying this at creation time allows the caller to know the preview locator url before the event is created. If omitted, the service will generate a random identifier. This value cannot be updated once the live event is created.
    - stream_options -- The options to use for the LiveEvent. This value is specified at creation time and cannot be updated.
    - streaming_policy_name -- The name of streaming policy used for the live event preview. This can be specified at creation time but cannot be updated.
    - stretch_mode -- Specifies how the input video will be resized to fit the desired output resolution(s). Default is None.  Allowed values: None, AutoSize, AutoFit.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - transcription_lang -- Live transcription language for the live event. Allowed values: ca-ES, da-DK, de-DE, en-AU, en-CA, en-GB, en-IN, en-NZ, en-US, es-ES, es-MX, fi-FI, fr-CA, fr-FR, it-IT, nl-NL, pt-BR, pt-PT, sv-SE See https://go.microsoft.com/fwlink/?linkid=2133742 for more information about the live transcription feature.
    - use_static_hostname -- Specifies whether a static hostname would be assigned to the live event preview and ingest endpoints. This value can only be updated if the live event is in Standby state. If hostname_prefix is not specified, the live event name will be used as the hostname prefix.
    '''
    return _call_az("az ams live-event create", locals())


def start(account_name, name, resource_group, no_wait=None):
    '''
    Start a live event.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the live event.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az ams live-event start", locals())


def standby(account_name, name, resource_group, no_wait=None):
    '''
    Allocate a live event to be started later.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the live event.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az ams live-event standby", locals())


def stop(account_name, name, resource_group, no_wait=None, remove_outputs_on_stop=None):
    '''
    Stop a live event.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the live event.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove_outputs_on_stop -- Remove live outputs on stop.
    '''
    return _call_az("az ams live-event stop", locals())


def reset(account_name, name, resource_group, no_wait=None):
    '''
    Reset a live event.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the live event.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az ams live-event reset", locals())


def show(account_name, name, resource_group):
    '''
    Show the details of a live event.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the live event.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams live-event show", locals())


def delete(account_name, name, resource_group):
    '''
    Delete a live event.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the live event.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams live-event delete", locals())


def list(account_name, resource_group):
    '''
    List all the live events of an Azure Media Services account.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams live-event list", locals())


def update(account_name, name, resource_group, add=None, client_access_policy=None, cross_domain_policy=None, description=None, force_string=None, ips=None, key_frame_interval_duration=None, preview_ips=None, remove=None, set=None, tags=None):
    '''
    Update the details of a live event.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the live event.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - client_access_policy -- Filepath to the clientaccesspolicy.xml used by Microsoft Silverlight and Adobe Flash. Use @{file} to load from a file.
    - cross_domain_policy -- Filepath to the crossdomain.xml used by Microsoft Silverlight and Adobe Flash. Use @{file} to load from a file.
    - description -- The live event description.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - ips -- Space-separated IP addresses for access control. Allowed IP addresses can be specified as either a single IP address (e.g. "10.0.0.1") or as an IP range using an IP address and a CIDR subnet mask (e.g. "10.0.0.1/22"). Use "" to clear existing list. Use "AllowAll" to allow all IP addresses. Allowing all IPs is not recommended for production environments.
    - key_frame_interval_duration -- ISO 8601 timespan duration of the key frame interval duration in seconds. The value should be an interger in the range of 1 (PT1S or 00:00:01) to 30 (PT30S or 00:00:30) seconds.
    - preview_ips -- Space-separated IP addresses for access control. Allowed IP addresses can be specified as either a single IP address (e.g. "10.0.0.1") or as an IP range using an IP address and a CIDR subnet mask (e.g. "10.0.0.1/22"). Use "" to clear existing list. Use "AllowAll" to allow all IP addresses. Allowing all IPs is not recommended for production environments.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az ams live-event update", locals())


def wait(account_name, name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the live event is met.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the live event.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az ams live-event wait", locals())

