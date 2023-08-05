from ... pyaz_utils import _call_az

def set_key(hybrid_connection, key_type, namespace, plan, resource_group):
    '''
    set the key that all apps in an appservice plan use to connect to the hybrid-connections in that appservice plan

    Required Parameters:
    - hybrid_connection -- Hybrid connection name
    - key_type -- Which key (primary or secondary) should be used
    - namespace -- Hybrid connection namespace
    - plan -- AppService plan
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az appservice hybrid-connection set-key", locals())

