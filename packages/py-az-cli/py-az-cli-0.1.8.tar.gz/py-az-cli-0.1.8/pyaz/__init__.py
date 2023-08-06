from . pyaz_utils import _call_az
from . import account, acr, acs, aks, apim, appconfig, appservice, aro, batchai, bicep, bot, cache, cdn, cloud, cognitiveservices, config, container, cosmosdb, databoxedge, demo, deployment, deployment_scripts, disk, disk_access, disk_encryption_set, dms, extension, feature, functionapp, group, hdinsight, identity, image, keyvault, lab, local_context, lock, logicapp, managedapp, monitor, network, openshift, ppg, provider, redis, resource, sig, signalr, snapshot, sql, sshkey, staticwebapp, storage, tag, term, ts, vm, vmss, webapp


def configure(defaults=None, list_defaults=None, scope=None):
    '''
    Manage Azure CLI configuration. This command is interactive.

    Optional Parameters:
    - defaults -- None
    - list_defaults -- list all applicable defaults
    - scope -- scope of defaults. Using "local" for settings only effective under current folder
    '''
    return _call_az("az configure", locals())


def feedback():
    '''
    Send feedback to the Azure CLI Team.
    '''
    return _call_az("az feedback", locals())


def find():
    '''
    I'm an AI robot, my advice is based on our Azure documentation as well as the usage patterns of Azure CLI and Azure ARM users. Using me improves Azure products and documentation.
    '''
    return _call_az("az find", locals())


def interactive(style=None, update=None):
    '''
    Start interactive mode. Installs the Interactive extension if not installed already.

    Optional Parameters:
    - style -- The colors of the shell.
    - update -- Update the Interactive extension to the latest available.
    '''
    return _call_az("az interactive", locals())


def login(allow_no_subscriptions=None, federated_token=None, password=None, scope=None, service_principal=None, tenant=None, use_cert_sn_issuer=None, use_device_code=None, username=None):
    '''
    Log in to Azure.

    Optional Parameters:
    - allow_no_subscriptions -- Support access tenants without subscriptions. It's uncommon but useful to run tenant level commands, such as 'az ad'
    - federated_token -- Federated token that can be used for OIDC token exchange.
    - password -- Credentials like user password, or for a service principal, provide client secret or a pem file with key and public certificate. Will prompt if not given.
    - scope -- Used in the /authorize request. It can cover only one static resource.
    - service_principal -- The credential representing a service principal.
    - tenant -- The AAD tenant, must provide when using service principals.
    - use_cert_sn_issuer -- used with a service principal configured with Subject Name and Issuer Authentication in order to support automatic certificate rolls
    - use_device_code -- Use CLI's old authentication flow based on device code. CLI will also use this if it can't launch a browser in your behalf, e.g. in remote SSH or Cloud Shell
    - username -- user name, service principal, or managed service identity ID
    '''
    return _call_az("az login", locals())


def logout(username=None):
    '''
    

    Optional Parameters:
    - username -- account user, if missing, logout the current active account
    '''
    return _call_az("az logout", locals())


def self_test():
    '''
    Runs a self-test of the CLI.
    '''
    return _call_az("az self-test", locals())


def rest(url, body=None, headers=None, method=None, output_file=None, resource=None, skip_authorization_header=None, uri_parameters=None):
    '''
    Invoke a custom request.

    Required Parameters:
    - url -- Request URL. If it doesn't start with a host, CLI assumes it as an Azure resource ID and prefixes it with the ARM endpoint of the current cloud shown by `az cloud show --query endpoints.resourceManager`. Common token {subscriptionId} will be replaced with the current subscription ID specified by `az account set`

    Optional Parameters:
    - body -- Request body. Use @{file} to load from a file. For quoting issues in different terminals, see https://github.com/Azure/azure-cli/blob/dev/doc/use_cli_effectively.md#quoting-issues
    - headers -- Space-separated headers in KEY=VALUE format or JSON string. Use @{file} to load from a file
    - method -- HTTP request method
    - output_file -- save response payload to a file
    - resource -- Resource url for which CLI should acquire a token from AAD in order to access the service. The token will be placed in the Authorization header. By default, CLI can figure this out based on --url argument, unless you use ones not in the list of "az cloud show --query endpoints"
    - skip_authorization_header -- Do not auto-append Authorization header
    - uri_parameters -- Query parameters in the URL. Space-separated queries in KEY=VALUE format or JSON string. Use @{file} to load from a file
    '''
    return _call_az("az rest", locals())


def version():
    '''
    Show the versions of Azure CLI modules and extensions in JSON format by default or format configured by --output
    '''
    return _call_az("az version", locals())


def upgrade(all=None, yes=None):
    '''
    Upgrade Azure CLI and extensions

    Optional Parameters:
    - all -- Enable updating extensions as well.
    - yes -- Do not prompt for checking release notes.
    '''
    return _call_az("az upgrade", locals())

