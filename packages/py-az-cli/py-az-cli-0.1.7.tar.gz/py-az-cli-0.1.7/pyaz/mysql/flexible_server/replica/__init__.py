from .... pyaz_utils import _call_az

def list(name, resource_group):
    '''
    List all read replicas for a given server.

    Required Parameters:
    - name -- Name of the source server.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az mysql flexible-server replica list", locals())


def create(replica_name, resource_group, source_server, no_wait=None, zone=None):
    '''
    Create a read replica for a server.

    Required Parameters:
    - replica_name -- The name of the server to restore to.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source_server -- The name or resource ID of the source server to restore from.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - zone -- Availability zone into which to provision the resource.
    '''
    return _call_az("az mysql flexible-server replica create", locals())


def stop_replication(name, resource_group, yes=None):
    '''
    Stop replication to a read replica and make it a read/write server.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az mysql flexible-server replica stop-replication", locals())

