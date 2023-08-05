'''
View your security contacts.
'''
from ... pyaz_utils import _call_az

def list():
    '''
    List security contact.
    '''
    return _call_az("az security contact list", locals())


def show(name):
    '''
    Shows a security contact.

    Required Parameters:
    - name -- name of the resource to be fetched
    '''
    return _call_az("az security contact show", locals())


def create(email, name, alert_notifications=None, alerts_admins=None, phone=None):
    '''
    Creates a security contact.

    Required Parameters:
    - email -- E-mail of the security contact
    - name -- name of the resource to be fetched

    Optional Parameters:
    - alert_notifications -- Whether to send mail notifications to the security contacts
    - alerts_admins -- Whether to send mail notifications to the subscription administrators
    - phone -- Phone of the security contact
    '''
    return _call_az("az security contact create", locals())


def delete(name):
    '''
    Deletes a security contact.

    Required Parameters:
    - name -- name of the resource to be fetched
    '''
    return _call_az("az security contact delete", locals())

