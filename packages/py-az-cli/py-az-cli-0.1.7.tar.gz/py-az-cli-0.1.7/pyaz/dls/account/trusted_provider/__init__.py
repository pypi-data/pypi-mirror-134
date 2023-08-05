from .... pyaz_utils import _call_az

def create(account, id_provider, trusted_id_provider_name, resource_group=None):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - id_provider -- The URL of this trusted identity provider.
    - trusted_id_provider_name -- The name of the trusted identity provider. This is used for differentiation of providers in the account.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Store account.
    '''
    return _call_az("az dls account trusted-provider create", locals())


def update(account, trusted_id_provider_name, id_provider=None, resource_group=None):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - trusted_id_provider_name -- The name of the trusted identity provider. This is used for differentiation of providers in the account.

    Optional Parameters:
    - id_provider -- The URL of this trusted identity provider.
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Store account.
    '''
    return _call_az("az dls account trusted-provider update", locals())


def list(account, resource_group=None):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Store account.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Store account.
    '''
    return _call_az("az dls account trusted-provider list", locals())


def show(account, trusted_id_provider_name, resource_group=None):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - trusted_id_provider_name -- The name of the trusted identity provider to retrieve.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Store account.
    '''
    return _call_az("az dls account trusted-provider show", locals())


def delete(account, trusted_id_provider_name, resource_group=None):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - trusted_id_provider_name -- The name of the trusted identity provider to delete.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Store account.
    '''
    return _call_az("az dls account trusted-provider delete", locals())

