'''
Tag Management on a resource.
'''
from .. pyaz_utils import _call_az

def list(resource_id=None):
    '''
    List the entire set of tags on a specific resource.

    Optional Parameters:
    - resource_id -- The resource identifier for the tagged entity. A resource, a resource group or a subscription may be tagged.
    '''
    return _call_az("az tag list", locals())


def create(name=None, resource_id=None, tags=None):
    '''
    Create tags on a specific resource.

    Optional Parameters:
    - name -- The tag name.
    - resource_id -- The resource identifier for the tagged entity. A resource, a resource group or a subscription may be tagged.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az tag create", locals())


def delete(name=None, resource_id=None, yes=None):
    '''
    Delete tags on a specific resource.

    Optional Parameters:
    - name -- The tag name.
    - resource_id -- The resource identifier for the tagged entity. A resource, a resource group or a subscription may be tagged.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az tag delete", locals())


def update(operation, resource_id, tags):
    '''
    Selectively update the set of tags on a specific resource.

    Required Parameters:
    - operation -- The update operation: options include Merge, Replace and Delete.
    - resource_id -- The resource identifier for the tagged entity. A resource, a resource group or a subscription may be tagged.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az tag update", locals())


def add_value(name, value):
    '''
    Create a tag value.

    Required Parameters:
    - name -- The tag name.
    - value -- The tag value.
    '''
    return _call_az("az tag add-value", locals())


def remove_value(name, value):
    '''
    

    Required Parameters:
    - name -- The tag name.
    - value -- The tag value.
    '''
    return _call_az("az tag remove-value", locals())

