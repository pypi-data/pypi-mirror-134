'''
Manage Data Lake Analytics job pipelines.
'''
from .... pyaz_utils import _call_az

def show(account, pipeline_identity, end_date_time=None, start_date_time=None):
    '''
    Retrieve a job pipeline in a Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - pipeline_identity -- Pipeline ID.

    Optional Parameters:
    - end_date_time -- The end date for when to get the pipeline and aggregate its data. The startDateTime and endDateTime can be no more than 30 days apart.
    - start_date_time -- The start date for when to get the pipeline and aggregate its data. The startDateTime and endDateTime can be no more than 30 days apart.
    '''
    return _call_az("az dla job pipeline show", locals())


def list(account, end_date_time=None, start_date_time=None):
    '''
    List job pipelines in a Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.

    Optional Parameters:
    - end_date_time -- The end date for when to get the list of pipelines. The startDateTime and endDateTime can be no more than 30 days apart.
    - start_date_time -- The start date for when to get the list of pipelines. The startDateTime and endDateTime can be no more than 30 days apart.
    '''
    return _call_az("az dla job pipeline list", locals())

