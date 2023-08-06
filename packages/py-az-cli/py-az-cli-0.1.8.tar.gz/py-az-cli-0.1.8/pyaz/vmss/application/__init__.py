'''
manage applications for VM scale set.
'''
from ... pyaz_utils import _call_az

def set(app_version_ids, name, resource_group, app_config_overrides=None, order_applications=None):
    '''
    Set applications for VMSS.

    Required Parameters:
    - app_version_ids -- Space-separated application version ids to set to VM.
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - app_config_overrides -- Space-separated application configuration overrides for each application version ids. It should have the same number of items as the application version ids. Null is available for a application which does not have a configuration override.
    - order_applications -- Whether set order index at each gallery applications, the order index starts from 1.
    '''
    return _call_az("az vmss application set", locals())


def list(name, resource_group):
    '''
    List applications for VMSS

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vmss application list", locals())

