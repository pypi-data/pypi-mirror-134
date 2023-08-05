from .... pyaz_utils import _call_az

def add(data, gateway_name, name, resource_group):
    '''
    Add trusted client certificate of the application gateway.

    Required Parameters:
    - data -- Certificate public data.
    - gateway_name -- Name of the application gateway.
    - name -- Name of the trusted client certificate that is unique within an Application Gateway
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway client-cert add", locals())


def remove(gateway_name, name, resource_group):
    '''
    Remove an existing trusted client certificate of the application gateway.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- Name of the trusted client certificate that is unique within an Application Gateway
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway client-cert remove", locals())


def list(gateway_name, resource_group):
    '''
    List the existing trusted client certificate of the application gateway.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway client-cert list", locals())


def show(gateway_name, name, resource_group):
    '''
    Show an existing trusted client certificate of the application gateway.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- Name of the trusted client certificate that is unique within an Application Gateway
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway client-cert show", locals())


def update(data, gateway_name, name, resource_group):
    '''
    Update trusted client certificate of the application gateway.

    Required Parameters:
    - data -- Certificate public data.
    - gateway_name -- Name of the application gateway.
    - name -- Name of the trusted client certificate that is unique within an Application Gateway
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway client-cert update", locals())

