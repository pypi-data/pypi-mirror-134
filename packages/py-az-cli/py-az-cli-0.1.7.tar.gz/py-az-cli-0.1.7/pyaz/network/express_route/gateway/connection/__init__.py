from ..... pyaz_utils import _call_az

def create(gateway_name, name, peering, resource_group, associated=None, authorization_key=None, circuit_name=None, internet_security=None, labels=None, propagated=None, routing_weight=None):
    '''
    Create an ExpressRoute gateway connection.

    Required Parameters:
    - gateway_name -- ExpressRoute gateway name.
    - name -- ExpressRoute connection name.
    - peering -- Name or ID of an ExpressRoute peering.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - associated -- The resource id of route table associated with this routing configuration.
    - authorization_key -- Authorization key to establish the connection.
    - circuit_name -- ExpressRoute circuit name.
    - internet_security -- Enable internet security. A virtual hub can have the ability to propagate a learned default route to this ExpressRoute connection. This ref https://review.docs.microsoft.com/en-us/azure/virtual-wan/effective-routes-virtual-hub?branch=pr-en-us-91866#aboutdefaultroute might be helpful.
    - labels -- Space-separated list of labels for propagated route tables.
    - propagated -- Space-separated list of resource id of propagated route tables.
    - routing_weight -- Routing weight associated with the connection.
    '''
    return _call_az("az network express-route gateway connection create", locals())


def delete(gateway_name, name, resource_group):
    '''
    Delete an ExpressRoute gateway connection.

    Required Parameters:
    - gateway_name -- ExpressRoute gateway name.
    - name -- ExpressRoute connection name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route gateway connection delete", locals())


def list(gateway_name, resource_group):
    '''
    List ExpressRoute gateway connections.

    Required Parameters:
    - gateway_name -- ExpressRoute gateway name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route gateway connection list", locals())


def show(gateway_name, name, resource_group):
    '''
    Get the details of an ExpressRoute gateway connection.

    Required Parameters:
    - gateway_name -- ExpressRoute gateway name.
    - name -- ExpressRoute connection name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route gateway connection show", locals())


def update(gateway_name, name, resource_group, add=None, associated=None, authorization_key=None, circuit_name=None, force_string=None, internet_security=None, labels=None, peering=None, propagated=None, remove=None, routing_weight=None, set=None):
    '''
    Update an ExpressRoute gateway connection.

    Required Parameters:
    - gateway_name -- ExpressRoute gateway name.
    - name -- ExpressRoute connection name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - associated -- The resource id of route table associated with this routing configuration.
    - authorization_key -- Authorization key to establish the connection.
    - circuit_name -- ExpressRoute circuit name.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - internet_security -- Enable internet security. A virtual hub can have the ability to propagate a learned default route to this ExpressRoute connection. This ref https://review.docs.microsoft.com/en-us/azure/virtual-wan/effective-routes-virtual-hub?branch=pr-en-us-91866#aboutdefaultroute might be helpful.
    - labels -- Space-separated list of labels for propagated route tables.
    - peering -- Name or ID of an ExpressRoute peering.
    - propagated -- Space-separated list of resource id of propagated route tables.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - routing_weight -- Routing weight associated with the connection.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network express-route gateway connection update", locals())

