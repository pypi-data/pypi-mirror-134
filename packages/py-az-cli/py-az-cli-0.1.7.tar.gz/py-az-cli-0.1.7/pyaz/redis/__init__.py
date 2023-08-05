'''
Manage dedicated Redis caches for your Azure applications.
'''
from .. pyaz_utils import _call_az
from . import firewall_rules, patch_schedule, server_link


def create(location, name, resource_group, sku, vm_size, enable_non_ssl_port=None, minimum_tls_version=None, redis_configuration=None, redis_version=None, replicas_per_master=None, shard_count=None, static_ip=None, subnet_id=None, tags=None, tenant_settings=None, zones=None):
    '''
    Create new Redis Cache instance.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku -- Type of Redis cache.
    - vm_size -- Size of Redis cache to deploy. Basic and Standard Cache sizes start with C. Premium Cache sizes start with P

    Optional Parameters:
    - enable_non_ssl_port -- If specified, then the non-ssl redis server port (6379) will be enabled.
    - minimum_tls_version -- Specifies the TLS version required by clients to connect to cache
    - redis_configuration -- JSON encoded configuration settings. Use @{file} to load from a file.
    - redis_version -- Redis version. Only major version will be used in create/update request with current valid values: (4, 6)
    - replicas_per_master -- The number of replicas to be created per master.
    - shard_count -- The number of shards to be created on a Premium Cluster Cache.
    - static_ip -- Specify a static ip if required for the VNET. If you do not specify a static IP then an IP address is chosen automatically
    - subnet_id -- The full resource ID of a subnet in a virtual network to deploy the redis cache in. Example format /subscriptions/{subid}/resourceGroups/{resourceGroupName}/providers/Microsoft.{Network|ClassicNetwork}/virtualNetworks/vnet1/subnets/subnet1
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tenant_settings -- Space-separated tenant settings in key[=value] format
    - zones -- Space-separated list of availability zones into which to provision the resource.
    '''
    return _call_az("az redis create", locals())


def delete(name, resource_group, yes=None):
    '''
    

    Required Parameters:
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az redis delete", locals())


def export(container, name, prefix, resource_group, file_format=None):
    '''
    Export data stored in a Redis cache.

    Required Parameters:
    - container -- SAS url for container where data needs to be exported to
    - name -- Name of the Redis cache.
    - prefix -- Prefix to use for exported files
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - file_format -- Format of the blob (Currently rdb is the only supported format, with other formats expected in the future)
    '''
    return _call_az("az redis export", locals())


def force_reboot(name, reboot_type, resource_group, shard_id=None):
    '''
    Reboot specified Redis node(s).

    Required Parameters:
    - name -- Name of the Redis cache.
    - reboot_type -- Which Redis node(s) to reboot. Depending on this value data loss is possible.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - shard_id -- If clustering is enabled, the ID of the shard to be rebooted.
    '''
    return _call_az("az redis force-reboot", locals())


def import_method(files, name, resource_group, file_format=None):
    '''
    Import data into Redis cache.

    Required Parameters:
    - files -- SAS url for blobs that needs to be imported
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - file_format -- Format of the blob (Currently rdb is the only supported format, with other formats expected in the future)
    '''
    return _call_az("az redis import-method", locals())


def import_(files, name, resource_group, file_format=None):
    '''
    Import data into a Redis cache.

    Required Parameters:
    - files -- SAS url for blobs that needs to be imported
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - file_format -- Format of the blob (Currently rdb is the only supported format, with other formats expected in the future)
    '''
    return _call_az("az redis import", locals())


def list(resource_group=None):
    '''
    List Redis Caches.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az redis list", locals())


def list_keys(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az redis list-keys", locals())


def regenerate_keys(key_type, name, resource_group):
    '''
    Regenerate Redis cache's access keys.

    Required Parameters:
    - key_type -- The Redis access key to regenerate.
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az redis regenerate-keys", locals())


def show(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az redis show", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None, sku=None, vm_size=None):
    '''
    Update a Redis cache.

    Required Parameters:
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sku -- Type of Redis cache.
    - vm_size -- Size of Redis cache to deploy. Basic and Standard Cache sizes start with C. Premium Cache sizes start with P
    '''
    return _call_az("az redis update", locals())

