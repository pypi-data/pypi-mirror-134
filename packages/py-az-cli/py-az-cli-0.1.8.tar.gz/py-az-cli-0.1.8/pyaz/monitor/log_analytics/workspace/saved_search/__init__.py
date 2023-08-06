from ..... pyaz_utils import _call_az

def create(category, display_name, name, resource_group, saved_query, workspace_name, func_alias=None, func_param=None, tags=None):
    '''
    Create a saved search for a given workspace.

    Required Parameters:
    - category -- The category of the saved search. This helps the user to find a saved search faster.
    - display_name -- Display name of the saved search.
    - name -- Name of the saved search and it's unique in a given workspace.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - saved_query -- The query expression for the saved search.
    - workspace_name -- Name of the Log Analytics Workspace.

    Optional Parameters:
    - func_alias -- Function Aliases are short names given to Saved Searches so they can be easily referenced in query. They are required for Computer Groups.
    - func_param -- The optional function parameters if query serves as a function. Value should be in the following format: 'param-name1:type1 = default_value1, param-name2:type2 = default_value2'. For more examples and proper syntax please refer to https://docs.microsoft.com/azure/kusto/query/functions/user-defined-functions.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az monitor log-analytics workspace saved-search create", locals())


def update(name, resource_group, workspace_name, add=None, category=None, display_name=None, force_string=None, func_alias=None, func_param=None, remove=None, saved_query=None, set=None, tags=None):
    '''
    Update a saved search for a given workspace.

    Required Parameters:
    - name -- Name of the saved search and it's unique in a given workspace.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - category -- The category of the saved search. This helps the user to find a saved search faster.
    - display_name -- Display name of the saved search.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - func_alias -- Function Aliases are short names given to Saved Searches so they can be easily referenced in query. They are required for Computer Groups.
    - func_param -- The optional function parameters if query serves as a function. Value should be in the following format: 'param-name1:type1 = default_value1, param-name2:type2 = default_value2'. For more examples and proper syntax please refer to https://docs.microsoft.com/azure/kusto/query/functions/user-defined-functions.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - saved_query -- The query expression for the saved search.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az monitor log-analytics workspace saved-search update", locals())


def delete(name, resource_group, workspace_name, yes=None):
    '''
    Delete a saved search for a given workspace.

    Required Parameters:
    - name -- Name of the saved search and it's unique in a given workspace.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az monitor log-analytics workspace saved-search delete", locals())


def show(name, resource_group, workspace_name):
    '''
    Show a saved search for a given workspace.

    Required Parameters:
    - name -- Name of the saved search and it's unique in a given workspace.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace saved-search show", locals())


def list(resource_group, workspace_name):
    '''
    List all saved searches for a given workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace saved-search list", locals())

