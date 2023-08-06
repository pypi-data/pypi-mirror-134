from .. pyaz_utils import _call_az

def list(resource_group=None):
    '''
    List all deployment scripts.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az deployment-scripts list", locals())


def show(name, resource_group):
    '''
    Retrieve a deployment script.

    Required Parameters:
    - name -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az deployment-scripts show", locals())


def show_log(name, resource_group):
    '''
    Show deployment script logs.

    Required Parameters:
    - name -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az deployment-scripts show-log", locals())


def delete(name, resource_group, yes=None):
    '''
    Delete a deployment script.

    Required Parameters:
    - name -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az deployment-scripts delete", locals())

