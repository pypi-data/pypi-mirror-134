'''
Manage App Service Environments
'''
from ... pyaz_utils import _call_az

def list(resource_group=None):
    '''
    List app service environments.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az appservice ase list", locals())


def list_addresses(name, resource_group=None):
    '''
    List VIPs associated with an app service environment v2.

    Required Parameters:
    - name -- Name of the app service environment

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az appservice ase list-addresses", locals())


def list_plans(name, resource_group=None):
    '''
    List app service plans associated with an app service environment.

    Required Parameters:
    - name -- Name of the app service environment

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az appservice ase list-plans", locals())


def show(name, resource_group=None):
    '''
    Show details of an app service environment.

    Required Parameters:
    - name -- Name of the app service environment

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az appservice ase show", locals())


def create(name, resource_group, subnet, force_network_security_group=None, force_route_table=None, front_end_scale_factor=None, front_end_sku=None, ignore_network_security_group=None, ignore_route_table=None, ignore_subnet_size_validation=None, kind=None, location=None, no_wait=None, os_preference=None, virtual_ip_type=None, vnet_name=None, zone_redundant=None):
    '''
    Create app service environment.

    Required Parameters:
    - name -- Name of the app service environment
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subnet -- Name or ID of existing subnet. To create vnet and/or subnet                    use `az network vnet [subnet] create`

    Optional Parameters:
    - force_network_security_group -- Override network security group for subnet. Applies to ASEv2 only.
    - force_route_table -- Override route table for subnet. Applies to ASEv2 only.
    - front_end_scale_factor -- Scale of front ends to app service plan instance ratio. Applies to ASEv2 only.
    - front_end_sku -- Size of front end servers. Applies to ASEv2 only.
    - ignore_network_security_group -- Configure network security group manually. Applies to ASEv2 only.
    - ignore_route_table -- Configure route table manually. Applies to ASEv2 only.
    - ignore_subnet_size_validation -- Do not check if subnet is sized according to recommendations.
    - kind -- Specify App Service Environment version
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - os_preference -- Determine if app service environment should start with Linux workers. Applies to ASEv2 only.
    - virtual_ip_type -- Specify if app service environment should be accessible from internet
    - vnet_name -- Name of the vNet. Mandatory if only subnet name is specified.
    - zone_redundant -- Configure App Service Environment as Zone Redundant. Applies to ASEv3 only.
    '''
    return _call_az("az appservice ase create", locals())


def update(name, allow_new_private_endpoint_connections=None, front_end_scale_factor=None, front_end_sku=None, no_wait=None, resource_group=None):
    '''
    Update app service environment.

    Required Parameters:
    - name -- Name of the app service environment

    Optional Parameters:
    - allow_new_private_endpoint_connections -- (ASEv3 only) Configure Apps in App Service Environment to allow new private endpoint connections.
    - front_end_scale_factor -- (ASEv2 only) Scale of front ends to app service plan instance ratio between 5 and 15.
    - front_end_sku -- (ASEv2 only) Size of front end servers.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az appservice ase update", locals())


def delete(name, no_wait=None, resource_group=None, yes=None):
    '''
    Delete app service environment.

    Required Parameters:
    - name -- Name of the app service environment

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az appservice ase delete", locals())


def create_inbound_services(name, resource_group, subnet, skip_dns=None, vnet_name=None):
    '''
    Private DNS Zone for Internal ASEv2.

    Required Parameters:
    - name -- Name of the app service environment
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subnet -- Name or ID of existing subnet for inbound traffic to ASEv3.                    To create vnet and/or subnet use `az network vnet [subnet] create`

    Optional Parameters:
    - skip_dns -- Do not create Private DNS Zone and DNS records.
    - vnet_name -- Name of the vNet. Mandatory if only subnet name is specified.
    '''
    return _call_az("az appservice ase create-inbound-services", locals())

