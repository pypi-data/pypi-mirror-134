from .... pyaz_utils import _call_az

def create(endpoint_name, endpoint_resource_group, endpoint_subscription_id, endpoint_type, hub_name, auth_type=None, batch_frequency=None, chunk_size=None, connection_string=None, container_name=None, encoding=None, endpoint_uri=None, entity_path=None, file_name_format=None, identity=None, resource_group=None):
    '''
    Add an endpoint to your IoT Hub.

    Required Parameters:
    - endpoint_name -- Name of the Routing Endpoint.
    - endpoint_resource_group -- Resource group of the Endpoint resoure.
    - endpoint_subscription_id -- SubscriptionId of the Endpoint resource.
    - endpoint_type -- Type of the Routing Endpoint.
    - hub_name -- IoT Hub name.

    Optional Parameters:
    - auth_type -- Authentication type for the endpoint. The default is keyBased.
    - batch_frequency -- Request batch frequency in seconds. The maximum amount of time that can elapse before data is written to a blob, between 60 and 720 seconds.
    - chunk_size -- Request chunk size in megabytes(MB). The maximum size of blobs, between 10 and 500 MB.
    - connection_string -- Connection string of the Routing Endpoint.
    - container_name -- Name of the storage container.
    - encoding -- Encoding format for the container. The default is AVRO. Note that this field is applicable only for blob container endpoints.
    - endpoint_uri -- The uri of the endpoint resource.
    - entity_path -- The entity path of the endpoint resource.
    - file_name_format -- File name format for the blob. The file name format must contain {iothub}, {partition}, {YYYY}, {MM}, {DD}, {HH} and {mm} fields. All parameters are mandatory but can be reordered with or without delimiters.
    - identity -- Use a system-assigned or user-assigned managed identity for endpoint authentication. Use "[system]" to refer to the system-assigned identity or a resource ID to refer to a user-assigned identity. If you use --auth-type without this parameter, system-assigned managed identity is assumed.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub routing-endpoint create", locals())


def show(endpoint_name, hub_name, resource_group=None):
    '''
    Get information on mentioned endpoint for your IoT Hub.

    Required Parameters:
    - endpoint_name -- Name of the Routing Endpoint.
    - hub_name -- IoT Hub name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub routing-endpoint show", locals())


def list(hub_name, endpoint_type=None, resource_group=None):
    '''
    Get information on all the endpoints for your IoT Hub.

    Required Parameters:
    - hub_name -- IoT Hub name.

    Optional Parameters:
    - endpoint_type -- Type of the Routing Endpoint.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub routing-endpoint list", locals())


def delete(hub_name, endpoint_name=None, endpoint_type=None, resource_group=None):
    '''
    Delete all or mentioned endpoint for your IoT Hub.

    Required Parameters:
    - hub_name -- IoT Hub name.

    Optional Parameters:
    - endpoint_name -- Name of the Routing Endpoint.
    - endpoint_type -- Type of the Routing Endpoint.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub routing-endpoint delete", locals())

