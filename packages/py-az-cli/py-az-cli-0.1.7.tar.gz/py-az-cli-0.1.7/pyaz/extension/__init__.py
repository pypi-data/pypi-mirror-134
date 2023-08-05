'''
Manage and update CLI extensions.
'''
from .. pyaz_utils import _call_az

def add(index=None, name=None, pip_extra_index_urls=None, pip_proxy=None, source=None, system=None, upgrade=None, version=None, yes=None):
    '''
    Add an extension.

    Optional Parameters:
    - index -- ==SUPPRESS==
    - name -- Name of extension
    - pip_extra_index_urls -- Space-separated list of extra URLs of package indexes to use. This should point to a repository compliant with PEP 503 (the simple repository API) or a local directory laid out in the same format.
    - pip_proxy -- Proxy for pip to use for extension dependencies in the form of [user:passwd@]proxy.server:port
    - source -- Filepath or URL to an extension
    - system -- None
    - upgrade -- Update the extension if already installed, otherwise just install the extension.
    - version -- The specific version of an extension
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az extension add", locals())


def remove(name):
    '''
    Remove an extension.

    Required Parameters:
    - name -- Name of extension
    '''
    return _call_az("az extension remove", locals())


def list():
    '''
    List the installed extensions.
    '''
    return _call_az("az extension list", locals())


def show(name):
    '''
    Show an extension.

    Required Parameters:
    - name -- Name of extension
    '''
    return _call_az("az extension show", locals())


def list_available(index=None, show_details=None):
    '''
    List publicly available extensions.

    Optional Parameters:
    - index -- ==SUPPRESS==
    - show_details -- Show the raw data from the extension index.
    '''
    return _call_az("az extension list-available", locals())


def update(name, index=None, pip_extra_index_urls=None, pip_proxy=None):
    '''
    Update an extension.

    Required Parameters:
    - name -- Name of extension

    Optional Parameters:
    - index -- ==SUPPRESS==
    - pip_extra_index_urls -- Space-separated list of extra URLs of package indexes to use. This should point to a repository compliant with PEP 503 (the simple repository API) or a local directory laid out in the same format.
    - pip_proxy -- Proxy for pip to use for extension dependencies in the form of [user:passwd@]proxy.server:port
    '''
    return _call_az("az extension update", locals())


def list_versions(name, index=None):
    '''
    List available versions for an extension.

    Required Parameters:
    - name -- Name of extension

    Optional Parameters:
    - index -- ==SUPPRESS==
    '''
    return _call_az("az extension list-versions", locals())

