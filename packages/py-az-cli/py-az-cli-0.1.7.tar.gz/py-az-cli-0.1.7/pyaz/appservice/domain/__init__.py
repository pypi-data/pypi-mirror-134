'''
Manage custom domains.
'''
from ... pyaz_utils import _call_az

def create(contact_info, hostname, resource_group, accept_terms=None, auto_renew=None, dryrun=None, privacy=None, tags=None):
    '''
    Create and purchase a custom domain.

    Required Parameters:
    - contact_info -- The file path to a JSON object with your contact info for domain registration. Please see the following link for the format of the JSON file expected: https://github.com/AzureAppServiceCLI/appservice_domains_templates/blob/master/contact_info.json
    - hostname -- Name of the custom domain
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - accept_terms -- By using this flag, you are accepting the conditions shown using the --show-hostname-purchase-terms flag. 
    - auto_renew -- Enable auto-renew on the domain
    - dryrun -- Show summary of the purchase and create operation instead of executing it
    - privacy -- Enable privacy protection
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az appservice domain create", locals())


def show_terms(hostname):
    '''
    Show the legal terms for purchasing and creating a custom domain.

    Required Parameters:
    - hostname -- Name of the custom domain
    '''
    return _call_az("az appservice domain show-terms", locals())

