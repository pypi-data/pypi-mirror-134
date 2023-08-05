'''
Manage billing profile of billing account
'''
from ... pyaz_utils import _call_az

def list(account_name, expand=None):
    '''
    List the billing profiles that a user has access to. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.

    Optional Parameters:
    - expand -- May be used to expand the invoice sections.
    '''
    return _call_az("az billing profile list", locals())


def show(account_name, name, expand=None):
    '''
    Get a billing profile by its ID. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- The ID that uniquely identifies a billing profile.

    Optional Parameters:
    - expand -- May be used to expand the invoice sections.
    '''
    return _call_az("az billing profile show", locals())


def create(account_name, name, bill_to=None, display_name=None, enabled_azure_plans=None, invoice_email_opt_in=None, invoice_sections_value=None, no_wait=None, po_number=None):
    '''
    Creates or updates a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- The ID that uniquely identifies a billing profile.

    Optional Parameters:
    - bill_to -- Billing address.
    - display_name -- The name of the billing profile.
    - enabled_azure_plans -- Information about the enabled azure plans.
    - invoice_email_opt_in -- Flag controlling whether the invoices for the billing profile are sent through email.
    - invoice_sections_value -- The invoice sections associated to the billing profile. Expected value: json-string/@json-file.
    - no_wait -- Do not wait for the long-running operation to finish.
    - po_number -- The purchase order name that will appear on the invoices generated for the billing profile.
    '''
    return _call_az("az billing profile create", locals())


def update(account_name, name, bill_to=None, display_name=None, enabled_azure_plans=None, invoice_email_opt_in=None, invoice_sections_value=None, no_wait=None, po_number=None):
    '''
    Creates or updates a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- The ID that uniquely identifies a billing profile.

    Optional Parameters:
    - bill_to -- Billing address.
    - display_name -- The name of the billing profile.
    - enabled_azure_plans -- Information about the enabled azure plans.
    - invoice_email_opt_in -- Flag controlling whether the invoices for the billing profile are sent through email.
    - invoice_sections_value -- The invoice sections associated to the billing profile. Expected value: json-string/@json-file.
    - no_wait -- Do not wait for the long-running operation to finish.
    - po_number -- The purchase order name that will appear on the invoices generated for the billing profile.
    '''
    return _call_az("az billing profile update", locals())


def wait(account_name, name, created=None, custom=None, deleted=None, exists=None, expand=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the billing profile is met.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- The ID that uniquely identifies a billing profile.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - expand -- May be used to expand the invoice sections.
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az billing profile wait", locals())

