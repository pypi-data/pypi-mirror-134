from ... pyaz_utils import _call_az

def list():
    '''
    List all security assessment results.
    '''
    return _call_az("az security assessment-metadata list", locals())


def show(name):
    '''
    Shows a security assessment.

    Required Parameters:
    - name -- name of the resource to be fetched
    '''
    return _call_az("az security assessment-metadata show", locals())


def create(description, display_name, name, severity, remediation_description=None):
    '''
    Creates a customer managed security assessment type.

    Required Parameters:
    - description -- Detailed string that will help users to understand the assessment and how it is calculated
    - display_name -- Human readable title for this object
    - name -- name of the resource to be fetched
    - severity -- Indicates the importance of the security risk if the assessment is unhealthy

    Optional Parameters:
    - remediation_description -- Detailed string that will help users to understand the different ways to mitigate or fix the security issue
    '''
    return _call_az("az security assessment-metadata create", locals())


def delete(name):
    '''
    Deletes a security assessment type and all it's assessment results.

    Required Parameters:
    - name -- name of the resource to be fetched
    '''
    return _call_az("az security assessment-metadata delete", locals())

