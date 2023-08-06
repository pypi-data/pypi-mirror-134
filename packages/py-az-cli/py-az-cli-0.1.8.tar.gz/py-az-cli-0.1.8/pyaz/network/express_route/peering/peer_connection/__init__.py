from ..... pyaz_utils import _call_az

def show(circuit_name, name, peering_name, resource_group):
    '''
    

    Required Parameters:
    - circuit_name -- ExpressRoute circuit name.
    - name -- Name of the peering peer-connection.
    - peering_name -- Name of BGP peering (i.e. AzurePrivatePeering).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route peering peer-connection show", locals())


def list(circuit_name, peering_name, resource_group):
    '''
    

    Required Parameters:
    - circuit_name -- ExpressRoute circuit name.
    - peering_name -- Name of BGP peering (i.e. AzurePrivatePeering).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route peering peer-connection list", locals())

