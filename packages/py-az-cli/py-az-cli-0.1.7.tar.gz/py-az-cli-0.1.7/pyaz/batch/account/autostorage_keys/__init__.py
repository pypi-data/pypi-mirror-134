from .... pyaz_utils import _call_az

def sync(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Name of the Batch account.
    - resource_group -- Name of the resource group
    '''
    return _call_az("az batch account autostorage-keys sync", locals())

