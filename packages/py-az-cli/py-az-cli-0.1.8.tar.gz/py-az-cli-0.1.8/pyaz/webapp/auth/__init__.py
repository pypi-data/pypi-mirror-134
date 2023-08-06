'''
Manage webapp authentication and authorization. To use v2 auth commands, run "az extension add --name authV2" to add the authV2 CLI extension.
'''
from ... pyaz_utils import _call_az

def show(name, resource_group, slot=None):
    '''
    Show the authentification settings for the webapp.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp auth show", locals())


def update(name, resource_group, aad_allowed_token_audiences=None, aad_client_id=None, aad_client_secret=None, aad_client_secret_certificate_thumbprint=None, aad_token_issuer_url=None, action=None, allowed_external_redirect_urls=None, enabled=None, facebook_app_id=None, facebook_app_secret=None, facebook_oauth_scopes=None, google_client_id=None, google_client_secret=None, google_oauth_scopes=None, microsoft_account_client_id=None, microsoft_account_client_secret=None, microsoft_account_oauth_scopes=None, runtime_version=None, slot=None, token_refresh_extension_hours=None, token_store=None, twitter_consumer_key=None, twitter_consumer_secret=None):
    '''
    Update the authentication settings for the webapp.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - aad_allowed_token_audiences -- One or more token audiences (space-delimited).
    - aad_client_id -- Application ID to integrate AAD organization account Sign-in into your web app
    - aad_client_secret -- AAD application secret
    - aad_client_secret_certificate_thumbprint -- Alternative to AAD Client Secret, thumbprint of a certificate used for signing purposes
    - aad_token_issuer_url -- This url can be found in the JSON output returned from your active directory endpoint using your tenantID. The endpoint can be queried from `az cloud show` at "endpoints.activeDirectory". The tenantID can be found using `az account show`. Get the "issuer" from the JSON at <active directory endpoint>/<tenantId>/.well-known/openid-configuration.
    - action -- None
    - allowed_external_redirect_urls -- One or more urls (space-delimited).
    - enabled -- None
    - facebook_app_id -- Application ID to integrate Facebook Sign-in into your web app
    - facebook_app_secret -- Facebook Application client secret
    - facebook_oauth_scopes -- One or more facebook authentication scopes (space-delimited).
    - google_client_id -- Application ID to integrate Google Sign-in into your web app
    - google_client_secret -- Google Application client secret
    - google_oauth_scopes -- One or more Google authentication scopes (space-delimited).
    - microsoft_account_client_id -- AAD V2 Application ID to integrate Microsoft account Sign-in into your web app
    - microsoft_account_client_secret -- AAD V2 Application client secret
    - microsoft_account_oauth_scopes -- One or more Microsoft authentification scopes (space-delimited).
    - runtime_version -- Runtime version of the Authentication/Authorization feature in use for the current app
    - slot -- the name of the slot. Default to the productions slot if not specified
    - token_refresh_extension_hours -- Hours, must be formattable into a float
    - token_store -- use App Service Token Store
    - twitter_consumer_key -- Application ID to integrate Twitter Sign-in into your web app
    - twitter_consumer_secret -- Twitter Application client secret
    '''
    return _call_az("az webapp auth update", locals())

