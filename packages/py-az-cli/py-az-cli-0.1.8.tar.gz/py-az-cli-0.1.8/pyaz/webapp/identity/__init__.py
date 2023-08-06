'''
manage web app's managed identity
'''
from ... pyaz_utils import _call_az

def assign(name, resource_group, identities=None, role=None, scope=None, slot=None):
    '''
    assign managed identity to the web app

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - identities -- Space-separated identities to assign. Use '[system]' to refer to the system assigned identity. Default: '[system]'
    - role -- Role name or id the managed identity will be assigned
    - scope -- The scope the managed identity has access to
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp identity assign", locals())


def show(name, resource_group, slot=None):
    '''
    display web app's managed identity

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp identity show", locals())


def remove(name, resource_group, identities=None, slot=None):
    '''
    Disable web app's managed identity

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - identities -- Space-separated identities to assign. Use '[system]' to refer to the system assigned identity. Default: '[system]'
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp identity remove", locals())

