from ... pyaz_utils import _call_az

def create(name, parameters, resource_group):
    '''
    

    Required Parameters:
    - name -- The autoscale setting name.
    - parameters -- JSON encoded parameters configuration. Use @{file} to load from a file. Use az autoscale-settings get-parameters-template to export json template.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor autoscale-settings create", locals())


def delete(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The autoscale setting name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor autoscale-settings delete", locals())


def show(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The autoscale setting name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor autoscale-settings show", locals())


def list(resource_group):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor autoscale-settings list", locals())


def get_parameters_template():
    return _call_az("az monitor autoscale-settings get-parameters-template", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None):
    '''
    Updates an autoscale setting.

    Required Parameters:
    - name -- The autoscale setting name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az monitor autoscale-settings update", locals())

