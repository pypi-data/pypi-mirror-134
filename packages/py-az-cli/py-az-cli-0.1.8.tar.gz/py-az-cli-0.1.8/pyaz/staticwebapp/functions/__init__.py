'''
Link or unlink a prexisting functionapp with a static webapp. Also known as "Bring your own Functions."
'''
from ... pyaz_utils import _call_az

def link(function_resource_id, name, resource_group, force=None):
    '''
    Link an Azure Function to a static webapp. Also known as "Bring your own Functions." Only one Azure Functions app is available to a single static web app. Static webapp SKU must be "Standard"

    Required Parameters:
    - function_resource_id -- Resource ID of the functionapp to link. Can be retrieved with 'az functionapp --query id'
    - name -- Name of the static site
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - force -- Force the function link even if the function is already linked to a static webapp. May be needed if the function was previously linked to a static webapp.
    '''
    return _call_az("az staticwebapp functions link", locals())


def unlink(name, resource_group):
    '''
    Unlink an Azure Function from a static webapp

    Required Parameters:
    - name -- Name of the static site
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp functions unlink", locals())


def show(name, resource_group):
    '''
    Show details on the Azure Function linked to a static webapp

    Required Parameters:
    - name -- Name of the static site
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp functions show", locals())

