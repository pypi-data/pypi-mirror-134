from .... pyaz_utils import _call_az

def create(gateway_name, name, resource_group, thumbprint):
    '''
    Revoke a certificate.

    Required Parameters:
    - gateway_name -- Virtual network gateway name
    - name -- Root certificate name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - thumbprint -- Certificate thumbprint.
    '''
    return _call_az("az network vnet-gateway revoked-cert create", locals())


def delete(gateway_name, name, resource_group):
    '''
    Delete a revoked certificate.

    Required Parameters:
    - gateway_name -- Virtual network gateway name
    - name -- Root certificate name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet-gateway revoked-cert delete", locals())

