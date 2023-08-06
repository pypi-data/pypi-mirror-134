'''
Manage custom hostnames of Functions of the static app.
'''
from ... pyaz_utils import _call_az

def list(name, resource_group=None):
    '''
    List custom hostnames of the static app.

    Required Parameters:
    - name -- Name of the static site

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp hostname list", locals())


def set(hostname, name, no_wait=None, resource_group=None, validation_method=None):
    '''
    Set given sub-domain hostname to the static app. Please configure CNAME/TXT/ALIAS record with your DNS provider. Use --no-wait to not wait for validation.

    Required Parameters:
    - hostname -- custom hostname such as www.example.com. Only support sub domain in preview.
    - name -- Name of the static site

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - validation_method -- Validation method for the custom domain.
    '''
    return _call_az("az staticwebapp hostname set", locals())


def delete(hostname, name, no_wait=None, resource_group=None, yes=None):
    '''
    Delete given hostname of the static app.

    Required Parameters:
    - hostname -- custom hostname such as www.example.com. Only support sub domain in preview.
    - name -- Name of the static site

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az staticwebapp hostname delete", locals())


def show(hostname, name, resource_group):
    '''
    Get details for a staticwebapp custom domain. Can be used to fetch validation token for TXT domain validation (see example).

    Required Parameters:
    - hostname -- custom hostname such as www.example.com. Only support sub domain in preview.
    - name -- Name of the static site
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp hostname show", locals())

