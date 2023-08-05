from ... pyaz_utils import _call_az

def show(custom_domain_name, profile_name, resource_group):
    '''
    Show the custom domain details.

    Required Parameters:
    - custom_domain_name -- Name of the custom domain.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az afd custom-domain show", locals())


def wait(custom_domain_name, profile_name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the custom domain is met.

    Required Parameters:
    - custom_domain_name -- Name of the custom domain.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az afd custom-domain wait", locals())


def delete(custom_domain_name, profile_name, resource_group, yes=None):
    '''
    Delete a custom domain.

    Required Parameters:
    - custom_domain_name -- Name of the custom domain.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az afd custom-domain delete", locals())


def list(profile_name, resource_group):
    '''
    List all the custom domains within the specified profile.

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az afd custom-domain list", locals())


def create(certificate_type, custom_domain_name, host_name, minimum_tls_version, profile_name, resource_group, azure_dns_zone=None, no_wait=None, secret=None):
    '''
    Create a custom domain within the specified profile.

    Required Parameters:
    - certificate_type -- Defines the source of the SSL certificate.
    - custom_domain_name -- Name of the custom domain.
    - host_name -- The host name of the domain. Must be a domain name.
    - minimum_tls_version -- TLS protocol version that will be used for Https.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - azure_dns_zone -- ID of the Azure DNS zone.
    - no_wait -- Do not wait for the long-running operation to finish.
    - secret -- Name of the azure front door secret.
    '''
    return _call_az("az afd custom-domain create", locals())


def update(custom_domain_name, profile_name, resource_group, azure_dns_zone=None, certificate_type=None, minimum_tls_version=None, secret=None):
    '''
    Update a custom domain within the specified profile.

    Required Parameters:
    - custom_domain_name -- Name of the custom domain.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - azure_dns_zone -- ID of the Azure DNS zone.
    - certificate_type -- Defines the source of the SSL certificate.
    - minimum_tls_version -- TLS protocol version that will be used for Https.
    - secret -- Name of the azure front door secret.
    '''
    return _call_az("az afd custom-domain update", locals())

