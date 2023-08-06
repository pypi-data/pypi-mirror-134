'''
View your security assessment results.
'''
from ... pyaz_utils import _call_az

def list():
    '''
    List all security assessment results.
    '''
    return _call_az("az security assessment list", locals())


def show(name, assessed_resource_id=None):
    '''
    Shows a security assessment.

    Required Parameters:
    - name -- name of the resource to be fetched

    Optional Parameters:
    - assessed_resource_id -- The target resource for this assessment
    '''
    return _call_az("az security assessment show", locals())


def create(name, status_code, additional_data=None, assessed_resource_id=None, status_cause=None, status_description=None):
    '''
    Creates a customer managed security assessment.

    Required Parameters:
    - name -- name of the resource to be fetched
    - status_code -- Progremmatic code for the result of the assessment. can be "Healthy", "Unhealthy" or "NotApplicable"

    Optional Parameters:
    - additional_data -- Data that is attached to the assessment result for better investigations or status clarity
    - assessed_resource_id -- The target resource for this assessment
    - status_cause -- Progremmatic code for the cause of the assessment result
    - status_description -- Human readable description of the cause of the assessment result
    '''
    return _call_az("az security assessment create", locals())


def delete(name, assessed_resource_id=None):
    '''
    Deletes a security assessment.

    Required Parameters:
    - name -- name of the resource to be fetched

    Optional Parameters:
    - assessed_resource_id -- The target resource for this assessment
    '''
    return _call_az("az security assessment delete", locals())

