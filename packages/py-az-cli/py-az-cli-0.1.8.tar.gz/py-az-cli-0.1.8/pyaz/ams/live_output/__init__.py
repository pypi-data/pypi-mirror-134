from ... pyaz_utils import _call_az

def create(account_name, archive_window_length, asset_name, live_event_name, name, resource_group, description=None, fragments_per_ts_segment=None, manifest_name=None, output_snap_time=None):
    '''
    Create a live output.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - archive_window_length -- ISO 8601 timespan duration of the archive window length. This is the duration that customer want to retain the recorded content. Minimum window is 5 minutes (PT5M or 00:05:00). Maximum window is 25 hours (PT25H or 25:00:00). For example, to retain the output for 10 minutes, use PT10M or 00:10:00
    - asset_name -- The name of the asset.
    - live_event_name -- The name of the live event.
    - name -- The name of the live output.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - description -- The live output description.
    - fragments_per_ts_segment -- The number of fragments per HLS segment.
    - manifest_name -- The manifest file name. If not provided, the service will generate one automatically.
    - output_snap_time -- The output snapshot time.
    '''
    return _call_az("az ams live-output create", locals())


def show(account_name, live_event_name, name, resource_group):
    '''
    Show the details of a live output.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - live_event_name -- The name of the live event.
    - name -- The name of the live output.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams live-output show", locals())


def list(account_name, live_event_name, resource_group):
    '''
    List all the live outputs in a live event.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - live_event_name -- The name of the live event.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams live-output list", locals())


def delete(account_name, live_event_name, name, resource_group):
    '''
    Delete a live output.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - live_event_name -- The name of the live event.
    - name -- The name of the live output.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams live-output delete", locals())

