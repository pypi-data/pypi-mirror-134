'''
Manage Azure API Management Named Values.
'''
from ... pyaz_utils import _call_az

def create(display_name, named_value_id, resource_group, service_name, secret=None, tags=None, value=None):
    '''
    Create an API Management Named Value.

    Required Parameters:
    - display_name -- Required. Unique name of NamedValue. It may contain only letters, digits, period, dash, and underscore characters.
    - named_value_id -- Identifier of the NamedValue.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.

    Optional Parameters:
    - secret -- Determines whether the value is a secret and should be encrypted or not. Default value is false.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - value -- Required. Value of the NamedValue. Can contain policy expressions. It may not be empty or consist only of whitespace. This property will not be filled on GET operations! Use /listSecrets POST request to get the value.
    '''
    return _call_az("az apim nv create", locals())


def show(named_value_id, resource_group, service_name):
    '''
    Show details of an API Management Named Value.

    Required Parameters:
    - named_value_id -- Identifier of the NamedValue.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.
    '''
    return _call_az("az apim nv show", locals())


def list(resource_group, service_name):
    '''
    List API Management Named Values.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.
    '''
    return _call_az("az apim nv list", locals())


def delete(named_value_id, resource_group, service_name, yes=None):
    '''
    Delete an API Management Named Value.

    Required Parameters:
    - named_value_id -- Identifier of the NamedValue.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az apim nv delete", locals())


def show_secret(named_value_id, resource_group, service_name):
    '''
    Gets the secret of an API Management Named Value.

    Required Parameters:
    - named_value_id -- Identifier of the NamedValue.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.
    '''
    return _call_az("az apim nv show-secret", locals())


def update(named_value_id, resource_group, service_name, add=None, force_string=None, if_match=None, remove=None, secret=None, set=None, tags=None, value=None):
    '''
    Update an API Management Named Value.

    Required Parameters:
    - named_value_id -- Identifier of the NamedValue.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - if_match -- ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - secret -- Determines whether the value is a secret and should be encrypted or not. Default value is false.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - value -- Required. Value of the NamedValue. Can contain policy expressions. It may not be empty or consist only of whitespace. This property will not be filled on GET operations! Use /listSecrets POST request to get the value.
    '''
    return _call_az("az apim nv update", locals())

