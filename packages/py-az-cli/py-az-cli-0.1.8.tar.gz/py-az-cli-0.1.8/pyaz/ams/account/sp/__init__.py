'''
Manage service principal and role based access for an Azure Media Services account.
'''
from .... pyaz_utils import _call_az

def create(account_name, resource_group, name=None, new_sp_name=None, password=None, role=None, xml=None, years=None):
    '''
    Create or update a service principal and configure its access to an Azure Media Services account.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - name -- The app name or app URI to associate the RBAC with. If not present, a default name like '{amsaccountname}-access-sp' will be generated.
    - new_sp_name -- The new app name or app URI to update the RBAC with.
    - password -- The password used to log in. Also known as 'Client Secret'. If not present, a random secret will be generated.
    - role -- The role of the service principal.
    - xml -- Enables xml output format.
    - years -- Number of years for which the secret will be valid. Default: 1 year.
    '''
    return _call_az("az ams account sp create", locals())


def reset_credentials(account_name, resource_group, name=None, password=None, role=None, xml=None, years=None):
    '''
    Generate a new client secret for a service principal configured for an Azure Media Services account.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - name -- The app name or app URI to associate the RBAC with. If not present, a default name like '{amsaccountname}-access-sp' will be generated.
    - password -- The password used to log in. Also known as 'Client Secret'. If not present, a random secret will be generated.
    - role -- The role of the service principal.
    - xml -- Enables xml output format.
    - years -- Number of years for which the secret will be valid. Default: 1 year.
    '''
    return _call_az("az ams account sp reset-credentials", locals())

