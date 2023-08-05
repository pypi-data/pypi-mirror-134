'''
Manage static apps.
'''
from .. pyaz_utils import _call_az
from . import appsettings, environment, functions, hostname, identity, secrets, users


def list(resource_group=None):
    '''
    List all static app resources in a subscription, or in resource group if provided

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp list", locals())


def show(name, resource_group=None):
    '''
    Show details of a static app.

    Required Parameters:
    - name -- Name of the static site

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp show", locals())


def create(branch, location, name, resource_group, source, api_location=None, app_location=None, login_with_github=None, no_wait=None, output_location=None, sku=None, tags=None, token=None):
    '''
    Create a static app with content from a GitHub repository URL and on the provided branch. If the repo is under a Github organization, please ensure that the Azure CLI Github App has access to the organization. Access can be requested in the browser when using the "--login-with-github" argument. Access must be granted by the organization's admin.

    Required Parameters:
    - branch -- The target branch in the repository.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- Name of the static site
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source -- URL for the repository of the static site.

    Optional Parameters:
    - api_location -- Location of your Azure Functions code. For example, '/api' represents a folder called 'api'.
    - app_location -- Location of your application code. For example, '/' represents the root of your app, while '/app' represents a directory called 'app'
    - login_with_github -- Interactively log in with Github to retrieve the Personal Access Token
    - no_wait -- Do not wait for the long-running operation to finish.
    - output_location -- The path of your build output relative to your apps location. For example, setting a value of 'build' when your app location is set to '/app' will cause the content at '/app/build' to be served.
    - sku -- The pricing tiers for Static Web App
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - token -- A user's github repository token. This is used to setup the Github Actions workflow file and API secrets. If you need to create a Github Personal Access Token, please run with the '--login-with-github' flag or follow the steps found at the following link:
https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line
    '''
    return _call_az("az staticwebapp create", locals())


def delete(name, no_wait=None, resource_group=None, yes=None):
    '''
    Delete a static app.

    Required Parameters:
    - name -- Name of the static site

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az staticwebapp delete", locals())


def disconnect(name, no_wait=None, resource_group=None):
    '''
    Disconnect source control to enable connecting to a different repo.

    Required Parameters:
    - name -- Name of the static site

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp disconnect", locals())


def reconnect(branch, name, source, login_with_github=None, no_wait=None, resource_group=None, token=None):
    '''
    Connect to a repo and branch following a disconnect command.

    Required Parameters:
    - branch -- The target branch in the repository.
    - name -- Name of the static site
    - source -- URL for the repository of the static site.

    Optional Parameters:
    - login_with_github -- Interactively log in with Github to retrieve the Personal Access Token
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - token -- A user's github repository token. This is used to setup the Github Actions workflow file and API secrets. If you need to create a Github Personal Access Token, please run with the '--login-with-github' flag or follow the steps found at the following link:
https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line
    '''
    return _call_az("az staticwebapp reconnect", locals())


def update(name, branch=None, no_wait=None, sku=None, source=None, tags=None, token=None):
    '''
    Update a static app. Return the app updated.

    Required Parameters:
    - name -- Name of the static site

    Optional Parameters:
    - branch -- The target branch in the repository.
    - no_wait -- Do not wait for the long-running operation to finish.
    - sku -- The pricing tiers for Static Web App
    - source -- URL for the repository of the static site.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - token -- A user's github repository token. This is used to setup the Github Actions workflow file and API secrets. If you need to create a Github Personal Access Token, please run with the '--login-with-github' flag or follow the steps found at the following link:
https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line
    '''
    return _call_az("az staticwebapp update", locals())

