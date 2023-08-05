'''
Manage secrets within the specified profile.
'''
from ... pyaz_utils import _call_az

def show(profile_name, resource_group, secret_name):
    '''
    

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - secret_name -- Name of the secret.
    '''
    return _call_az("az afd secret show", locals())


def delete(profile_name, resource_group, secret_name, yes=None):
    '''
    

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - secret_name -- Name of the secret.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az afd secret delete", locals())


def list(profile_name, resource_group):
    '''
    

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az afd secret list", locals())


def create(profile_name, resource_group, secret_name, secret_source, secret_version=None, use_latest_version=None):
    '''
    Creates a new secret within the specified profile.

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - secret_name -- Name of the secret.
    - secret_source -- ID of the Azure key vault certificate.

    Optional Parameters:
    - secret_version -- Version of the certificate to be used.
    - use_latest_version -- Whether to use the latest version for the certificate.
    '''
    return _call_az("az afd secret create", locals())


def update(profile_name, resource_group, secret_name, secret_source=None, secret_version=None, use_latest_version=None):
    '''
    Update an existing secret within the specified profile.

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - secret_name -- Name of the secret.

    Optional Parameters:
    - secret_source -- ID of the Azure key vault certificate.
    - secret_version -- Version of the certificate to be used.
    - use_latest_version -- Whether to use the latest version for the certificate.
    '''
    return _call_az("az afd secret update", locals())

