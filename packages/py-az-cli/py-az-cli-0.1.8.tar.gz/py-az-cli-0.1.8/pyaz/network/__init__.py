'''
Manage Azure Network resources.
'''
from .. pyaz_utils import _call_az
from . import application_gateway, asg, bastion, cross_region_lb, ddos_protection, dns, express_route, lb, local_gateway, nic, nsg, private_endpoint, private_endpoint_connection, private_link_resource, private_link_service, profile, public_ip, route_filter, route_table, routeserver, security_partner_provider, service_endpoint, virtual_appliance, vnet, vnet_gateway, vpn_connection, vrouter, watcher


def list_usages(location):
    '''
    List the number of network resources in a region that are used against a subscription quota.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az network list-usages", locals())


def list_service_tags(location):
    '''
    List all service tags which are below to different resources

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az network list-service-tags", locals())


def list_service_aliases(location, resource_group=None):
    '''
    List available service aliases in the region which can be used for Service Endpoint Policies.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network list-service-aliases", locals())

