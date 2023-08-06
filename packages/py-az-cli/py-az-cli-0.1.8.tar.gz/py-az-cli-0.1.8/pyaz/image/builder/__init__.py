'''
Manage and build image builder templates.
'''
from ... pyaz_utils import _call_az
from . import customizer, output


def create(name, resource_group, build_timeout=None, checksum=None, identity=None, image_source=None, image_template=None, location=None, managed_image_destinations=None, no_wait=None, os_disk_size=None, scripts=None, shared_image_destinations=None, subnet=None, tags=None, vm_size=None, vnet=None):
    '''
    Create an image builder template.

    Required Parameters:
    - name -- The name of the image template.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - build_timeout -- The Maximum duration to wait while building the image template, in minutes. Default is 60.
    - checksum -- The SHA256 checksum of the Red Hat ISO image
    - identity -- List of user assigned identities (name or ID, space delimited) of the image template.
    - image_source -- The base image to customize. Must be a valid platform image URN, platform image alias, Red Hat ISO image URI, managed image name/ID, or shared image version ID.
    - image_template -- Local path or URL to an image template file. When using --image-template, all other parameters are ignored except -g and -n. Reference: https://docs.microsoft.com/azure/virtual-machines/linux/image-builder-json
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - managed_image_destinations -- Managed image output distributor information. Space-separated list of key-value pairs. E.g "image_1=westus2 image_2=westus". Each key is the name or resource ID of the managed image to be created. Each value is the location of the image.
    - no_wait -- Do not wait for the long-running operation to finish.
    - os_disk_size -- Size of the OS disk in GB. Omit or specify 0 to use Azure's default OS disk size
    - scripts -- Space-separated list of shell or powershell scripts to customize the image with. Each script must be a publicly accessible URL. Infers type of script from file extension ('.sh' or'.ps1') or from source type. More more customizer options and flexibility, see: 'az image template customizer add'
    - shared_image_destinations -- Shared image gallery (sig) output distributor information. Space-separated list of key-value pairs. E.g "my_gallery_1/image_def_1=eastus,westus  my_gallery_2/image_def_2=uksouth,canadaeast,francesouth." Each key is the sig image definition ID or sig gallery name and sig image definition delimited by a "/". Each value is a comma-delimited list of replica locations.
    - subnet -- Name or ID of subnet to deploy the build virtual machine
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vm_size -- Size of the virtual machine used to build, customize and capture images. Omit or specify empty string to use the default (Standard_D1_v2)
    - vnet -- Name of VNET to deploy the build virtual machine. You should only specify it when subnet is a name
    '''
    return _call_az("az image builder create", locals())


def list(resource_group=None):
    '''
    List image builder templates.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az image builder list", locals())


def show(name, resource_group):
    '''
    Show an image builder template.

    Required Parameters:
    - name -- The name of the image template.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az image builder show", locals())


def delete(name, resource_group):
    '''
    Delete image builder template.

    Required Parameters:
    - name -- The name of the image template.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az image builder delete", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None):
    '''
    Update an image builder template.

    Required Parameters:
    - name -- The name of the image template.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az image builder update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the template is met.

    Required Parameters:
    - name -- The name of the image template.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az image builder wait", locals())


def run(name, resource_group, no_wait=None):
    '''
    Build an image builder template.

    Required Parameters:
    - name -- The name of the image template.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az image builder run", locals())


def show_runs(name, resource_group, output_name=None):
    '''
    Show an image builder template's run outputs.

    Required Parameters:
    - name -- The name of the image template.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - output_name -- Name of the image builder run output.
    '''
    return _call_az("az image builder show-runs", locals())


def cancel(name, resource_group):
    '''
    Cancel the long running image build based on the image template.

    Required Parameters:
    - name -- The name of the image template.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az image builder cancel", locals())

