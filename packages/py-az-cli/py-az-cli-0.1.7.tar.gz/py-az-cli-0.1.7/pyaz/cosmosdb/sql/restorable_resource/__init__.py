from .... pyaz_utils import _call_az

def list(instance_id, location, restore_location, restore_timestamp):
    '''
    List all the databases and its containers that can be restored in the given account at the given timesamp and region.

    Required Parameters:
    - instance_id -- InstanceId of the Account
    - location -- Azure Location of the account
    - restore_location -- The region of the restore.
    - restore_timestamp -- The timestamp of the restore
    '''
    return _call_az("az cosmosdb sql restorable-resource list", locals())

