from .... pyaz_utils import _call_az

def list(gateway_name, resource_group):
    '''
    List SSL certificates.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway ssl-cert list", locals())


def show(gateway_name, name, resource_group):
    '''
    Get the details of an SSL certificate.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the SSL certificate.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway ssl-cert show", locals())


def delete(gateway_name, name, resource_group, no_wait=None):
    '''
    Delete an SSL certificate.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the SSL certificate.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway ssl-cert delete", locals())


def create(gateway_name, name, resource_group, cert_file=None, cert_password=None, key_vault_secret_id=None, no_wait=None):
    '''
    Upload an SSL certificate.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the SSL certificate.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - cert_file -- The path to the PFX certificate file.
    - cert_password -- Certificate password.
    - key_vault_secret_id -- Secret Id of (base-64 encoded unencrypted pfx) 'Secret' or 'Certificate' object stored in Azure KeyVault.
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway ssl-cert create", locals())


def update(gateway_name, name, resource_group, add=None, cert_file=None, cert_password=None, force_string=None, key_vault_secret_id=None, no_wait=None, remove=None, set=None):
    '''
    Update an SSL certificate.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the SSL certificate.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - cert_file -- The path to the PFX certificate file.
    - cert_password -- Certificate password.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - key_vault_secret_id -- Secret Id of (base-64 encoded unencrypted pfx) 'Secret' or 'Certificate' object stored in Azure KeyVault.
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network application-gateway ssl-cert update", locals())

