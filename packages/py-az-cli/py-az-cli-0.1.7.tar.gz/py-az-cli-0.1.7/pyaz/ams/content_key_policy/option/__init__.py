from .... pyaz_utils import _call_az

def add(account_name, name, policy_option_name, resource_group, alt_rsa_token_keys=None, alt_symmetric_token_keys=None, alt_x509_token_keys=None, ask=None, audience=None, clear_key_configuration=None, fair_play_pfx=None, fair_play_pfx_password=None, fp_playback_duration_seconds=None, fp_storage_duration_seconds=None, issuer=None, open_id_connect_discovery_document=None, open_restriction=None, play_ready_template=None, rental_and_lease_key_type=None, rental_duration=None, token_claims=None, token_key=None, token_key_type=None, token_type=None, widevine_template=None):
    '''
    Add a new option to an existing content key policy.

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
    return _call_az("az ams content-key-policy option add", locals())


def remove(account_name, name, policy_option_id, resource_group):
    '''
    Remove an option from an existing content key policy.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The content key policy name.
    - policy_option_id -- The content key policy option identifier. This value can be obtained from "policyOptionId" property by running a show operation on a content key policy resource.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams content-key-policy option remove", locals())


def update(account_name, name, policy_option_id, resource_group, add_alt_token_key=None, add_alt_token_key_type=None, ask=None, audience=None, fair_play_pfx=None, fair_play_pfx_password=None, fp_playback_duration_seconds=None, fp_storage_duration_seconds=None, issuer=None, open_id_connect_discovery_document=None, play_ready_template=None, policy_option_name=None, rental_and_lease_key_type=None, rental_duration=None, token_claims=None, token_key=None, token_key_type=None, token_type=None, widevine_template=None):
    '''
    Update an option from an existing content key policy.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The content key policy name.
    - policy_option_id -- The content key policy option identifier. This value can be obtained from "policyOptionId" property by running a show operation on a content key policy resource.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add_alt_token_key -- Creates an alternate token key with either a string (for symmetric key) or a filepath to a certificate (x509) or public key (rsa). Must be used in conjunction with --add-alt-token-key-type.
    - add_alt_token_key_type -- The type of the token key to be used for the alternate verification key. Allowed values: Symmetric, RSA, X509
    - ask -- The key that must be used as FairPlay Application Secret Key, which is a 32 character hex string.
    - audience -- The audience for the token.
    - fair_play_pfx -- The filepath to a FairPlay certificate file in PKCS 12 (pfx) format (including private key).
    - fair_play_pfx_password -- The password encrypting FairPlay certificate in PKCS 12 (pfx) format.
    - fp_playback_duration_seconds -- Playback duration
    - fp_storage_duration_seconds -- Storage duration
    - issuer -- The token issuer.
    - open_id_connect_discovery_document -- The OpenID connect discovery document.
    - play_ready_template -- JSON PlayReady license template. Use @{file} to load from a file.
    - policy_option_name -- The content key policy option name.
    - rental_and_lease_key_type -- The rental and lease key type. Available values: Undefined, DualExpiry, PersistentUnlimited, PersistentLimited.
    - rental_duration -- The rental duration. Must be greater than or equal to 0.
    - token_claims -- Space-separated required token claims in '[key=value]' format.
    - token_key -- Either a string (for symmetric key) or a filepath to a certificate (x509) or public key (rsa). Must be used in conjunction with --token-key-type.
    - token_key_type -- The type of the token key to be used for the primary verification key. Allowed values: Symmetric, RSA, X509
    - token_type -- The type of token. Allowed values: Jwt, Swt.
    - widevine_template -- JSON Widevine license template. Use @{file} to load from a file.
    '''
    return _call_az("az ams content-key-policy option update", locals())

