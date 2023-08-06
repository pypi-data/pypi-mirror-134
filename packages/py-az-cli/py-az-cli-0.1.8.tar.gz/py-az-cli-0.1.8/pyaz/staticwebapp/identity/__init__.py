'''
Manage a static web app's managed identity
'''
from ... pyaz_utils import _call_az

def assign(name, resource_group, identities=None, role=None, scope=None):
    '''
    assign managed identity to the static web app

    Required Parameters:
    - name -- Name of the static site
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - identities -- Space-separated identities to assign. Use '[system]' to refer to the system assigned identity. Default: '[system]'
    - role -- Role name or id the managed identity will be assigned
    - scope -- The scope the managed identity has access to
    '''
    return _call_az("az staticwebapp identity assign", locals())


def remove(name, resource_group, identities=None, yes=None):
    '''
    Disable static web app's managed identity

    Required Parameters:
    - name -- Name of the static site
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - identities -- Space-separated identities to assign. Use '[system]' to refer to the system assigned identity. Default: '[system]'
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az staticwebapp identity remove", locals())


def show(name, resource_group):
    '''
    display static web app's managed identity

    Required Parameters:
    - name -- Name of the static site
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp identity show", locals())

