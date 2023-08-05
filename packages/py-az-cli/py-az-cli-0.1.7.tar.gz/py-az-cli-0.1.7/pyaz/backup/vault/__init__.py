'''
Online storage entity in Azure used to hold data such as backup copies, recovery points and backup policies.
'''
from ... pyaz_utils import _call_az
from . import backup_properties, encryption, identity


def create(location, name, resource_group, tags=None):
    '''
    Create a new Recovery Services vault.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- Name of the Recovery services vault.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az backup vault create", locals())


def show(name, resource_group):
    '''
    Show details of a particular Recovery service vault.

    Required Parameters:
    - name -- Name of the Recovery services vault.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az backup vault show", locals())


def list(resource_group=None):
    '''
    List Recovery service vaults within a subscription.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az backup vault list", locals())


def delete(name, resource_group, force=None, yes=None):
    '''
    Delete an existing Recovery services vault.

    Required Parameters:
    - name -- Name of the Recovery services vault.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - force -- Force completion of the requested action.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az backup vault delete", locals())

