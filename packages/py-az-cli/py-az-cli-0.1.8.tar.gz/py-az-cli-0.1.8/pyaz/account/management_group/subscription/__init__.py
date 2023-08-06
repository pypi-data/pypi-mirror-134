from .... pyaz_utils import _call_az

def add(name, subscription):
    '''
    Add a subscription to a management group.

    Required Parameters:
    - name -- None
    - subscription -- Name or ID of subscription.
    '''
    return _call_az("az account management-group subscription add", locals())


def remove(name, subscription):
    '''
    Remove an existing subscription from a management group.

    Required Parameters:
    - name -- None
    - subscription -- Name or ID of subscription.
    '''
    return _call_az("az account management-group subscription remove", locals())

