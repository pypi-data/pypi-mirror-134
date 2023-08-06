'''
Manage Azure API Management API Revision.
'''
from .... pyaz_utils import _call_az

def list(api_id, resource_group, service_name):
    '''
    Lists all revisions of an API.

    Required Parameters:
    - api_id -- API identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.
    '''
    return _call_az("az apim api revision list", locals())


def create(api_id, api_revision, resource_group, service_name, api_revision_description=None):
    '''
    Create API revision.

    Required Parameters:
    - api_id -- API identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - api_revision -- Describes the Revision of the Api.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.

    Optional Parameters:
    - api_revision_description -- Description of the Api Revision.
    '''
    return _call_az("az apim api revision create", locals())

