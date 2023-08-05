'''
Manage Azure API Management Product's.
'''
from ... pyaz_utils import _call_az
from . import api


def list(resource_group, service_name):
    '''
    Lists a collection of products in the specified service instance.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the api management service instance
    '''
    return _call_az("az apim product list", locals())


def show(product_id, resource_group, service_name):
    '''
    Gets the details of the product specified by its identifier.

    Required Parameters:
    - product_id -- Product identifier. Must be unique in the current API Management service instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the api management service instance
    '''
    return _call_az("az apim product show", locals())


def create(product_name, resource_group, service_name, approval_required=None, description=None, legal_terms=None, no_wait=None, product_id=None, state=None, subscription_required=None, subscriptions_limit=None):
    '''
    Creates a product.

    Required Parameters:
    - product_name -- Product name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the api management service instance

    Optional Parameters:
    - approval_required -- whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.
    - description -- Product description. May include HTML formatting tags.
    - legal_terms -- Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.
    - no_wait -- Do not wait for the long-running operation to finish.
    - product_id -- Product identifier. Must be unique in the current API Management service instance.
    - state -- whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished. Possible values include: 'notPublished', 'published'
    - subscription_required -- Whether a product subscription is required for accessing APIs included in this product.
    - subscriptions_limit -- Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.
    '''
    return _call_az("az apim product create", locals())


def update(product_id, resource_group, service_name, add=None, approval_required=None, description=None, force_string=None, if_match=None, legal_terms=None, no_wait=None, product_name=None, remove=None, set=None, state=None, subscription_required=None, subscriptions_limit=None):
    '''
    Update existing product details.

    Required Parameters:
    - product_id -- Product identifier. Must be unique in the current API Management service instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the api management service instance

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - approval_required -- whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.
    - description -- Product description. May include HTML formatting tags.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - if_match -- ETag of the Entity.
    - legal_terms -- Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.
    - no_wait -- Do not wait for the long-running operation to finish.
    - product_name -- Product name.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - state -- whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished. Possible values include: 'notPublished', 'published'
    - subscription_required -- Whether a product subscription is required for accessing APIs included in this product.
    - subscriptions_limit -- Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.
    '''
    return _call_az("az apim product update", locals())


def delete(product_id, resource_group, service_name, delete_subscriptions=None, if_match=None, no_wait=None, yes=None):
    '''
    Delete product.

    Required Parameters:
    - product_id -- Product identifier. Must be unique in the current API Management service instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the api management service instance

    Optional Parameters:
    - delete_subscriptions -- Delete existing subscriptions associated with the product or not.
    - if_match -- ETag of the Entity.
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az apim product delete", locals())


def wait(product_id, resource_group, service_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of an apim product is met.

    Required Parameters:
    - product_id -- Product identifier. Must be unique in the current API Management service instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the api management service instance

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az apim product wait", locals())

