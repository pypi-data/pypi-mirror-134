'''
Shows the network topology in your subscription.
'''
from ... pyaz_utils import _call_az

def list():
    '''
    Shows the network topology in your subscription.
    '''
    return _call_az("az security topology list", locals())


def show(name, resource_group):
    '''
    Shows the network topology in your subscription.

    Required Parameters:
    - name -- name of the resource to be fetched
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az security topology show", locals())

