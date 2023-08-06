'''
Manage resource policy remediation deployments.
'''
from .... pyaz_utils import _call_az

def list(name, management_group=None, namespace=None, parent=None, resource=None, resource_group=None, resource_type=None):
    '''
    Lists deployments for a resource policy remediation.

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
    return _call_az("az policy remediation deployment list", locals())

