'''
Manage appliations for VM
'''
from ... pyaz_utils import _call_az

def set(app_version_ids, name, resource_group, app_config_overrides=None, order_applications=None):
    '''
    Set appliations for VM.

    Required Parameters:
    - app_version_ids -- Space-separated application version ids to set to VM.
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - app_config_overrides -- Space-separated application configuration overrides for each application version ids. It should have the same number of items as the application version ids. Null is available for a application which does not have a configuration override.
    - order_applications -- Whether set order index at each gallery applications, the order index starts from 1.
    '''
    return _call_az("az vm application set", locals())


def list(resource_group, vm_name):
    '''
    List applications for VM

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    '''
    return _call_az("az vm application list", locals())

