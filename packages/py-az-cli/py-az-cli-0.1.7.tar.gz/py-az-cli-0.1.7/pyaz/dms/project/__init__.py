'''
Manage projects for an instance of the Data Migration Service.
'''
from ... pyaz_utils import _call_az
from . import task


def create(location, name, resource_group, service_name, source_platform, target_platform, tags=None):
    '''
    Create a migration project which can contain multiple tasks.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the Project.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the Service.
    - source_platform -- None
    - target_platform -- None

    Optional Parameters:
    - tags -- A space-delimited list of tags in "tag1[=value1]" format.
    '''
    return _call_az("az dms project create", locals())


def delete(name, resource_group, service_name, delete_running_tasks=None, yes=None):
    '''
    Delete a project.

    Required Parameters:
    - name -- The name of the Project.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the Service.

    Optional Parameters:
    - delete_running_tasks -- Delete the resource even if it contains running tasks.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az dms project delete", locals())


def list(resource_group, service_name):
    '''
    List the projects within an instance of DMS.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the Service.
    '''
    return _call_az("az dms project list", locals())


def show(name, resource_group, service_name):
    '''
    Show the details of a migration project.

    Required Parameters:
    - name -- The name of the Project.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the Service.
    '''
    return _call_az("az dms project show", locals())


def check_name(name, resource_group, service_name):
    '''
    Check if a given project name is available within a given instance of DMS as well as the name's validity.

    Required Parameters:
    - name -- The name of the Project.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the Service.
    '''
    return _call_az("az dms project check-name", locals())

