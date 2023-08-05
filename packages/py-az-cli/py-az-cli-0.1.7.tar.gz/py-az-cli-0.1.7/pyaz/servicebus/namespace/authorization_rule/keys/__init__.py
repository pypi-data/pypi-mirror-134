from ..... pyaz_utils import _call_az

def list(name, namespace_name, resource_group):
    '''
    List the keys and connection strings of Authorization Rule for Service Bus Namespace

    Required Parameters:
    - name -- Name of Namespace Authorization Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az servicebus namespace authorization-rule keys list", locals())


def renew(key, name, namespace_name, resource_group):
    '''
    Regenerate keys of Authorization Rule for the Service Bus Namespace.

    Required Parameters:
    - key -- specifies Primary or Secondary key needs to be reset
    - name -- Name of Namespace Authorization Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az servicebus namespace authorization-rule keys renew", locals())

