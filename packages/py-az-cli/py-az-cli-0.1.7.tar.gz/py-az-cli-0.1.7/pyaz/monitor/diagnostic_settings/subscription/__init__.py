from .... pyaz_utils import _call_az

def create(location, logs, name, event_hub_auth_rule=None, event_hub_name=None, service_bus_rule=None, storage_account=None, workspace=None):
    '''
    Create diagnostic settings for a subscription

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - logs -- JSON encoded list of logs settings. Use '@{file}' to load from a file.
    - name -- The name of the diagnostic setting.

    Optional Parameters:
    - event_hub_auth_rule -- The resource Id for the event hub authorization rule.
    - event_hub_name -- The name of the event hub. If none is specified, the default event hub will be selected.
    - service_bus_rule -- The service bus rule ID of the service bus namespace in which you would like to have Event Hubs created for streaming the Activity Log. The rule ID is of the format '{service bus resource ID}/authorizationrules/{key name}'.
    - storage_account -- The resource id of the storage account to which you would like to send the Activity Log.
    - workspace -- The resource id of the log analytics workspace.
    '''
    return _call_az("az monitor diagnostic-settings subscription create", locals())


def delete(name, subscription_id=None, yes=None):
    '''
    

    Required Parameters:
    - name -- The name of the diagnostic setting.

    Optional Parameters:
    - subscription_id -- ==SUPPRESS==
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az monitor diagnostic-settings subscription delete", locals())


def show(name, subscription_id=None):
    '''
    

    Required Parameters:
    - name -- The name of the diagnostic setting.

    Optional Parameters:
    - subscription_id -- ==SUPPRESS==
    '''
    return _call_az("az monitor diagnostic-settings subscription show", locals())


def list(subscription_id=None):
    '''
    

    Optional Parameters:
    - subscription_id -- ==SUPPRESS==
    '''
    return _call_az("az monitor diagnostic-settings subscription list", locals())


def update(name, add=None, event_hub_auth_rule=None, event_hub_name=None, force_string=None, logs=None, remove=None, service_bus_rule=None, set=None, storage_account=None, subscription_id=None, workspace=None):
    '''
    Update diagnostic settings for a subscription.

    Required Parameters:
    - name -- The name of the diagnostic setting.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - event_hub_auth_rule -- The resource Id for the event hub authorization rule.
    - event_hub_name -- The name of the event hub. If none is specified, the default event hub will be selected.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - logs -- JSON encoded list of logs settings. Use '@{file}' to load from a file.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - service_bus_rule -- The service bus rule ID of the service bus namespace in which you would like to have Event Hubs created for streaming the Activity Log. The rule ID is of the format '{service bus resource ID}/authorizationrules/{key name}'.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - storage_account -- The resource id of the storage account to which you would like to send the Activity Log.
    - subscription_id -- ==SUPPRESS==
    - workspace -- The resource id of the log analytics workspace.
    '''
    return _call_az("az monitor diagnostic-settings subscription update", locals())

