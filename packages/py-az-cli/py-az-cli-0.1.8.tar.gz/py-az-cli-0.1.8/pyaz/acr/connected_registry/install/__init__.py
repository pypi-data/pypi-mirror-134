from .... pyaz_utils import _call_az

def info(name, parent_protocol, registry, resource_group=None):
    '''
    Retrieve information required to activate a connected registry.

    Required Parameters:
    - name -- Name for the connected registry. Name must be between 5 to 40 character long, start with a letter and contain only alphanumeric characters (including ‘_’ or ‘-’). Name must be unique under the Cloud ACR hierarchy.
    - parent_protocol -- Specify the protocol used to communicate with its parent.
    - registry -- The login server of the Cloud ACR registry. Must be the FQDN to support also Azure Stack.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr connected-registry install info", locals())


def renew_credentials(name, parent_protocol, registry, resource_group=None, yes=None):
    '''
    Retrieve information required to activate a connected registry, and renews the sync token credentials.

    Required Parameters:
    - name -- Name for the connected registry. Name must be between 5 to 40 character long, start with a letter and contain only alphanumeric characters (including ‘_’ or ‘-’). Name must be unique under the Cloud ACR hierarchy.
    - parent_protocol -- Specify the protocol used to communicate with its parent.
    - registry -- The login server of the Cloud ACR registry. Must be the FQDN to support also Azure Stack.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az acr connected-registry install renew-credentials", locals())

