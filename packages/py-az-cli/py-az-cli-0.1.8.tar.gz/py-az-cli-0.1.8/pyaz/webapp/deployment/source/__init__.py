'''
Manage web app deployment via source control.
'''
from .... pyaz_utils import _call_az

def config_local_git(name, resource_group, slot=None):
    '''
    Get a URL for a git repository endpoint to clone and push to for web app deployment.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp deployment source config-local-git", locals())


def config_zip(name, resource_group, src, slot=None, timeout=None):
    '''
    Perform deployment using the kudu zip push deployment for a web app.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - src -- a zip file path for deployment

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    - timeout -- Configurable timeout in seconds for checking the status of deployment
    '''
    return _call_az("az webapp deployment source config-zip", locals())


def config(name, repo_url, resource_group, branch=None, git_token=None, github_action=None, manual_integration=None, repository_type=None, slot=None):
    '''
    Manage deployment from git or Mercurial repositories.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - repo_url -- repository url to pull the latest source from, e.g. https://github.com/foo/foo-web
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - branch -- the branch name of the repository
    - git_token -- Git access token required for auto sync
    - github_action -- If using github action, default to False
    - manual_integration -- disable automatic sync between source control and web
    - repository_type -- repository type
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp deployment source config", locals())


def sync(name, resource_group, slot=None):
    '''
    Synchronize from the repository. Only needed under manual integration mode.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp deployment source sync", locals())


def show(name, resource_group, slot=None):
    '''
    Get the details of a source control deployment configuration.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp deployment source show", locals())


def delete(name, resource_group, slot=None):
    '''
    Delete a source control deployment configuration.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp deployment source delete", locals())


def update_token(git_token=None):
    '''
    

    Optional Parameters:
    - git_token -- Git access token required for auto sync
    '''
    return _call_az("az webapp deployment source update-token", locals())

