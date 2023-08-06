from ... pyaz_utils import _call_az
from . import version


def list(gallery_name, resource_group):
    '''
    

    Required Parameters:
    - gallery_name -- gallery name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sig gallery-application list", locals())


def show(gallery_name, name, resource_group):
    '''
    

    Required Parameters:
    - gallery_name -- gallery name
    - name -- The name of the gallery Application
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sig gallery-application show", locals())


def create(gallery_name, name, os_type, resource_group, description=None, location=None, no_wait=None, tags=None):
    '''
    Create a gallery Application Definition.

    Required Parameters:
    - gallery_name -- gallery name
    - name -- The name of the gallery Application
    - os_type -- This property allows you to specify the supported type of the OS that application is built for. <br><br> Possible values are: <br><br> **Windows** <br><br> **Linux**
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - description -- The description of this gallery Application Definition resource. This property is updatable.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az sig gallery-application create", locals())


def update(gallery_name, name, resource_group, description=None, location=None, no_wait=None, tags=None):
    '''
    Update a gallery Application Definition.

    Required Parameters:
    - gallery_name -- gallery name
    - name -- The name of the gallery Application
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - description -- The description of this gallery Application Definition resource. This property is updatable.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az sig gallery-application update", locals())


def delete(gallery_name, name, resource_group, no_wait=None, yes=None):
    '''
    

    Required Parameters:
    - gallery_name -- gallery name
    - name -- The name of the gallery Application
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az sig gallery-application delete", locals())


def wait(gallery_name, name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the sig gallery-application is met.

    Required Parameters:
    - gallery_name -- gallery name
    - name -- The name of the gallery Application
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
    return _call_az("az sig gallery-application wait", locals())

