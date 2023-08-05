'''
billing transaction
'''
from ... pyaz_utils import _call_az

def list(account_name, invoice_name):
    '''
    List the transactions for an invoice. Transactions include purchases, refunds and Azure usage charges.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - invoice_name -- The ID that uniquely identifies an invoice.
    '''
    return _call_az("az billing transaction list", locals())

