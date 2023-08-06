'''
Manage shared access keys of a topic.
'''
from .... pyaz_utils import _call_az

def list(name, resource_group):
    '''
    List shared access keys of a topic.

    Required Parameters:
    - name -- Name of the topic
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid topic key list", locals())


def regenerate(key_name, name, resource_group):
    '''
    Regenerate a shared access key of a topic.

    Required Parameters:
    - key_name -- Key name to regenerate key1 or key2
    - name -- Name of the topic
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid topic key regenerate", locals())

