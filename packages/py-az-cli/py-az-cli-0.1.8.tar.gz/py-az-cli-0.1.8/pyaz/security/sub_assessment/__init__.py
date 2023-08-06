from ... pyaz_utils import _call_az

def list(assessed_resource_id=None, assessment_name=None):
    '''
    List all security sub assessment results.

    Optional Parameters:
    - assessed_resource_id -- The target resource for this assessment
    - assessment_name -- Name of the assessment resource
    '''
    return _call_az("az security sub-assessment list", locals())


def show(assessment_name, name, assessed_resource_id=None):
    '''
    Shows a security sub assessment.

    Required Parameters:
    - assessment_name -- Name of the assessment resource
    - name -- name of the resource to be fetched

    Optional Parameters:
    - assessed_resource_id -- The target resource for this assessment
    '''
    return _call_az("az security sub-assessment show", locals())

