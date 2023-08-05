'''
Find the available VM extensions for a subscription and region.
'''
from .... pyaz_utils import _call_az

def show(location, name, publisher, version):
    '''
    Display information for an extension.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- Name of the extension
    - publisher -- Image publisher name
    - version -- Extension version
    '''
    return _call_az("az vm extension image show", locals())


def list_names(location, publisher):
    '''
    List the names of available extensions.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - publisher -- Image publisher name
    '''
    return _call_az("az vm extension image list-names", locals())


def list_versions(location, name, publisher, filter=None, orderby=None, top=None):
    '''
    List the versions for available extensions.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- Name of the extension
    - publisher -- Image publisher name

    Optional Parameters:
    - filter -- The filter to apply on the operation.
    - orderby -- the $orderby odata query option
    - top -- the $top odata query option
    '''
    return _call_az("az vm extension image list-versions", locals())


def list(latest=None, location=None, name=None, publisher=None, version=None):
    '''
    List the information on available extensions.

    Optional Parameters:
    - latest -- Show the latest version only.
    - location -- Image location.
    - name -- Image name
    - publisher -- Image publisher name
    - version -- Extension version
    '''
    return _call_az("az vm extension image list", locals())

