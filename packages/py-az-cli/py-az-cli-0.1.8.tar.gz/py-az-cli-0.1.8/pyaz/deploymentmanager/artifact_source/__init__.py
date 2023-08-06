from ... pyaz_utils import _call_az

def create(artifact_source_name, location, resource_group, sas_uri, artifact_root=None, tags=None):
    '''
    Creates an artifact source.

    Required Parameters:
    - artifact_source_name -- The name of the artifact source
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sas_uri -- The SAS Uri to the Azure Storage container where the artifacts are stored.

    Optional Parameters:
    - artifact_root -- The root folder under which the artifacts are to be found. This is the path relative to the Azure storage container provided in --sas-uri.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az deploymentmanager artifact-source create", locals())


def delete(artifact_source_name, resource_group, yes=None):
    '''
    Deletes an artifact source.

    Required Parameters:
    - artifact_source_name -- The name of the artifact source
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az deploymentmanager artifact-source delete", locals())


def show(artifact_source_name, resource_group):
    '''
    Get the details of an artifact source.

    Required Parameters:
    - artifact_source_name -- The name of the artifact source
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az deploymentmanager artifact-source show", locals())


def list(resource_group):
    '''
    List all artifact sources in a resource group.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az deploymentmanager artifact-source list", locals())


def update(artifact_source_name, resource_group, add=None, artifact_root=None, force_string=None, remove=None, sas_uri=None, set=None, tags=None):
    '''
    Updates an artifact source.

    Required Parameters:
    - artifact_source_name -- The name of the artifact source
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - artifact_root -- The root folder under which the artifacts are to be found. This is the path relative to the Azure storage container provided in --sas-uri.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - sas_uri -- The SAS Uri to the Azure Storage container where the artifacts are stored.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az deploymentmanager artifact-source update", locals())

