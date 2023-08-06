'''
View and manage Advanced Threat Protection settings for storage accounts.
'''
from .... pyaz_utils import _call_az

def show(resource_group, storage_account):
    '''
    Display Advanced Threat Protection settings for a storage account.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - storage_account -- Name of an existing storage account.
    '''
    return _call_az("az security atp storage show", locals())


def update(is_enabled, resource_group, storage_account):
    '''
    Toggle status of Advanced Threat Protection for a storage account.

    Required Parameters:
    - is_enabled -- Enable or disable Advanced Threat Protection for a received storage account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - storage_account -- Name of an existing storage account.
    '''
    return _call_az("az security atp storage update", locals())

