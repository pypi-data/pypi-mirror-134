'''
Get billing invoices for a subscription.
'''
from ... pyaz_utils import _call_az
from . import section


def list(period_end_date, period_start_date, account_name=None, profile_name=None):
    '''
    List the invoices for a subscription.

    Required Parameters:
    - period_end_date -- The end date to fetch the invoices. The date should be specified in MM-DD-YYYY format.
    - period_start_date -- The start date to fetch the invoices. The date should be specified in MM-DD-YYYY format.

    Optional Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - profile_name -- The ID that uniquely identifies a billing profile.
    '''
    return _call_az("az billing invoice list", locals())


def show(name, account_name=None, by_subscription=None):
    '''
    Get an invoice. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

    Required Parameters:
    - name -- The ID that uniquely identifies an invoice.

    Optional Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - by_subscription -- When provided, it must work with --invoice-name to get an invoice by subscription ID and invoice ID
    '''
    return _call_az("az billing invoice show", locals())


def download(account_name=None, download_token=None, download_urls=None, invoice_name=None):
    '''
    Get URL to download invoice

    Optional Parameters:
    - account_name -- The ID that uniquely identifies a billing account
    - download_token -- The download token with document source and document ID
    - download_urls -- Space-separated list of download urls for individual
    - invoice_name -- The ID that uniquely identifies an invoice
    '''
    return _call_az("az billing invoice download", locals())

