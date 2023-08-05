from ... pyaz_utils import _call_az

def list(control_name, standard_name):
    '''
    Get details and state of assessments mapped to selected regulatory compliance control.

    Required Parameters:
    - control_name -- The compliance control name
    - standard_name -- The compliance standard name
    '''
    return _call_az("az security regulatory-compliance-assessments list", locals())


def show(control_name, name, standard_name):
    '''
    Shows supported regulatory compliance details and state for selected assessment.

    Required Parameters:
    - control_name -- The compliance control name
    - name -- name of the resource to be fetched
    - standard_name -- The compliance standard name
    '''
    return _call_az("az security regulatory-compliance-assessments show", locals())

