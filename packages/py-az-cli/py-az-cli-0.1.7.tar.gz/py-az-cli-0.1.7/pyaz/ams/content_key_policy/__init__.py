from ... pyaz_utils import _call_az
from . import option


def create(account_name, name, policy_option_name, resource_group, alt_rsa_token_keys=None, alt_symmetric_token_keys=None, alt_x509_token_keys=None, ask=None, audience=None, clear_key_configuration=None, description=None, fair_play_pfx=None, fair_play_pfx_password=None, fp_playback_duration_seconds=None, fp_storage_duration_seconds=None, issuer=None, open_id_connect_discovery_document=None, open_restriction=None, play_ready_template=None, rental_and_lease_key_type=None, rental_duration=None, token_claims=None, token_key=None, token_key_type=None, token_type=None, widevine_template=None):
    '''
    Create a new content key policy.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The content key policy name.
    - policy_option_name -- The content key policy option name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - alt_rsa_token_keys -- Space-separated list of alternate rsa token keys.
    - alt_symmetric_token_keys -- Space-separated list of alternate symmetric token keys.
    - alt_x509_token_keys -- Space-separated list of alternate x509 certificate token keys.
    - ask -- The key that must be used as FairPlay Application Secret Key, which is a 32 character hex string.
    - audience -- The audience for the token.
    - clear_key_configuration -- Use Clear Key configuration, a.k.a AES encryption. It's intended for non-DRM keys.
    - description -- The content key policy description.
    - fair_play_pfx -- The filepath to a FairPlay certificate file in PKCS 12 (pfx) format (including private key).
    - fair_play_pfx_password -- The password encrypting FairPlay certificate in PKCS 12 (pfx) format.
    - fp_playback_duration_seconds -- Playback duration
    - fp_storage_duration_seconds -- Storage duration
    - issuer -- The token issuer.
    - open_id_connect_discovery_document -- The OpenID connect discovery document.
    - open_restriction -- Use open restriction. License or key will be delivered on every request. Not recommended for production environments.
    - play_ready_template -- JSON PlayReady license template. Use @{file} to load from a file.
    - rental_and_lease_key_type -- The rental and lease key type. Available values: Undefined, DualExpiry, PersistentUnlimited, PersistentLimited.
    - rental_duration -- The rental duration. Must be greater than or equal to 0.
    - token_claims -- Space-separated required token claims in '[key=value]' format.
    - token_key -- Either a string (for symmetric key) or a filepath to a certificate (x509) or public key (rsa). Must be used in conjunction with --token-key-type.
    - token_key_type -- The type of the token key to be used for the primary verification key. Allowed values: Symmetric, RSA, X509
    - token_type -- The type of token. Allowed values: Jwt, Swt.
    - widevine_template -- JSON Widevine license template. Use @{file} to load from a file.
    '''
    return _call_az("az ams content-key-policy create", locals())


def show(account_name, name, resource_group, with_secrets=None):
    '''
    Show an existing content key policy.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The content key policy name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - with_secrets -- Include secret values of the content key policy.
    '''
    return _call_az("az ams content-key-policy show", locals())


def delete(account_name, name, resource_group):
    '''
    Delete a content key policy.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The content key policy name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams content-key-policy delete", locals())


def list(account_name, resource_group, filter=None, orderby=None, top=None):
    '''
    List all the content key policies within an Azure Media Services account.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - filter -- Restricts the set of items returned.
    - orderby -- Specifies the key by which the result collection should be ordered.
    - top -- Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
    '''
    return _call_az("az ams content-key-policy list", locals())


def update(account_name, name, resource_group, add=None, description=None, force_string=None, remove=None, set=None):
    '''
    Update an existing content key policy.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The content key policy name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - description -- The content key policy description.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az ams content-key-policy update", locals())

