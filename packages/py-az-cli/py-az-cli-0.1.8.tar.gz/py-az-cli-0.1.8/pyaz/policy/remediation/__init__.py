'''
Manage resource policy remediations.
'''
from ... pyaz_utils import _call_az
from . import deployment


def show(name, management_group=None, namespace=None, parent=None, resource=None, resource_group=None, resource_type=None):
    '''
    Show a resource policy remediation.

    Required Parameters:
    - name -- Name of the remediation.

    Optional Parameters:
    - management_group -- Name of management group.
    - namespace -- Provider namespace (Ex: Microsoft.Provider).
    - parent -- The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
    - resource -- Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- Resource type (Ex: resourceTypeC).
    '''
    return _call_az("az policy remediation show", locals())


def list(management_group=None, namespace=None, parent=None, resource=None, resource_group=None, resource_type=None):
    '''
    List resource policy remediations.

    Optional Parameters:
    - management_group -- Name of management group.
    - namespace -- Provider namespace (Ex: Microsoft.Provider).
    - parent -- The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
    - resource -- Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- Resource type (Ex: resourceTypeC).
    '''
    return _call_az("az policy remediation list", locals())


def delete(name, management_group=None, namespace=None, parent=None, resource=None, resource_group=None, resource_type=None):
    '''
    Delete a resource policy remediation.

    Required Parameters:
    - name -- Name of the remediation.

    Optional Parameters:
    - management_group -- Name of management group.
    - namespace -- Provider namespace (Ex: Microsoft.Provider).
    - parent -- The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
    - resource -- Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- Resource type (Ex: resourceTypeC).
    '''
    return _call_az("az policy remediation delete", locals())


def cancel(name, management_group=None, namespace=None, parent=None, resource=None, resource_group=None, resource_type=None):
    '''
    Cancel a resource policy remediation.

    Required Parameters:
    - name -- Name of the remediation.

    Optional Parameters:
    - management_group -- Name of management group.
    - namespace -- Provider namespace (Ex: Microsoft.Provider).
    - parent -- The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
    - resource -- Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- Resource type (Ex: resourceTypeC).
    '''
    return _call_az("az policy remediation cancel", locals())


def create(name, policy_assignment, definition_reference_id=None, location_filters=None, management_group=None, namespace=None, parent=None, resource=None, resource_discovery_mode=None, resource_group=None, resource_type=None):
    '''
    Create a resource policy remediation.

    Required Parameters:
    - name -- Name of the remediation.
    - policy_assignment -- Name or resource ID of the policy assignment.

    Optional Parameters:
    - definition_reference_id -- Policy definition reference ID inside the policy set definition. Only required when the policy assignment is assigning a policy set definition.
    - location_filters -- Space separated list of resource locations that should be remediated (Ex: centralus westeurope).
    - management_group -- Name of management group.
    - namespace -- Provider namespace (Ex: Microsoft.Provider).
    - parent -- The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
    - resource -- Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
    - resource_discovery_mode -- The way resources to remediate are discovered. Defaults to ExistingNonCompliant if not specified.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- Resource type (Ex: resourceTypeC).
    '''
    return _call_az("az policy remediation create", locals())

