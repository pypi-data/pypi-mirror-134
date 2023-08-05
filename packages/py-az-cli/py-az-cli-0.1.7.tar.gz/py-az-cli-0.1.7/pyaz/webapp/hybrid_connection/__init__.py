from ... pyaz_utils import _call_az

def list(name, resource_group, slot=None):
    '''
    list the hybrid-connections on a webapp

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp hybrid-connection list", locals())


def add(hybrid_connection, name, namespace, resource_group, slot=None):
    '''
    add an existing hybrid-connection to a webapp

    Required Parameters:
    - hybrid_connection -- Hybrid connection name
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - namespace -- Hybrid connection namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp hybrid-connection add", locals())


def remove(hybrid_connection, name, namespace, resource_group, slot=None):
    '''
    remove a hybrid-connection from a webapp

    Required Parameters:
    - hybrid_connection -- Hybrid connection name
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - namespace -- Hybrid connection namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp hybrid-connection remove", locals())

