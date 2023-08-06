'''
Manage partner registrations.
'''
from .... pyaz_utils import _call_az

def show(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Name of the partner registration.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid partner registration show", locals())


def delete(name, resource_group, yes=None):
    '''
    

    Required Parameters:
    - name -- Name of the partner registration.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az eventgrid partner registration delete", locals())


def list(odata_query=None, resource_group=None):
    '''
    List all partner registrations in specific resource group or all under the specified azure subscription.

    Optional Parameters:
    - odata_query -- The OData query used for filtering the list results. Filtering is currently allowed on the Name property only. The supported operations include: CONTAINS, eq (for equal), ne (for not equal), AND, OR and NOT.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid partner registration list", locals())


def create(name, partner_name, resource_group, resource_type_name, authorized_subscription_ids=None, customer_service_extension=None, customer_service_number=None, customer_service_uri=None, description=None, display_name=None, logo_uri=None, long_description=None, setup_uri=None, tags=None):
    '''
    Create a new partner registration.

    Required Parameters:
    - name -- Name of the partner registration.
    - partner_name -- Official name of the partner.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type_name -- Name of the partner topic resource type. This name should be unique among all partner topic types names.

    Optional Parameters:
    - authorized_subscription_ids -- A space-separated list of Azure subscription Ids that are authorized to create a partner namespace associated with this partner registration. This is an optional property. Creating partner namespaces is always permitted under the same Azure subscription as the one used for creating the partner registration.
    - customer_service_extension -- The extension of the customer service number of the publisher. Only digits are allowed and number of digits should not exceed 10.
    - customer_service_number -- The customer service number of the publisher. The expected phone format should start with a '+' sign followed by the country code. The remaining digits are then followed. Only digits and spaces are allowed and its length cannot exceed 16 digits including country code. Examples of valid phone numbers are: +1 515 123 4567 and +966 7 5115 2471. Examples of invalid phone numbers are: +1 (515) 123-4567, 1 515 123 4567 and +966 121 5115 24 7 551 1234 43.
    - customer_service_uri -- The customer service URI of the publisher.
    - description -- Description of the partner topic type.
    - display_name -- Display name for the partner topic type.
    - logo_uri -- URI of the partner logo.
    - long_description -- Description of the custom scenarios and integration. Length of this description should not exceed 2048 characters
    - setup_uri -- URI of the partner website that can be used by Azure customers to setup Event Grid integration on an event source.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az eventgrid partner registration create", locals())

