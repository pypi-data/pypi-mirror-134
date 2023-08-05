from .... pyaz_utils import _call_az

def list(database_rid, instance_id, location, end_time=None, start_time=None):
    '''
    List all the versions of all the sql containers that were created / modified / deleted in the given database and restorable account.

    Required Parameters:
    - database_rid -- Rid of the database
    - instance_id -- InstanceId of the Account
    - location -- Location

    Optional Parameters:
    - end_time -- The snapshot create timestamp before which snapshots need to be listed.
    - start_time -- The snapshot create timestamp after which snapshots need to be listed.
    '''
    return _call_az("az cosmosdb sql restorable-container list", locals())

