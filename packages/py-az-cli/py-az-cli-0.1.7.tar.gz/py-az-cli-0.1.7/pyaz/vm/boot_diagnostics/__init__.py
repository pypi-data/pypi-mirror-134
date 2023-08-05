from ... pyaz_utils import _call_az

def disable(name, resource_group):
    '''
    Disable the boot diagnostics on a VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm boot-diagnostics disable", locals())


def enable(name, resource_group, storage=None):
    '''
    Enable the boot diagnostics on a VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - storage -- None
    '''
    return _call_az("az vm boot-diagnostics enable", locals())


def get_boot_log(name, resource_group):
    '''
    Get the boot diagnostics log from a VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm boot-diagnostics get-boot-log", locals())


def get_boot_log_uris(name, resource_group, expire=None):
    '''
    Get SAS URIs for a virtual machine's boot diagnostic logs.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expire -- None
    '''
    return _call_az("az vm boot-diagnostics get-boot-log-uris", locals())

