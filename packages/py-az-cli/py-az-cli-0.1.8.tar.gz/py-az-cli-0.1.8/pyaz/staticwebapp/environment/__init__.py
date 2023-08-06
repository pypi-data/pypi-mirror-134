'''
Manage environment of the static app.
'''
from ... pyaz_utils import _call_az

def list(name, resource_group=None):
    '''
    List all environment of the static app including production.

    Required Parameters:
    - name -- Name of the static site

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp environment list", locals())


def show(name, environment_name=None, resource_group=None):
    '''
    Show information about the production environment or the specified environment.

    Required Parameters:
    - name -- Name of the static site

    Optional Parameters:
    - environment_name -- Name of the environment of static site
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp environment show", locals())


def functions(name, environment_name=None, resource_group=None):
    '''
    Show information about functions.

    Required Parameters:
    - name -- Name of the static site

    Optional Parameters:
    - environment_name -- Name of the environment of static site
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp environment functions", locals())


def delete(name, environment_name=None, resource_group=None, yes=None):
    '''
    Delete the static app production environment or the specified environment.

    Required Parameters:
    - name -- Name of the static site

    Optional Parameters:
    - environment_name -- Name of the environment of static site
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az staticwebapp environment delete", locals())

