from .... pyaz_utils import _call_az

def add(name, repo, resource_group, branch=None, force=None, login_with_github=None, runtime=None, slot=None, token=None):
    '''
    Add a GitHub Actions workflow file to the specified repository. The workflow will build and deploy your app to the specified webapp.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - repo -- The GitHub repository to which the workflow file will be added. In the format: <owner>/<repository-name>
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - branch -- The branch to which the workflow file will be added. Defaults to "master" if not specified.
    - force -- When true, the command will overwrite any workflow file with a conflicting name.
    - login_with_github -- Interactively log in with Github to retrieve the Personal Access Token
    - runtime -- Canonicalized web runtime in the format of Framework|Version, e.g. "PHP|5.6". Use "az webapp list-runtimes" for available list.
    - slot -- The name of the slot. Default to the production slot if not specified.
    - token -- A Personal Access Token with write access to the specified repository. For more information: https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line
    '''
    return _call_az("az webapp deployment github-actions add", locals())


def remove(name, repo, resource_group, branch=None, login_with_github=None, slot=None, token=None):
    '''
    Remove and disconnect the GitHub Actions workflow file from the specified repository.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - repo -- The GitHub repository to which the workflow file will be added. In the format: <owner>/<repository-name>
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - branch -- The branch to which the workflow file will be added. Defaults to "master" if not specified.
    - login_with_github -- Interactively log in with Github to retrieve the Personal Access Token
    - slot -- The name of the slot. Default to the production slot if not specified.
    - token -- A Personal Access Token with write access to the specified repository. For more information: https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line
    '''
    return _call_az("az webapp deployment github-actions remove", locals())

