'''
Manage Azure resources.
'''
from .. pyaz_utils import _call_az
from . import link, lock


def create(properties, api_version=None, id=None, is_full_object=None, latest_include_preview=None, location=None, name=None, namespace=None, parent=None, resource_group=None, resource_type=None):
    '''
    create a resource.

    Required Parameters:
    - properties -- a JSON-formatted string containing resource properties

    Optional Parameters:
    - api_version -- The api version of the resource (omit for the latest stable version)
    - id -- Resource ID.
    - is_full_object -- Indicate that the properties object includes other options such as location, tags, sku, and/or plan.
    - latest_include_preview -- Indicate that the latest api-version will be used regardless of whether it is preview version (like 2020-01-01-preview) or not. For example, if the supported api-version of resource provider is 2020-01-01-preview and 2019-01-01: when passing in this parameter it will take the latest version 2020-01-01-preview, otherwise it will take the latest stable version 2019-01-01 without passing in this parameter
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The resource name. (Ex: myC)
    - namespace -- Provider namespace (Ex: 'Microsoft.Provider')
    - parent -- The parent path (Ex: 'resA/myA/resB/myB')
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC')
    '''
    return _call_az("az resource create", locals())


def delete(api_version=None, ids=None, latest_include_preview=None, name=None, namespace=None, parent=None, resource_group=None, resource_type=None):
    '''
    Delete a resource.

    Optional Parameters:
    - api_version -- The api version of the resource (omit for the latest stable version)
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - latest_include_preview -- Indicate that the latest api-version will be used regardless of whether it is preview version (like 2020-01-01-preview) or not. For example, if the supported api-version of resource provider is 2020-01-01-preview and 2019-01-01: when passing in this parameter it will take the latest version 2020-01-01-preview, otherwise it will take the latest stable version 2019-01-01 without passing in this parameter
    - name -- The resource name. (Ex: myC)
    - namespace -- Provider namespace (Ex: 'Microsoft.Provider')
    - parent -- The parent path (Ex: 'resA/myA/resB/myB')
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC')
    '''
    return _call_az("az resource delete", locals())


def show(api_version=None, ids=None, include_response_body=None, latest_include_preview=None, name=None, namespace=None, parent=None, resource_group=None, resource_type=None):
    '''
    Get the details of a resource.

    Optional Parameters:
    - api_version -- The api version of the resource (omit for the latest stable version)
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - include_response_body -- Use if the default command output doesn't capture all of the property data.
    - latest_include_preview -- Indicate that the latest api-version will be used regardless of whether it is preview version (like 2020-01-01-preview) or not. For example, if the supported api-version of resource provider is 2020-01-01-preview and 2019-01-01: when passing in this parameter it will take the latest version 2020-01-01-preview, otherwise it will take the latest stable version 2019-01-01 without passing in this parameter
    - name -- The resource name. (Ex: myC)
    - namespace -- Provider namespace (Ex: 'Microsoft.Provider')
    - parent -- The parent path (Ex: 'resA/myA/resB/myB')
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC')
    '''
    return _call_az("az resource show", locals())


def list(location=None, name=None, namespace=None, resource_group=None, resource_type=None, tag=None):
    '''
    List resources.

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The resource name. (Ex: myC)
    - namespace -- Provider namespace (Ex: 'Microsoft.Provider')
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC')
    - tag -- a single tag in 'key[=value]' format. Use '' to clear existing tags.
    '''
    return _call_az("az resource list", locals())


def tag(tags, api_version=None, ids=None, is_incremental=None, latest_include_preview=None, name=None, namespace=None, parent=None, resource_group=None, resource_type=None):
    '''
    Tag a resource.

    Required Parameters:
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.

    Optional Parameters:
    - api_version -- The api version of the resource (omit for the latest stable version)
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - is_incremental -- The option to add tags incrementally without deleting the original tags. If the key of new tag and original tag are duplicated, the original value will be overwritten.
    - latest_include_preview -- Indicate that the latest api-version will be used regardless of whether it is preview version (like 2020-01-01-preview) or not. For example, if the supported api-version of resource provider is 2020-01-01-preview and 2019-01-01: when passing in this parameter it will take the latest version 2020-01-01-preview, otherwise it will take the latest stable version 2019-01-01 without passing in this parameter
    - name -- The resource name. (Ex: myC)
    - namespace -- Provider namespace (Ex: 'Microsoft.Provider')
    - parent -- The parent path (Ex: 'resA/myA/resB/myB')
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC')
    '''
    return _call_az("az resource tag", locals())


def move(destination_group, ids, destination_subscription_id=None):
    '''
    

    Required Parameters:
    - destination_group -- the destination resource group name
    - ids -- the space-separated resource ids to be moved

    Optional Parameters:
    - destination_subscription_id -- the destination subscription identifier
    '''
    return _call_az("az resource move", locals())


def invoke_action(action, api_version=None, ids=None, latest_include_preview=None, name=None, namespace=None, parent=None, request_body=None, resource_group=None, resource_type=None):
    '''
    Invoke an action on the resource.

    Required Parameters:
    - action -- The action that will be invoked on the specified resource

    Optional Parameters:
    - api_version -- The api version of the resource (omit for the latest stable version)
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - latest_include_preview -- Indicate that the latest api-version will be used regardless of whether it is preview version (like 2020-01-01-preview) or not. For example, if the supported api-version of resource provider is 2020-01-01-preview and 2019-01-01: when passing in this parameter it will take the latest version 2020-01-01-preview, otherwise it will take the latest stable version 2019-01-01 without passing in this parameter
    - name -- The resource name. (Ex: myC)
    - namespace -- Provider namespace (Ex: 'Microsoft.Provider')
    - parent -- The parent path (Ex: 'resA/myA/resB/myB')
    - request_body -- JSON encoded parameter arguments for the action that will be passed along in the post request body. Use @{file} to load from a file.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC')
    '''
    return _call_az("az resource invoke-action", locals())


def update(add=None, api_version=None, force_string=None, ids=None, include_response_body=None, latest_include_preview=None, name=None, namespace=None, parent=None, remove=None, resource_group=None, resource_type=None, set=None):
    '''
    Update a resource.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - api_version -- The api version of the resource (omit for the latest stable version)
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - include_response_body -- Use if the default command output doesn't capture all of the property data.
    - latest_include_preview -- Indicate that the latest api-version will be used regardless of whether it is preview version (like 2020-01-01-preview) or not. For example, if the supported api-version of resource provider is 2020-01-01-preview and 2019-01-01: when passing in this parameter it will take the latest version 2020-01-01-preview, otherwise it will take the latest stable version 2019-01-01 without passing in this parameter
    - name -- The resource name. (Ex: myC)
    - namespace -- Provider namespace (Ex: 'Microsoft.Provider')
    - parent -- The parent path (Ex: 'resA/myA/resB/myB')
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC')
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az resource update", locals())


def wait(api_version=None, created=None, custom=None, deleted=None, exists=None, ids=None, include_response_body=None, interval=None, name=None, namespace=None, parent=None, resource_group=None, resource_type=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of a resources is met.

    Optional Parameters:
    - api_version -- The api version of the resource (omit for the latest stable version)
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - include_response_body -- Use if the default command output doesn't capture all of the property data.
    - interval -- polling interval in seconds
    - name -- The resource name. (Ex: myC)
    - namespace -- Provider namespace (Ex: 'Microsoft.Provider')
    - parent -- The parent path (Ex: 'resA/myA/resB/myB')
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC')
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az resource wait", locals())

