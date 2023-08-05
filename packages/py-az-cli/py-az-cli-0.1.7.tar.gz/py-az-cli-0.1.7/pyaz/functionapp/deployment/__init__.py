'''
Manage function app deployments.
'''
from ... pyaz_utils import _call_az
from . import container, slot, source, user


def list_publishing_profiles(name, resource_group, slot=None, xml=None):
    '''
    Get the details for available function app deployment profiles.

    Required Parameters:
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    - xml -- retrieves the publishing profile details in XML format
    '''
    return _call_az("az functionapp deployment list-publishing-profiles", locals())


def list_publishing_credentials(name, resource_group, slot=None):
    '''
    Get the details for available function app publishing credentials.

    Required Parameters:
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp deployment list-publishing-credentials", locals())

