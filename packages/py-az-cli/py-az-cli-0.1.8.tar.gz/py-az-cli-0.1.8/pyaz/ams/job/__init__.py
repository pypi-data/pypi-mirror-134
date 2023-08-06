'''
Manage jobs for a transform.
'''
from ... pyaz_utils import _call_az

def show(account_name, name, resource_group, transform_name):
    '''
    Show the details of a job.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the job.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - transform_name -- The name of the transform.
    '''
    return _call_az("az ams job show", locals())


def list(account_name, resource_group, transform_name, filter=None, orderby=None):
    '''
    List all the jobs of a transform within an Azure Media Services account.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - transform_name -- The name of the transform.

    Optional Parameters:
    - filter -- Restricts the set of items returned.
    - orderby -- Specifies the key by which the result collection should be ordered.
    '''
    return _call_az("az ams job list", locals())


def delete(account_name, name, resource_group, transform_name):
    '''
    Delete a job.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the job.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - transform_name -- The name of the transform.
    '''
    return _call_az("az ams job delete", locals())


def cancel(account_name, name, resource_group, transform_name, delete=None):
    '''
    Cancel a job.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the job.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - transform_name -- The name of the transform.

    Optional Parameters:
    - delete -- Delete the job being cancelled.
    '''
    return _call_az("az ams job cancel", locals())


def start(account_name, name, output_assets, resource_group, transform_name, base_uri=None, correlation_data=None, description=None, files=None, input_asset_name=None, label=None, priority=None):
    '''
    Start a job.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the job.
    - output_assets -- Space-separated assets in 'assetName=label' format. An asset without label can be sent like this: 'assetName='
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - transform_name -- The name of the transform.

    Optional Parameters:
    - base_uri -- Base uri for http job input. It will be concatenated with provided file names. If no base uri is given, then the provided file list is assumed to be fully qualified uris.
    - correlation_data -- Space-separated correlation data in 'key[=value]' format. This customer provided data will be returned in Job and JobOutput state events.
    - description -- The job description.
    - files -- Space-separated list of files. It can be used to tell the service to only use the files specified from the input asset.
    - input_asset_name -- The name of the input asset.
    - label -- A label that is assigned to a Job Input that is used to satisfy a reference used in the Transform. For example, a Transform can be authored to take an image file with the label 'xyz' and apply it as an overlay onto the input video before it is encoded. When submitting a Job, exactly one of the JobInputs should be the image file, and it should have the label 'xyz'.
    - priority -- The priority with which the job should be processed.
    '''
    return _call_az("az ams job start", locals())


def update(account_name, name, resource_group, transform_name, add=None, description=None, force_string=None, priority=None, remove=None, set=None):
    '''
    Update an existing job.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the job.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - transform_name -- The name of the transform.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - description -- The job description.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - priority -- The priority with which the job should be processed.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az ams job update", locals())

