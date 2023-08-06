'''
Manage Synapse's triggers.
'''
from ... pyaz_utils import _call_az

def create(file, name, workspace_name, no_wait=None):
    '''
    Create a trigger.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The trigger name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse trigger create", locals())


def set(file, name, workspace_name, no_wait=None):
    '''
    Update an exist trigger.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The trigger name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse trigger set", locals())


def update(file, name, workspace_name, no_wait=None):
    '''
    Update an exist trigger.

    Required Parameters:
    - file -- Properties may be supplied from a JSON file using the `@{path}` syntax or a JSON string.
    - name -- The trigger name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse trigger update", locals())


def list(workspace_name):
    '''
    List triggers.

    Required Parameters:
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse trigger list", locals())


def show(name, workspace_name):
    '''
    Get a trigger.

    Required Parameters:
    - name -- The trigger name.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse trigger show", locals())


def delete(name, workspace_name, no_wait=None, yes=None):
    '''
    Delete a trigger.

    Required Parameters:
    - name -- The trigger name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse trigger delete", locals())


def subscribe_to_event(name, workspace_name, no_wait=None):
    '''
    Subscribe event trigger to events.

    Required Parameters:
    - name -- The trigger name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse trigger subscribe-to-event", locals())


def get_event_subscription_status(name, workspace_name):
    '''
    Get a trigger's event subscription status.

    Required Parameters:
    - name -- The trigger name.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse trigger get-event-subscription-status", locals())


def unsubscribe_from_event(name, workspace_name, no_wait=None):
    '''
    Unsubscribe event trigger from events.

    Required Parameters:
    - name -- The trigger name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse trigger unsubscribe-from-event", locals())


def start(name, workspace_name, no_wait=None):
    '''
    Starts a trigger.

    Required Parameters:
    - name -- The trigger name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse trigger start", locals())


def stop(name, workspace_name, no_wait=None):
    '''
    Stops a trigger.

    Required Parameters:
    - name -- The trigger name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse trigger stop", locals())


def wait(name, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of a trigger is met.

    Required Parameters:
    - name -- The trigger name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az synapse trigger wait", locals())

