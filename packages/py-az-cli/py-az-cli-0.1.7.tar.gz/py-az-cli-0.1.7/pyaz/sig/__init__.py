'''
manage shared image gallery
'''
from .. pyaz_utils import _call_az
from . import gallery_application, image_definition, image_version, share


def create(gallery_name, resource_group, description=None, location=None, permissions=None, soft_delete=None, tags=None):
    '''
    Create a shared image gallery.

    Required Parameters:
    - gallery_name -- gallery name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - description -- the description of the gallery
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - permissions -- This property allows you to specify the permission of sharing gallery.
    - soft_delete -- Enable soft-deletion for resources in this gallery, allowing them to be recovered within retention time.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az sig create", locals())


def show(gallery_name, resource_group, select=None):
    '''
    

    Required Parameters:
    - gallery_name -- gallery name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - select -- The select expression to apply on the operation.
    '''
    return _call_az("az sig show", locals())


def list(resource_group=None):
    '''
    list share image galleries.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sig list", locals())


def delete(gallery_name, resource_group):
    '''
    

    Required Parameters:
    - gallery_name -- gallery name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sig delete", locals())


def update(gallery_name, resource_group, add=None, force_string=None, permissions=None, remove=None, select=None, set=None, soft_delete=None):
    '''
    update a share image gallery.

    Required Parameters:
    - gallery_name -- gallery name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - permissions -- This property allows you to specify the permission of sharing gallery.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - select -- The select expression to apply on the operation.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - soft_delete -- Enable soft-deletion for resources in this gallery, allowing them to be recovered within retention time.
    '''
    return _call_az("az sig update", locals())


def list_shared(location, shared_to=None):
    '''
    List all galleries shared directly to your subscription or tenant (preview).

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.

    Optional Parameters:
    - shared_to -- The query parameter to decide what shared galleries to fetch when doing listing operations. If not specified, list by subscription id.
    '''
    return _call_az("az sig list-shared", locals())


def show_shared(gallery_unique_name, location):
    '''
    Get a gallery that has been shared directly to your subscription or tenant (preview).

    Required Parameters:
    - gallery_unique_name -- The unique name of the Shared Gallery.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az sig show-shared", locals())

