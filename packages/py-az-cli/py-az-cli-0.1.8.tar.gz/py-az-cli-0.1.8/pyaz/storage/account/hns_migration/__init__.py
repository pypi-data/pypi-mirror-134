from .... pyaz_utils import _call_az

def start(name, type, no_wait=None, resource_group=None):
    '''
    Validate/Begin migrating a storage account to enable hierarchical namespace.

    Required Parameters:
    - name -- The storage account name.
    - type -- Start a validation request for migration or start a migration request

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account hns-migration start", locals())


def stop(name, no_wait=None, resource_group=None):
    '''
    Stop the enabling hierarchical namespace migration of a storage account.

    Required Parameters:
    - name -- The storage account name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account hns-migration stop", locals())

