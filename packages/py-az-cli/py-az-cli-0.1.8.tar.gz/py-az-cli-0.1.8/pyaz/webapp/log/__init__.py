'''
Manage web app logs.
'''
from ... pyaz_utils import _call_az
from . import deployment


def tail(name, resource_group, provider=None, slot=None):
    '''
    Start live log tracing for a web app.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - provider -- By default all live traces configured by `az webapp log config` will be shown, but you can scope to certain providers/folders, e.g. 'application', 'http', etc. For details, check out https://github.com/projectkudu/kudu/wiki/Diagnostic-Log-Stream
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp log tail", locals())


def download(name, resource_group, log_file=None, slot=None):
    '''
    Download a web app's log history as a zip file.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - log_file -- the downloaded zipped log file path
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp log download", locals())


def config(name, resource_group, application_logging=None, detailed_error_messages=None, docker_container_logging=None, failed_request_tracing=None, level=None, slot=None, web_server_logging=None):
    '''
    Configure logging for a web app.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - application_logging -- configure application logging
    - detailed_error_messages -- configure detailed error messages
    - docker_container_logging -- configure gathering STDOUT and STDERR output from container
    - failed_request_tracing -- configure failed request tracing
    - level -- logging level
    - slot -- the name of the slot. Default to the productions slot if not specified
    - web_server_logging -- configure Web server logging
    '''
    return _call_az("az webapp log config", locals())


def show(name, resource_group, slot=None):
    '''
    Get the details of a web app's logging configuration.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp log show", locals())

