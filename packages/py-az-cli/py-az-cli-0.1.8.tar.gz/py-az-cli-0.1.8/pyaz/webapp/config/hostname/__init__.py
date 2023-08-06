'''
Configure hostnames for a web app.
'''
from .... pyaz_utils import _call_az

def add(hostname, resource_group, webapp_name, slot=None):
    '''
    Bind a hostname to a web app.

    Required Parameters:
    - hostname -- hostname assigned to the site, such as custom domains
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - webapp_name -- webapp name. You can configure the default using `az configure --defaults web=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config hostname add", locals())


def list(resource_group, webapp_name, slot=None):
    '''
    List all hostname bindings for a web app.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - webapp_name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config hostname list", locals())


def delete(hostname, resource_group, webapp_name, slot=None):
    '''
    Unbind a hostname from a web app.

    Required Parameters:
    - hostname -- hostname assigned to the site, such as custom domains
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - webapp_name -- webapp name. You can configure the default using `az configure --defaults web=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config hostname delete", locals())


def get_external_ip(resource_group, webapp_name):
    '''
    Get the external-facing IP address for a web app.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - webapp_name -- webapp name. You can configure the default using `az configure --defaults web=<name>`
    '''
    return _call_az("az webapp config hostname get-external-ip", locals())

