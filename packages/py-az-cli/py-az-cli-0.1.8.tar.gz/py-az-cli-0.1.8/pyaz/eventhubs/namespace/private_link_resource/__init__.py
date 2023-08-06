from .... pyaz_utils import _call_az

def show(namespace_name, resource_group):
    '''
    Get the private link resources that need to be created for a eventhubs namespace.

    Required Parameters:
    - namespace_name -- Name of the Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs namespace private-link-resource show", locals())

