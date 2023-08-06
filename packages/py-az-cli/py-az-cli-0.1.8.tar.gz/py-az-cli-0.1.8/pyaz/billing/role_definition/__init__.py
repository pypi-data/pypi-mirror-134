from ... pyaz_utils import _call_az

def list(account_name, invoice_section_name=None, profile_name=None):
    '''
    List the role definitions for a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.

    Optional Parameters:
    - invoice_section_name -- The ID that uniquely identifies an invoice section.
    - profile_name -- The ID that uniquely identifies a billing profile.
    '''
    return _call_az("az billing role-definition list", locals())


def show(account_name, name, invoice_section_name=None, profile_name=None):
    '''
    Show the role definition details

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- The name that uniquely identifies a role definition.

    Optional Parameters:
    - invoice_section_name -- The ID that uniquely identifies an invoice section.
    - profile_name -- The ID that uniquely identifies a billing profile.
    '''
    return _call_az("az billing role-definition show", locals())

