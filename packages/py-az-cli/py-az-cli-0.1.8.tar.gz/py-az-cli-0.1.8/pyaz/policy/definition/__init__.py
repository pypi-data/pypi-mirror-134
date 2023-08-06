'''
Manage resource policy definitions.
'''
from ... pyaz_utils import _call_az

def create(name, description=None, display_name=None, management_group=None, metadata=None, mode=None, params=None, rules=None, subscription=None):
    '''
    Create a policy definition.

    Required Parameters:
    - name -- Name of the new policy definition.

    Optional Parameters:
    - description -- Description of policy definition.
    - display_name -- Display name of policy definition.
    - management_group -- The name of the management group of the policy [set] definition.
    - metadata -- Metadata in space-separated key=value pairs.
    - mode -- Mode of the policy definition, e.g. All, Indexed. Please visit https://aka.ms/azure-policy-mode for more information.
    - params -- JSON formatted string or a path to a file or uri with parameter definitions.
    - rules -- JSON formatted string or a path to a file with such content
    - subscription -- The subscription id of the policy [set] definition.
    '''
    return _call_az("az policy definition create", locals())


def delete(name, management_group=None, subscription=None):
    '''
    Delete a policy definition.

    Required Parameters:
    - name -- The policy definition name.

    Optional Parameters:
    - management_group -- The name of the management group of the policy [set] definition.
    - subscription -- The subscription id of the policy [set] definition.
    '''
    return _call_az("az policy definition delete", locals())


def list(management_group=None, subscription=None):
    '''
    List policy definitions.

    Optional Parameters:
    - management_group -- The name of the management group of the policy [set] definition.
    - subscription -- The subscription id of the policy [set] definition.
    '''
    return _call_az("az policy definition list", locals())


def show(name, management_group=None, subscription=None):
    '''
    Show a policy definition.

    Required Parameters:
    - name -- The policy definition name.

    Optional Parameters:
    - management_group -- The name of the management group of the policy [set] definition.
    - subscription -- The subscription id of the policy [set] definition.
    '''
    return _call_az("az policy definition show", locals())


def update(name, description=None, display_name=None, management_group=None, metadata=None, mode=None, params=None, rules=None, subscription=None):
    '''
    Update a policy definition.

    Required Parameters:
    - name -- The policy definition name.

    Optional Parameters:
    - description -- Description of policy definition.
    - display_name -- Display name of policy definition.
    - management_group -- The name of the management group of the policy [set] definition.
    - metadata -- Metadata in space-separated key=value pairs.
    - mode -- Mode of the policy definition, e.g. All, Indexed. Please visit https://aka.ms/azure-policy-mode for more information.
    - params -- JSON formatted string or a path to a file or uri with parameter definitions.
    - rules -- JSON formatted string or a path to a file with such content
    - subscription -- The subscription id of the policy [set] definition.
    '''
    return _call_az("az policy definition update", locals())

