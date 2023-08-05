'''
Configure SSL certificates.
'''
from .... pyaz_utils import _call_az

def upload(certificate_file, certificate_password, name, resource_group, slot=None):
    '''
    Upload an SSL certificate to a function app.

    Required Parameters:
    - certificate_file -- The filepath for the .pfx file
    - certificate_password -- The ssl cert password
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- The name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp config ssl upload", locals())


def list(resource_group):
    '''
    List SSL certificates for a function app.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az functionapp config ssl list", locals())


def show(certificate_name, resource_group):
    '''
    Show the details of an SSL certificate for a function app.

    Required Parameters:
    - certificate_name -- The name of the certificate
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az functionapp config ssl show", locals())


def bind(certificate_thumbprint, name, resource_group, ssl_type, slot=None):
    '''
    Bind an SSL certificate to a function app.

    Required Parameters:
    - certificate_thumbprint -- The ssl cert thumbprint
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - ssl_type -- The ssl cert type

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp config ssl bind", locals())


def unbind(certificate_thumbprint, name, resource_group, slot=None):
    '''
    Unbind an SSL certificate from a function app.

    Required Parameters:
    - certificate_thumbprint -- The ssl cert thumbprint
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp config ssl unbind", locals())


def delete(certificate_thumbprint, resource_group):
    '''
    Delete an SSL certificate from a function app.

    Required Parameters:
    - certificate_thumbprint -- The ssl cert thumbprint
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az functionapp config ssl delete", locals())


def import_(key_vault, key_vault_certificate_name, name, resource_group):
    '''
    Import an SSL certificate to a function app from Key Vault.

    Required Parameters:
    - key_vault -- The name or resource ID of the Key Vault
    - key_vault_certificate_name -- The name of the certificate in Key Vault
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az functionapp config ssl import", locals())


def create(hostname, name, resource_group, slot=None):
    '''
    Create a Managed Certificate for a hostname in a function app.

    Required Parameters:
    - hostname -- The custom domain name
    - name -- Name of the web app.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp config ssl create", locals())

