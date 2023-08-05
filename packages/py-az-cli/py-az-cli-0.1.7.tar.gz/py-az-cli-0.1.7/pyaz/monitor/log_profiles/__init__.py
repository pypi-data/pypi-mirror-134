from ... pyaz_utils import _call_az

def create(categories, days, enabled, location, locations, name, service_bus_rule_id=None, storage_account_id=None, tags=None):
    '''
    Create a log profile.

    Required Parameters:
    - categories -- None
    - days -- None
    - enabled -- None
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - locations -- None
    - name -- None

    Optional Parameters:
    - service_bus_rule_id -- None
    - storage_account_id -- None
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az monitor log-profiles create", locals())


def delete(name):
    '''
    

    Required Parameters:
    - name -- The name of the log profile.
    '''
    return _call_az("az monitor log-profiles delete", locals())


def show(name):
    '''
    

    Required Parameters:
    - name -- The name of the log profile.
    '''
    return _call_az("az monitor log-profiles show", locals())


def list():
    return _call_az("az monitor log-profiles list", locals())


def update(name, add=None, force_string=None, remove=None, set=None):
    '''
    Update a log profile.

    Required Parameters:
    - name -- The name of the log profile.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az monitor log-profiles update", locals())

