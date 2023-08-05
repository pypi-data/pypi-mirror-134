'''
Manage Azure Container Registry Tasks that use Cloud Native Buildpacks.
'''
from ... pyaz_utils import _call_az

def build(builder, image, registry, agent_pool=None, auth_mode=None, no_format=None, no_logs=None, no_wait=None, pack_image_tag=None, platform=None, pull=None, resource_group=None, timeout=None):
    '''
    Queues a quick build task that builds an app and pushes it into an Azure Container Registry.

    Required Parameters:
    - builder -- The name and tag of a Buildpack builder image.
    - image -- The name and tag of the image using the format: '-t repo/image:tag'.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - agent_pool -- The name of the agent pool.
    - auth_mode -- Auth mode of the source registry.
    - no_format -- Indicates whether the logs should be displayed in raw format
    - no_logs -- Do not show logs after successfully queuing the build.
    - no_wait -- Do not wait for the run to complete and return immediately after queuing the run.
    - pack_image_tag -- The tag of the 'pack' runner image ('mcr.microsoft.com/oryx/pack').
    - platform -- The platform where build/task is run, Eg, 'windows' and 'linux'. When it's used in build commands, it also can be specified in 'os/arch/variant' format for the resulting image. Eg, linux/arm/v7. The 'arch' and 'variant' parts are optional.
    - pull -- Pull the latest builder and run images before use.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - timeout -- The timeout in seconds.
    '''
    return _call_az("az acr pack build", locals())

