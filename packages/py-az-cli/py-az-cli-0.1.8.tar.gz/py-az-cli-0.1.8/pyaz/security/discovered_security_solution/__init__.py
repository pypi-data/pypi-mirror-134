from ... pyaz_utils import _call_az

def list():
    '''
    List the discovered security solutions.
    '''
    return _call_az("az security discovered-security-solution list", locals())


def show(name, resource_group):
    '''
    Shows a discovered security solution.

    Required Parameters:
    - name -- name of the resource to be fetched
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az security discovered-security-solution show", locals())

