'''
Manage order with databoxedge
'''
from ... pyaz_utils import _call_az

def list(device_name, resource_group):
    '''
    List all the orders related to a Data Box Edge/Data Box Gateway device.

    Required Parameters:
    - device_name -- The device name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az databoxedge order list", locals())


def show(device_name, resource_group):
    '''
    Get a specific order by name.

    Required Parameters:
    - device_name -- The device name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az databoxedge order show", locals())


def create(address_line1, city, company_name, contact_person, country, device_name, email_list, phone, postal_code, resource_group, state, status, address_line2=None, address_line3=None, comments=None, no_wait=None):
    '''
    Create an order.

    Required Parameters:
    - address_line1 -- The address line1.
    - city -- The city name.
    - company_name -- The name of the company.
    - contact_person -- The contact person name.
    - country -- The country name.
    - device_name -- The order details of a device.
    - email_list -- The email list.
    - phone -- The phone number.
    - postal_code -- The postal code.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - state -- The state name.
    - status -- Status of the order as per the allowed status types.

    Optional Parameters:
    - address_line2 -- The address line2.
    - address_line3 -- The address line3.
    - comments -- Comments related to this status change.
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az databoxedge order create", locals())


def update(device_name, resource_group, add=None, address_line1=None, address_line2=None, address_line3=None, city=None, comments=None, company_name=None, contact_person=None, country=None, email_list=None, force_string=None, no_wait=None, phone=None, postal_code=None, remove=None, set=None, state=None, status=None):
    '''
    Update an order.

    Required Parameters:
    - device_name -- The order details of a device.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - address_line1 -- The address line1.
    - address_line2 -- The address line2.
    - address_line3 -- The address line3.
    - city -- The city name.
    - comments -- Comments related to this status change.
    - company_name -- The name of the company.
    - contact_person -- The contact person name.
    - country -- The country name.
    - email_list -- The email list.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - no_wait -- Do not wait for the long-running operation to finish.
    - phone -- The phone number.
    - postal_code -- The postal code.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - state -- The state name.
    - status -- Status of the order as per the allowed status types.
    '''
    return _call_az("az databoxedge order update", locals())


def delete(device_name, resource_group, no_wait=None, yes=None):
    '''
    Delete the order related to the device.

    Required Parameters:
    - device_name -- The device name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az databoxedge order delete", locals())


def wait(device_name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the databoxedge order is met.

    Required Parameters:
    - device_name -- The device name.
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
    return _call_az("az databoxedge order wait", locals())

