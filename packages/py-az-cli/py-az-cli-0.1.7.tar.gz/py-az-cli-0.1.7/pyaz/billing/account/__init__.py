'''
billing account
'''
from ... pyaz_utils import _call_az

def list(expand=None):
    '''
    List the billing accounts that a user has access to.

    Optional Parameters:
    - expand -- May be used to expand the soldTo, invoice sections and billing profiles.
    '''
    return _call_az("az billing account list", locals())


def show(name, expand=None):
    '''
    Get a billing account by its ID.

    Required Parameters:
    - name -- The ID that uniquely identifies a billing account.

    Optional Parameters:
    - expand -- May be used to expand the soldTo, invoice sections and billing profiles.
    '''
    return _call_az("az billing account show", locals())


def update(name, billing_profiles_value=None, departments=None, display_name=None, enrollment_accounts=None, no_wait=None, sold_to=None):
    '''
    Update the properties of a billing account. Currently, displayName and address can be updated. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

    Required Parameters:
    - name -- The ID that uniquely identifies a billing account.

    Optional Parameters:
    - billing_profiles_value -- The billing profiles associated with the billing account. Expected value: json-string/@json-file.
    - departments -- The departments associated to the enrollment. Expected value: json-string/@json-file.
    - display_name -- The billing account name.
    - enrollment_accounts -- The accounts associated to the enrollment. Expected value: json-string/@json-file.
    - no_wait -- Do not wait for the long-running operation to finish.
    - sold_to -- The address of the individual or organization that is responsible for the billing account.
    '''
    return _call_az("az billing account update", locals())


def wait(name, created=None, custom=None, deleted=None, exists=None, expand=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the billing account is met.

    Required Parameters:
    - name -- The ID that uniquely identifies a billing account.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - expand -- May be used to expand the soldTo, invoice sections and billing profiles.
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az billing account wait", locals())

