from ... pyaz_utils import _call_az

def list(account_name, asset_name, resource_group):
    '''
    List all the asset filters of an Azure Media Services account.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - asset_name -- The name of the asset.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams asset-filter list", locals())


def show(account_name, asset_name, name, resource_group):
    '''
    Show the details of an asset filter.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - asset_name -- The name of the asset.
    - name -- The name of the asset filter.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams asset-filter show", locals())


def delete(account_name, asset_name, name, resource_group):
    '''
    Delete an asset filter.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - asset_name -- The name of the asset.
    - name -- The name of the asset filter.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams asset-filter delete", locals())


def create(account_name, asset_name, name, resource_group, bitrate=None, end_timestamp=None, first_quality=None, force_end_timestamp=None, live_backoff_duration=None, presentation_window_duration=None, start_timestamp=None, timescale=None, tracks=None):
    '''
    Create an asset filter.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - asset_name -- The name of the asset.
    - name -- The name of the asset filter.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - bitrate -- The first quality bitrate.
    - end_timestamp -- Applies to Video on Demand (VoD).For the Live Streaming presentation, it is silently ignored and applied when the presentation ends and the stream becomes VoD.This is a long value that represents an absolute end point of the presentation, rounded to the closest next GOP start. The unit is the timescale, so an endTimestamp of 1800000000 would be for 3 minutes.Use startTimestamp and endTimestamp to trim the fragments that will be in the playlist (manifest).For example, startTimestamp=40000000 and endTimestamp=100000000 using the default timescale will generate a playlist that contains fragments from between 4 seconds and 10 seconds of the VoD presentation. If a fragment straddles the boundary, the entire fragment will be included in the manifest.
    - first_quality -- The first quality (lowest) bitrate to include in the manifest.
    - force_end_timestamp -- Applies to Live Streaming only. Indicates whether the endTimestamp property must be present. If true, endTimestamp must be specified or a bad request code is returned. Allowed values: false, true.
    - live_backoff_duration -- Applies to Live Streaming only. This value defines the latest live position that a client can seek to. Using this property, you can delay live playback position and create a server-side buffer for players. The unit for this property is timescale (see below). The maximum live back off duration is 300 seconds (3000000000). For example, a value of 2000000000 means that the latest available content is 20 seconds delayed from the real live edge.
    - presentation_window_duration -- Applies to Live Streaming only.Use presentationWindowDuration to apply a sliding window of fragments to include in a playlist.The unit for this property is timescale (see below).For example, set presentationWindowDuration=1200000000 to apply a two-minute sliding window. Media within 2 minutes of the live edge will be included in the playlist. If a fragment straddles the boundary, the entire fragment will be included in the playlist. The minimum presentation window duration is 60 seconds.
    - start_timestamp -- Applies to Video on Demand (VoD) or Live Streaming. This is a long value that represents an absolute start point of the stream. The value gets rounded to the closest next GOP start. The unit is the timescale, so a startTimestamp of 150000000 would be for 15 seconds. Use startTimestamp and endTimestampp to trim the fragments that will be in the playlist (manifest). For example, startTimestamp=40000000 and endTimestamp=100000000 using the default timescale will generate a playlist that contains fragments from between 4 seconds and 10 seconds of the VoD presentation. If a fragment straddles the boundary, the entire fragment will be included in the manifest.
    - timescale -- Applies to all timestamps and durations in a Presentation Time Range, specified as the number of increments in one second.Default is 10000000 - ten million increments in one second, where each increment would be 100 nanoseconds long. For example, if you want to set a startTimestamp at 30 seconds, you would use a value of 300000000 when using the default timescale.
    - tracks -- The JSON representing the track selections. Use @{file} to load from a file. For further information about the JSON structure please refer to swagger documentation on https://docs.microsoft.com/rest/api/media/assetfilters/createorupdate#filtertrackselection
    '''
    return _call_az("az ams asset-filter create", locals())


def update(account_name, asset_name, name, resource_group, add=None, bitrate=None, end_timestamp=None, first_quality=None, force_end_timestamp=None, force_string=None, live_backoff_duration=None, presentation_window_duration=None, remove=None, set=None, start_timestamp=None, timescale=None, tracks=None):
    '''
    Update the details of an asset filter.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - asset_name -- The name of the asset.
    - name -- The name of the asset filter.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - bitrate -- The first quality bitrate.
    - end_timestamp -- Applies to Video on Demand (VoD).For the Live Streaming presentation, it is silently ignored and applied when the presentation ends and the stream becomes VoD.This is a long value that represents an absolute end point of the presentation, rounded to the closest next GOP start. The unit is the timescale, so an endTimestamp of 1800000000 would be for 3 minutes.Use startTimestamp and endTimestamp to trim the fragments that will be in the playlist (manifest).For example, startTimestamp=40000000 and endTimestamp=100000000 using the default timescale will generate a playlist that contains fragments from between 4 seconds and 10 seconds of the VoD presentation. If a fragment straddles the boundary, the entire fragment will be included in the manifest.
    - first_quality -- The first quality (lowest) bitrate to include in the manifest.
    - force_end_timestamp -- Applies to Live Streaming only. Indicates whether the endTimestamp property must be present. If true, endTimestamp must be specified or a bad request code is returned. Allowed values: false, true.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - live_backoff_duration -- Applies to Live Streaming only. This value defines the latest live position that a client can seek to. Using this property, you can delay live playback position and create a server-side buffer for players. The unit for this property is timescale (see below). The maximum live back off duration is 300 seconds (3000000000). For example, a value of 2000000000 means that the latest available content is 20 seconds delayed from the real live edge.
    - presentation_window_duration -- Applies to Live Streaming only.Use presentationWindowDuration to apply a sliding window of fragments to include in a playlist.The unit for this property is timescale (see below).For example, set presentationWindowDuration=1200000000 to apply a two-minute sliding window. Media within 2 minutes of the live edge will be included in the playlist. If a fragment straddles the boundary, the entire fragment will be included in the playlist. The minimum presentation window duration is 60 seconds.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - start_timestamp -- Applies to Video on Demand (VoD) or Live Streaming. This is a long value that represents an absolute start point of the stream. The value gets rounded to the closest next GOP start. The unit is the timescale, so a startTimestamp of 150000000 would be for 15 seconds. Use startTimestamp and endTimestampp to trim the fragments that will be in the playlist (manifest). For example, startTimestamp=40000000 and endTimestamp=100000000 using the default timescale will generate a playlist that contains fragments from between 4 seconds and 10 seconds of the VoD presentation. If a fragment straddles the boundary, the entire fragment will be included in the manifest.
    - timescale -- Applies to all timestamps and durations in a Presentation Time Range, specified as the number of increments in one second.Default is 10000000 - ten million increments in one second, where each increment would be 100 nanoseconds long. For example, if you want to set a startTimestamp at 30 seconds, you would use a value of 300000000 when using the default timescale.
    - tracks -- The JSON representing the track selections. Use @{file} to load from a file. For further information about the JSON structure please refer to swagger documentation on https://docs.microsoft.com/rest/api/media/assetfilters/createorupdate#filtertrackselection
    '''
    return _call_az("az ams asset-filter update", locals())

