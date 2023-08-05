'''
Manage AFD profiles.
'''
from ... pyaz_utils import _call_az

def show(profile_name, resource_group):
    '''
    Show details of an AFD profile.

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az afd profile show", locals())


def delete(profile_name, resource_group):
    '''
    Delete an AFD profile.

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az afd profile delete", locals())


def update(profile_name, resource_group, tags):
    '''
    Update an AFD profile.

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az afd profile update", locals())


def list(resource_group=None):
    '''
    List AFD profiles.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az afd profile list", locals())


def create(profile_name, resource_group, sku, tags=None):
    '''
    Create a new AFD profile.

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku -- The pricing tier of the AFD profile.

    Optional Parameters:
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az afd profile create", locals())


def usage(profile_name, resource_group):
    '''
    List resource usage within the specific AFD profile.

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az afd profile usage", locals())

