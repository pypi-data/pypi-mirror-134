'''
Manage links between resources.
'''
from ... pyaz_utils import _call_az

def create(link, target, notes=None):
    '''
    Create a new link between resources.

    Required Parameters:
    - link -- Fully-qualified resource ID of the resource link.
    - target -- Fully-qualified resource ID of the resource link target.

    Optional Parameters:
    - notes -- Notes for the link.
    '''
    return _call_az("az resource link create", locals())


def delete(link):
    '''
    Delete a link between resources.

    Required Parameters:
    - link -- Fully-qualified resource ID of the resource link.
    '''
    return _call_az("az resource link delete", locals())


def show(link):
    '''
    

    Required Parameters:
    - link -- Fully-qualified resource ID of the resource link.
    '''
    return _call_az("az resource link show", locals())


def list(filter=None, scope=None):
    '''
    List resource links.

    Optional Parameters:
    - filter -- Filter string for limiting results.
    - scope -- Fully-qualified scope for retrieving links.
    '''
    return _call_az("az resource link list", locals())


def update(link, notes=None, target=None):
    '''
    Update link between resources.

    Required Parameters:
    - link -- Fully-qualified resource ID of the resource link.

    Optional Parameters:
    - notes -- Notes for the link.
    - target -- Fully-qualified resource ID of the resource link target.
    '''
    return _call_az("az resource link update", locals())

