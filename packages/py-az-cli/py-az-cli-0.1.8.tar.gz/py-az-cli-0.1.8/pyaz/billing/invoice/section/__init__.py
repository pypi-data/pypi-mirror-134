'''
billing invoice section
'''
from .... pyaz_utils import _call_az

def list(account_name, profile_name):
    '''
    List the invoice sections that a user has access to. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - profile_name -- The ID that uniquely identifies a billing profile.
    '''
    return _call_az("az billing invoice section list", locals())


def show(account_name, name, profile_name):
    '''
    Get an invoice section by its ID. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- The ID that uniquely identifies an invoice section.
    - profile_name -- The ID that uniquely identifies a billing profile.
    '''
    return _call_az("az billing invoice section show", locals())


def create(account_name, name, profile_name, display_name=None, labels=None, no_wait=None):
    '''
    Creates or updates an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- The ID that uniquely identifies an invoice section.
    - profile_name -- The ID that uniquely identifies a billing profile.

    Optional Parameters:
    - display_name -- The name of the invoice section.
    - labels -- Dictionary of metadata associated with the invoice section. Expect value: KEY1=VALUE1 KEY2=VALUE2 ...
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az billing invoice section create", locals())


def update(account_name, name, profile_name, display_name=None, labels=None, no_wait=None):
    '''
    Creates or updates an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- The ID that uniquely identifies an invoice section.
    - profile_name -- The ID that uniquely identifies a billing profile.

    Optional Parameters:
    - display_name -- The name of the invoice section.
    - labels -- Dictionary of metadata associated with the invoice section. Expect value: KEY1=VALUE1 KEY2=VALUE2 ...
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az billing invoice section update", locals())


def wait(account_name, name, profile_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the billing invoice section is met.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- The ID that uniquely identifies an invoice section.
    - profile_name -- The ID that uniquely identifies a billing profile.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az billing invoice section wait", locals())

