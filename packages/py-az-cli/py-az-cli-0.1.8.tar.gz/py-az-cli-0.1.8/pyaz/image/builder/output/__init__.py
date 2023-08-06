'''
Manage image builder template output distributors.
'''
from .... pyaz_utils import _call_az

def add(name, resource_group, artifact_tags=None, gallery_image_definition=None, gallery_name=None, gallery_replication_regions=None, is_vhd=None, managed_image=None, managed_image_location=None, output_name=None):
    '''
    Add an image builder output distributor to an image builder template.

    Required Parameters:
    - name -- The name of the image template.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - artifact_tags -- Tags that will be applied to the output artifact once it has been created by the distributor. space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - gallery_image_definition -- Name or ID of the existing SIG image definition to create the customized image version with.
    - gallery_name -- Shared image gallery name, if image definition name and not ID was provided.
    - gallery_replication_regions -- Space-separated list of regions to replicate the image version into. Defaults to resource group's location.
    - is_vhd -- The output is a VHD distributor.
    - managed_image -- Name or ID of the customized managed image to be created.
    - managed_image_location -- Location where the customized image will be created. Defaults to resource group's location.
    - output_name -- Name of the image builder run output. Defaults to the name of the managed image or sig image definition.
    '''
    return _call_az("az image builder output add", locals())


def remove(name, output_name, resource_group):
    '''
    Remove an image builder output distributor from an image builder template.

    Required Parameters:
    - name -- The name of the image template.
    - output_name -- Name of the image builder run output.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az image builder output remove", locals())


def clear(name, resource_group):
    '''
    Remove all image builder output distributors from an image builder template.

    Required Parameters:
    - name -- The name of the image template.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az image builder output clear", locals())

