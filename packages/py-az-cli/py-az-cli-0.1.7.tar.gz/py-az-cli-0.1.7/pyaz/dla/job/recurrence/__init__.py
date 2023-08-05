'''
Manage Data Lake Analytics job recurrences.
'''
from .... pyaz_utils import _call_az

def show(account, recurrence_identity, end_date_time=None, start_date_time=None):
    '''
    Retrieve a job recurrence in a Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - recurrence_identity -- Recurrence ID.

    Optional Parameters:
    - end_date_time -- The end date for when to get recurrence and aggregate its data. The startDateTime and endDateTime can be no more than 30 days apart.
    - start_date_time -- The start date for when to get the recurrence and aggregate its data. The startDateTime and endDateTime can be no more than 30 days apart.
    '''
    return _call_az("az dla job recurrence show", locals())


def list(account, end_date_time=None, start_date_time=None):
    '''
    List job recurrences in a Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.

    Optional Parameters:
    - end_date_time -- The end date for when to get the list of recurrences. The startDateTime and endDateTime can be no more than 30 days apart.
    - start_date_time -- The start date for when to get the list of recurrences. The startDateTime and endDateTime can be no more than 30 days apart.
    '''
    return _call_az("az dla job recurrence list", locals())

