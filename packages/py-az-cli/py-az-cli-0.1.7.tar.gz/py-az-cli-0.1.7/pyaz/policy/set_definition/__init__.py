from ... pyaz_utils import _call_az

def create(definitions, name, definition_groups=None, description=None, display_name=None, management_group=None, metadata=None, params=None, subscription=None):
    '''
    Create a policy set definition.

    Required Parameters:
    - definitions -- JSON formatted string or a path to a file or uri containing definitions.
    - name -- Name of the new policy set definition.

    Optional Parameters:
    - definition_groups -- JSON formatted string or a path to a file or uri containing policy definition groups. Groups are used to organize policy definitions within a policy set.
    - description -- Description of policy set definition.
    - display_name -- Display name of policy set definition.
    - management_group -- The name of the management group of the policy [set] definition.
    - metadata -- Metadata in space-separated key=value pairs.
    - params -- JSON formatted string or a path to a file or uri with parameter definitions.
    - subscription -- The subscription id of the policy [set] definition.
    '''
    return _call_az("az policy set-definition create", locals())


def delete(name, management_group=None, subscription=None):
    '''
    Delete a policy set definition.

    Required Parameters:
    - name -- The policy set definition name.

    Optional Parameters:
    - management_group -- The name of the management group of the policy [set] definition.
    - subscription -- The subscription id of the policy [set] definition.
    '''
    return _call_az("az policy set-definition delete", locals())


def list(management_group=None, subscription=None):
    '''
    List policy set definitions.

    Optional Parameters:
    - management_group -- The name of the management group of the policy [set] definition.
    - subscription -- The subscription id of the policy [set] definition.
    '''
    return _call_az("az policy set-definition list", locals())


def show(name, management_group=None, subscription=None):
    '''
    Show a policy set definition.

    Required Parameters:
    - name -- The policy set definition name.

    Optional Parameters:
    - management_group -- The name of the management group of the policy [set] definition.
    - subscription -- The subscription id of the policy [set] definition.
    '''
    return _call_az("az policy set-definition show", locals())


def update(name, definition_groups=None, definitions=None, description=None, display_name=None, management_group=None, metadata=None, params=None, subscription=None):
    '''
    Update a policy set definition.

    Required Parameters:
    - name -- The policy set definition name.

    Optional Parameters:
    - definition_groups -- JSON formatted string or a path to a file or uri containing policy definition groups. Groups are used to organize policy definitions within a policy set.
    - definitions -- JSON formatted string or a path to a file or uri containing definitions.
    - description -- Description of policy set definition.
    - display_name -- Display name of policy set definition.
    - management_group -- The name of the management group of the policy [set] definition.
    - metadata -- Metadata in space-separated key=value pairs.
    - params -- JSON formatted string or a path to a file or uri with parameter definitions.
    - subscription -- The subscription id of the policy [set] definition.
    '''
    return _call_az("az policy set-definition update", locals())

