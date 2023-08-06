'''
Configure hostnames for a function app.
'''
from .... pyaz_utils import _call_az

def add(hostname, name, resource_group, slot=None):
    '''
    Bind a hostname to a function app.

    Required Parameters:
    - hostname -- hostname assigned to the site, such as custom domains
    - name -- name of the function app.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp config hostname add", locals())


def list(resource_group, webapp_name, slot=None):
    '''
    List all hostname bindings for a function app.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - webapp_name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp config hostname list", locals())


def delete(hostname, name, resource_group, slot=None):
    '''
    Unbind a hostname from a function app.

    Required Parameters:
    - hostname -- hostname assigned to the site, such as custom domains
    - name -- name of the function app.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp config hostname delete", locals())


def get_external_ip(name, resource_group):
    '''
    Get the external-facing IP address for a function app.

    Required Parameters:
    - name -- name of the function app.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az functionapp config hostname get-external-ip", locals())

