from ... pyaz_utils import _call_az

def on():
    '''
    Turn on parameter persistence.
    '''
    return _call_az("az config param-persist on", locals())


def off():
    '''
    Turn off parameter persistence.
    '''
    return _call_az("az config param-persist off", locals())


def show():
    '''
    Show parameter persistence data.
    '''
    return _call_az("az config param-persist show", locals())


def delete(all=None, purge=None, recursive=None, yes=None):
    '''
    Delete parameter persistence data.

    Optional Parameters:
    - all -- Clear all parameter persistence data. Either positional name argument  or --all can be specified.
    - purge -- Delete parameter persistence file from working directory. Only available when --all is specified.
    - recursive -- Indicate this is recursive delete of parameter persistence. Only available when --all is specified.
    - yes -- Do not prompt for confirmation. Only available when --all is specified.
    '''
    return _call_az("az config param-persist delete", locals())

