from ... pyaz_utils import _call_az

def list(device_name, resource_group):
    '''
    Get all the bandwidth schedules for a Data Box Edge/Data Box Gateway device.

    Required Parameters:
    - device_name -- The device name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az databoxedge bandwidth-schedule list", locals())


def show(device_name, name, resource_group):
    '''
    Get the properties of the specified bandwidth schedule.

    Required Parameters:
    - device_name -- The device name.
    - name -- The bandwidth schedule name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az databoxedge bandwidth-schedule show", locals())


def create(days, device_name, name, rate_in_mbps, resource_group, start, stop, no_wait=None):
    '''
    Create a bandwidth schedule.

    Required Parameters:
    - days -- The days of the week when this schedule is applicable.
    - device_name -- The device name.
    - name -- The bandwidth schedule name which needs to be added/updated.
    - rate_in_mbps -- The bandwidth rate in Mbps.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - start -- The start time of the schedule in UTC.
    - stop -- The stop time of the schedule in UTC.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az databoxedge bandwidth-schedule create", locals())


def update(days, device_name, name, rate_in_mbps, resource_group, start, stop, add=None, force_string=None, no_wait=None, remove=None, set=None):
    '''
    Update a bandwidth schedule.

    Required Parameters:
    - days -- The days of the week when this schedule is applicable.
    - device_name -- The device name.
    - name -- The bandwidth schedule name which needs to be added/updated.
    - rate_in_mbps -- The bandwidth rate in Mbps.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - start -- The start time of the schedule in UTC.
    - stop -- The stop time of the schedule in UTC.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az databoxedge bandwidth-schedule update", locals())


def delete(device_name, name, resource_group, no_wait=None, yes=None):
    '''
    Delete the specified bandwidth schedule.

    Required Parameters:
    - device_name -- The device name.
    - name -- The bandwidth schedule name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az databoxedge bandwidth-schedule delete", locals())


def wait(device_name, name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the databoxedge bandwidth-schedule is met.

    Required Parameters:
    - device_name -- The device name.
    - name -- The bandwidth schedule name.
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
    return _call_az("az databoxedge bandwidth-schedule wait", locals())

