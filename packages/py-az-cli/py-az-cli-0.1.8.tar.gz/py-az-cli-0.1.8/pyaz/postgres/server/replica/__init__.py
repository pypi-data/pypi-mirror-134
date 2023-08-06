'''
Manage read replicas.
'''
from .... pyaz_utils import _call_az

def list(resource_group, server_name):
    '''
    List all read replicas for a given server.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the master server.
    '''
    return _call_az("az postgres server replica list", locals())


def create(name, resource_group, source_server, location=None, no_wait=None, sku_name=None):
    '''
    Create a read replica for a server.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source_server -- The name or resource ID of the master server to the create replica for.

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. If not provided, the create replica will be in the same location as the master server
    - no_wait -- Do not wait for the long-running operation to finish.
    - sku_name -- The name of the sku. Follows the convention {pricing tier}_{compute generation}_{vCores} in shorthand. Examples: B_Gen5_1, GP_Gen5_4, MO_Gen5_16.
    '''
    return _call_az("az postgres server replica create", locals())


def stop(name, resource_group, yes=None):
    '''
    Stop replication to a read replica and make it a read/write server.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az postgres server replica stop", locals())

