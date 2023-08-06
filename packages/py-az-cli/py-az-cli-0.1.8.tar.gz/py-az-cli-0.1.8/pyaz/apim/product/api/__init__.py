'''
Manage Azure API Management Product's APIs.
'''
from .... pyaz_utils import _call_az

def list(product_id, resource_group, service_name):
    '''
    Lists a collection of the APIs associated with a product.

    Required Parameters:
    - product_id -- Product identifier. Must be unique in the current API Management service instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the api management service instance
    '''
    return _call_az("az apim product api list", locals())


def check(api_id, product_id, resource_group, service_name):
    '''
    Checks that API entity specified by identifier is associated with the Product entity.

    Required Parameters:
    - api_id -- API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - product_id -- Product identifier. Must be unique in the current API Management service instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the api management service instance
    '''
    return _call_az("az apim product api check", locals())


def add(api_id, product_id, resource_group, service_name):
    '''
    Add an API to the specified product.

    Required Parameters:
    - api_id -- API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - product_id -- Product identifier. Must be unique in the current API Management service instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the api management service instance
    '''
    return _call_az("az apim product api add", locals())


def delete(api_id, product_id, resource_group, service_name):
    '''
    Deletes the specified API from the specified product.

    Required Parameters:
    - api_id -- API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - product_id -- Product identifier. Must be unique in the current API Management service instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the api management service instance
    '''
    return _call_az("az apim product api delete", locals())

