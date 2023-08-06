from .. pyaz_utils import _call_az

def on():
    '''
    Turn on local context
    '''
    return _call_az("az local-context on", locals())


def off():
    '''
    Turn off local context
    '''
    return _call_az("az local-context off", locals())


def show(name=None):
    '''
    Show local context data

    Optional Parameters:
    - name -- Space-separated list of local context parameter names.
    '''
    return _call_az("az local-context show", locals())


def delete(all=None, name=None, purge=None, recursive=None, yes=None):
    '''
    Delete local context data

    Optional Parameters:
    - all -- Clear all local context data. Either --name or --all can be specified.
    - name -- Space-separated list of local context parameter names. Either --name or --all can be specified.
    - purge -- Delete local context file from working directory. Only available when --all is specified.
    - recursive -- Indicate this is recursive delete of local context. Only available when --all is specified.
    - yes -- Do not prompt for confirmation. Only available when --all is specified.
    '''
    return _call_az("az local-context delete", locals())

