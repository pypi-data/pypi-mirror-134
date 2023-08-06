from ... pyaz_utils import _call_az

def list():
    '''
    Shows the workspace settings in your subscription - these settings let you control which workspace will hold your security data
    '''
    return _call_az("az security workspace-setting list", locals())


def show(name):
    '''
    Shows the workspace settings in your subscription - these settings let you control which workspace will hold your security data

    Required Parameters:
    - name -- name of the resource to be fetched
    '''
    return _call_az("az security workspace-setting show", locals())


def create(name, target_workspace):
    '''
    Creates a workspace settings in your subscription - these settings let you control which workspace will hold your security data

    Required Parameters:
    - name -- name of the resource to be fetched
    - target_workspace -- An ID of the workspace resource that will hold the security data
    '''
    return _call_az("az security workspace-setting create", locals())


def delete(name):
    '''
    Deletes the workspace settings in your subscription - this will make the security events on the subscription be reported to the default workspace

    Required Parameters:
    - name -- name of the resource to be fetched
    '''
    return _call_az("az security workspace-setting delete", locals())

