'''
Manage Data Lake Analytics catalog assemblies.
'''
from .... pyaz_utils import _call_az

def show(account, assembly_name, database_name):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - assembly_name -- The name of the assembly.
    - database_name -- The name of the database containing the assembly.
    '''
    return _call_az("az dla catalog assembly show", locals())


def list(account, database_name, count=None, filter=None, orderby=None, select=None, skip=None, top=None):
    '''
    

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - database_name -- The name of the database containing the assembly.

    Optional Parameters:
    - count -- The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true.
    - filter -- OData filter. Optional.
    - orderby -- OrderBy clause. One or more comma-separated expressions with an optional "asc" (the default) or "desc" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
    - select -- OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
    - skip -- The number of items to skip over before returning elements.
    - top -- Maximum number of items to return.
    '''
    return _call_az("az dla catalog assembly list", locals())

