from ... pyaz_utils import _call_az

def create(gallery_image_definition, gallery_name, offer, os_type, publisher, resource_group, sku, description=None, disallowed_disk_types=None, end_of_life_date=None, eula=None, features=None, hyper_v_generation=None, location=None, maximum_cpu_core=None, maximum_memory=None, minimum_cpu_core=None, minimum_memory=None, os_state=None, plan_name=None, plan_product=None, plan_publisher=None, privacy_statement_uri=None, release_note_uri=None, tags=None):
    '''
    create a gallery image definition

    Required Parameters:
    - gallery_image_definition -- gallery image definition
    - gallery_name -- gallery name
    - offer -- image offer
    - os_type -- the type of the OS that is included in the disk if creating a VM from user-image or a specialized VHD
    - publisher -- image publisher
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku -- image sku

    Optional Parameters:
    - description -- the description of the gallery image definition
    - disallowed_disk_types -- disk types which would not work with the image, e.g., Standard_LRS
    - end_of_life_date -- the end of life date, e.g. '2020-12-31'
    - eula -- The Eula agreement for the gallery image
    - features -- A list of gallery image features. E.g. "IsSecureBootSupported=true IsMeasuredBootSupported=false"
    - hyper_v_generation -- The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - maximum_cpu_core -- maximum cpu cores
    - maximum_memory -- maximum memory in MB
    - minimum_cpu_core -- minimum cpu cores
    - minimum_memory -- minimum memory in MB
    - os_state -- This property allows the user to specify whether the virtual machines created under this image are 'Generalized' or 'Specialized'.
    - plan_name -- plan name
    - plan_product -- plan product
    - plan_publisher -- plan publisher
    - privacy_statement_uri -- The privacy statement uri
    - release_note_uri -- The release note uri
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az sig image-definition create", locals())


def list(gallery_name, resource_group):
    '''
    

    Required Parameters:
    - gallery_name -- gallery name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sig image-definition list", locals())


def show(gallery_image_definition, gallery_name, resource_group):
    '''
    

    Required Parameters:
    - gallery_image_definition -- gallery image definition
    - gallery_name -- gallery name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sig image-definition show", locals())


def delete(gallery_image_definition, gallery_name, resource_group):
    '''
    

    Required Parameters:
    - gallery_image_definition -- gallery image definition
    - gallery_name -- gallery name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sig image-definition delete", locals())


def update(gallery_image_definition, gallery_name, resource_group, add=None, force_string=None, remove=None, set=None):
    '''
    Update a VM Image definition.

    Required Parameters:
    - gallery_image_definition -- gallery image definition
    - gallery_name -- gallery name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az sig image-definition update", locals())


def list_shared(gallery_unique_name, location, shared_to=None):
    '''
    List VM Image definitions in a gallery shared directly to your subscription or tenant (preview).

    Required Parameters:
    - gallery_unique_name -- The unique name of the Shared Gallery.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.

    Optional Parameters:
    - shared_to -- The query parameter to decide what shared galleries to fetch when doing listing operations. If not specified, list by subscription id.
    '''
    return _call_az("az sig image-definition list-shared", locals())


def show_shared(gallery_image_definition, gallery_unique_name, location):
    '''
    Get a shared gallery image (preview).

    Required Parameters:
    - gallery_image_definition -- The name of the Shared Gallery Image Definition from which the Image Versions are to be listed.
    - gallery_unique_name -- The unique name of the Shared Gallery.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az sig image-definition show-shared", locals())

