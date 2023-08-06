from .... pyaz_utils import _call_az

def create(gateway_name, name, public_cert_data, resource_group):
    '''
    Upload a root certificate.

    Required Parameters:
    - gateway_name -- Virtual network gateway name
    - name -- Root certificate name
    - public_cert_data -- Base64 contents of the root certificate file or file path.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet-gateway root-cert create", locals())


def delete(gateway_name, name, resource_group):
    '''
    Delete a root certificate.

    Required Parameters:
    - gateway_name -- Virtual network gateway name
    - name -- Root certificate name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet-gateway root-cert delete", locals())

