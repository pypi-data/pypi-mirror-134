from ... pyaz_utils import _call_az

def show():
    return _call_az("az ad signed-in-user show", locals())


def list_owned_objects(type=None):
    '''
    Get the list of directory objects that are owned by the user

    Optional Parameters:
    - type -- object type filter, e.g. "application", "servicePrincipal"  "group", etc
    '''
    return _call_az("az ad signed-in-user list-owned-objects", locals())

