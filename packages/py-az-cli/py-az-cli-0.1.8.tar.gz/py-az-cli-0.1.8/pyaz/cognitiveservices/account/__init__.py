'''
Manage Azure Cognitive Services accounts.
'''
from ... pyaz_utils import _call_az
from . import commitment_plan, deployment, identity, keys, network_rule


def create(kind, location, name, resource_group, sku, api_properties=None, assign_identity=None, custom_domain=None, encryption=None, storage=None, tags=None, yes=None):
    '''
    Manage Azure Cognitive Services accounts.

    Required Parameters:
    - kind -- the API name of cognitive services account
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku -- Name of the Sku of cognitive services account

    Optional Parameters:
    - api_properties -- Api properties in JSON format or a=b c=d format. Some cognitive services (i.e. QnA Maker) require extra api properties to create the account.
    - assign_identity -- Generate and assign an Azure Active Directory Identity for this account.
    - custom_domain -- User domain assigned to the account. Name is the CNAME source.
    - encryption -- The encryption properties for this resource, in JSON format.
    - storage -- The storage accounts for this resource, in JSON array format.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - yes -- Do not prompt for terms confirmation
    '''
    return _call_az("az cognitiveservices account create", locals())


def delete(name, resource_group):
    '''
    Manage Azure Cognitive Services accounts.

    Required Parameters:
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account delete", locals())


def show(name, resource_group):
    '''
    Manage Azure Cognitive Services accounts.

    Required Parameters:
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account show", locals())


def update(name, resource_group, api_properties=None, custom_domain=None, encryption=None, sku=None, storage=None, tags=None):
    '''
    Manage Azure Cognitive Services accounts.

    Required Parameters:
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - api_properties -- Api properties in JSON format or a=b c=d format. Some cognitive services (i.e. QnA Maker) require extra api properties to create the account.
    - custom_domain -- User domain assigned to the account. Name is the CNAME source.
    - encryption -- The encryption properties for this resource, in JSON format.
    - sku -- Name of the Sku of cognitive services account
    - storage -- The storage accounts for this resource, in JSON array format.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az cognitiveservices account update", locals())


def list(resource_group=None):
    '''
    Manage Azure Cognitive Services accounts.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account list", locals())


def show_deleted(location, name, resource_group):
    '''
    Show a soft-deleted Azure Cognitive Services account.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account show-deleted", locals())


def list_deleted():
    '''
    List soft-deleted Azure Cognitive Services accounts.
    '''
    return _call_az("az cognitiveservices account list-deleted", locals())


def purge(location, name, resource_group):
    '''
    Purge a soft-deleted Azure Cognitive Services account.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account purge", locals())


def recover(location, name, resource_group):
    '''
    Recover a soft-deleted Azure Cognitive Services account.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account recover", locals())


def list_skus(kind=None, location=None, name=None, resource_group=None):
    '''
    Manage Azure Cognitive Services accounts.

    Optional Parameters:
    - kind -- the API name of cognitive services account
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account list-skus", locals())


def list_usage(name, resource_group):
    '''
    

    Required Parameters:
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account list-usage", locals())


def list_kinds():
    return _call_az("az cognitiveservices account list-kinds", locals())

