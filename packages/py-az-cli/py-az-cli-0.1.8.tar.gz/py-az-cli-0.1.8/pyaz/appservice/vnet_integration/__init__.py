from ... pyaz_utils import _call_az

def list(plan, resource_group):
    '''
    list the virtual network integrations used in an appservice plan

    Required Parameters:
    - plan -- AppService plan
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az appservice vnet-integration list", locals())

