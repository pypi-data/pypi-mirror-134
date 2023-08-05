'''
Manage event domain topics.
'''
from .... pyaz_utils import _call_az

def show(domain_name, name, resource_group):
    '''
    Get the details of a domain topic.

    Required Parameters:
    - domain_name -- Name of the domain.
    - name -- Name of the domain topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid domain topic show", locals())


def list(domain_name, resource_group, odata_query=None):
    '''
    List available topics in a domain.

    Required Parameters:
    - domain_name -- Name of the domain.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - odata_query -- The OData query used for filtering the list results. Filtering is currently allowed on the Name property only. The supported operations include: CONTAINS, eq (for equal), ne (for not equal), AND, OR and NOT.
    '''
    return _call_az("az eventgrid domain topic list", locals())


def delete(domain_name, name, resource_group):
    '''
    Delete a domain topic under a domain.

    Required Parameters:
    - domain_name -- Name of the domain.
    - name -- Name of the domain topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid domain topic delete", locals())


def create(domain_name, name, resource_group):
    '''
    Create a domain topic under a domain.

    Required Parameters:
    - domain_name -- Name of the domain.
    - name -- Name of the domain topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid domain topic create", locals())

