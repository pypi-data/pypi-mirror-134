from ... pyaz_utils import _call_az

def list(id=None, name=None, resource_group=None, type=None):
    '''
    List all private link resources.

    Optional Parameters:
    - id -- ID of the resource
    - name -- Name of the resource. If provided, --type and --resource-group must be provided too
    - resource_group -- Name of resource group. If provided, --name and --type must be provided too
    - type -- Type of the resource. If provided, --name and --resource-group must be provided too
    '''
    return _call_az("az network private-link-resource list", locals())

