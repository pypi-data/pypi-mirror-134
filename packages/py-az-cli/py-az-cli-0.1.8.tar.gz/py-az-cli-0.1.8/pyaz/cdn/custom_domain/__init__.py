from ... pyaz_utils import _call_az

def show(endpoint_name, name, profile_name, resource_group):
    '''
    Show details for the custom domain of a CDN.

    Required Parameters:
    - endpoint_name -- Name of the endpoint under the profile which is unique globally.
    - name -- Resource name of the custom domain.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn custom-domain show", locals())


def delete(endpoint_name, name, profile_name, resource_group):
    '''
    Delete the custom domain of a CDN.

    Required Parameters:
    - endpoint_name -- Name of the endpoint under the profile which is unique globally.
    - name -- Resource name of the custom domain.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn custom-domain delete", locals())


def list(endpoint_name, profile_name, resource_group):
    '''
    

    Required Parameters:
    - endpoint_name -- Name of the endpoint under the profile which is unique globally.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn custom-domain list", locals())


def create(endpoint_name, hostname, name, profile_name, resource_group, location=None, tags=None):
    '''
    Create a new custom domain to provide a hostname for a CDN endpoint.

    Required Parameters:
    - endpoint_name -- None
    - hostname -- None
    - name -- Resource name of the custom domain.
    - profile_name -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az cdn custom-domain create", locals())


def enable_https(endpoint_name, name, profile_name, resource_group, min_tls_version=None, user_cert_group_name=None, user_cert_protocol_type=None, user_cert_secret_name=None, user_cert_secret_version=None, user_cert_subscription_id=None, user_cert_vault_name=None):
    '''
    Enable HTTPS for a custom domain. The resource name of the custom domain could be obtained using "az cdn custom-domain list".

    Required Parameters:
    - endpoint_name -- Name of the parent endpoint.
    - name -- Resource name of the custom domain.
    - profile_name -- Name of the parent profile.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - min_tls_version -- The minimum TLS version required for the custom domain.
    - user_cert_group_name -- The resource group of the KeyVault certificate
    - user_cert_protocol_type -- The protocol type of the certificate.
    - user_cert_secret_name -- The secret name of the KeyVault certificate
    - user_cert_secret_version -- The secret version of the KeyVault certificate, If not specified, the "Latest" version will always been used and the deployed certificate will be automatically rotated to the latest version when a newer version of the certificate is available.
    - user_cert_subscription_id -- The subscription id of the KeyVault certificate
    - user_cert_vault_name -- The vault name of the KeyVault certificate
    '''
    return _call_az("az cdn custom-domain enable-https", locals())


def disable_https(endpoint_name, name, profile_name, resource_group):
    '''
    

    Required Parameters:
    - endpoint_name -- Name of the endpoint under the profile which is unique globally.
    - name -- Resource name of the custom domain.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn custom-domain disable-https", locals())

