from ... pyaz_utils import _call_az

def cancel(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vmss rolling-upgrade cancel", locals())


def get_latest(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vmss rolling-upgrade get-latest", locals())


def start(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vmss rolling-upgrade start", locals())

