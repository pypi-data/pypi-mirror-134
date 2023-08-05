'''
Commands to manage webapp connections
'''
from ... pyaz_utils import _call_az
from . import create, update


def list(name=None, resource_group=None, source_id=None):
    '''
    List connections of a webapp.

    Optional Parameters:
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    '''
    return _call_az("az webapp connection list", locals())


def show(connection=None, id=None, name=None, resource_group=None):
    '''
    Get the details of a webapp connection.

    Optional Parameters:
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    '''
    return _call_az("az webapp connection show", locals())


def delete(connection=None, id=None, name=None, no_wait=None, resource_group=None, yes=None):
    '''
    Delete a webapp connection.

    Optional Parameters:
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az webapp connection delete", locals())


def list_configuration(connection=None, id=None, name=None, resource_group=None):
    '''
    List source configurations of a webapp connection.

    Optional Parameters:
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    '''
    return _call_az("az webapp connection list-configuration", locals())


def validate(connection=None, id=None, name=None, resource_group=None):
    '''
    Validate a webapp connection.

    Optional Parameters:
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    '''
    return _call_az("az webapp connection validate", locals())


def list_support_types(target_type=None):
    '''
    List client types and auth types supported by webapp connections.

    Optional Parameters:
    - target_type -- The target resource type
    '''
    return _call_az("az webapp connection list-support-types", locals())


def wait(connection=None, created=None, custom=None, deleted=None, exists=None, id=None, interval=None, name=None, resource_group=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the connection is met.

    Optional Parameters:
    - connection -- Name of the webapp connection.
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - interval -- polling interval in seconds
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az webapp connection wait", locals())

