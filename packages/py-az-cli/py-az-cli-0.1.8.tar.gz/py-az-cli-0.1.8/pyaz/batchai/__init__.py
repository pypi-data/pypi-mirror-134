'''
Manage Batch AI resources.
'''
from .. pyaz_utils import _call_az
from . import cluster, experiment, file_server, job, workspace


def list_usages(location):
    '''
    Gets the current usage information as well as limits for Batch AI resources for given location.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az batchai list-usages", locals())

