'''
Manage identities of an Azure IoT hub.
'''
from .... pyaz_utils import _call_az

def assign(name, resource_group=None, role=None, scopes=None, system_assigned=None, user_assigned=None):
    '''
    Assign managed identities to an IoT Hub

    Required Parameters:
    - name -- IoT Hub name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - role -- Role to assign to the hub's system-assigned managed identity.
    - scopes -- Space separated list of scopes to assign the role (--role) for the system-assigned managed identity.
    - system_assigned -- Assign a system-assigned managed identity to this hub.
    - user_assigned -- Assign user-assigned managed identities to this hub. Accept space-separated list of identity resource IDs.
    '''
    return _call_az("az iot hub identity assign", locals())


def show(name, resource_group=None):
    '''
    Show the identity properties of an IoT Hub

    Required Parameters:
    - name -- IoT Hub name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub identity show", locals())


def remove(name, resource_group=None, system_assigned=None, user_assigned=None):
    '''
    Remove managed identities from an IoT Hub

    Required Parameters:
    - name -- IoT Hub name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - system_assigned -- Remove a system-assigned managed identity from this hub.
    - user_assigned -- Remove user-assigned managed identities from this hub. Accept space-separated list of identity resource IDs.
    '''
    return _call_az("az iot hub identity remove", locals())

