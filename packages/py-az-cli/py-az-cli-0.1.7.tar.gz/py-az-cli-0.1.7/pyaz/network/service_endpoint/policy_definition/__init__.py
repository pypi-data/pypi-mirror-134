from .... pyaz_utils import _call_az

def create(name, policy_name, resource_group, service, service_resources, description=None):
    '''
    Create a service endpoint policy definition.

    Required Parameters:
    - name -- Name of the service endpoint policy definition
    - policy_name -- Name of the service endpoint policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service -- Service name the policy definition applies to.
    - service_resources -- Space-separated list of service resources the definition applies to.

    Optional Parameters:
    - description -- Description of the policy definition.
    '''
    return _call_az("az network service-endpoint policy-definition create", locals())


def delete(name, policy_name, resource_group):
    '''
    Delete a service endpoint policy definition.

    Required Parameters:
    - name -- Name of the service endpoint policy definition
    - policy_name -- Name of the service endpoint policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network service-endpoint policy-definition delete", locals())


def list(policy_name, resource_group):
    '''
    List service endpoint policy definitions.

    Required Parameters:
    - policy_name -- Name of the service endpoint policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network service-endpoint policy-definition list", locals())


def show(name, policy_name, resource_group):
    '''
    Get the details of a service endpoint policy definition.

    Required Parameters:
    - name -- Name of the service endpoint policy definition
    - policy_name -- Name of the service endpoint policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network service-endpoint policy-definition show", locals())


def update(name, policy_name, resource_group, add=None, description=None, force_string=None, remove=None, service=None, service_resources=None, set=None):
    '''
    Update a service endpoint policy definition.

    Required Parameters:
    - name -- Name of the service endpoint policy definition
    - policy_name -- Name of the service endpoint policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - description -- Description of the policy definition.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - service -- Service name the policy definition applies to.
    - service_resources -- Space-separated list of service resources the definition applies to.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network service-endpoint policy-definition update", locals())

