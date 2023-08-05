from .... pyaz_utils import _call_az

def list(database_rid, instance_id, location):
    '''
    List all the versions of all the mongodb collections that were created / modified / deleted in the given database and restorable account.

    Required Parameters:
    - database_rid -- Rid of the database
    - instance_id -- InstanceId of the Account
    - location -- Location
    '''
    return _call_az("az cosmosdb mongodb restorable-collection list", locals())

