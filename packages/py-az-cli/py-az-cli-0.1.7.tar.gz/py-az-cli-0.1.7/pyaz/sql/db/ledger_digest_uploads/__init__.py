from .... pyaz_utils import _call_az

def show(name, resource_group, server):
    '''
    Show the current ledger digest settings.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql db ledger-digest-uploads show", locals())


def enable(endpoint, name, resource_group, server):
    '''
    Enable uploading ledger digests to an Azure Storage account or to Azure Confidential Ledger. If uploading ledger digests is already enabled, the cmdlet resets the digest storage endpoint to a new value.

    Required Parameters:
    - endpoint -- The endpoint of a digest storage, which can be either an Azure Blob storage or a ledger in Azure Confidential Ledger.
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql db ledger-digest-uploads enable", locals())


def disable(name, resource_group, server):
    '''
    Disable uploading ledger digests.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql db ledger-digest-uploads disable", locals())

