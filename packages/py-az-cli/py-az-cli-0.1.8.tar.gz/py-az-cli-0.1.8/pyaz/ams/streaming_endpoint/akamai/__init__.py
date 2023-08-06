from .... pyaz_utils import _call_az

def add(account_name, name, resource_group, base64_key=None, expiration=None, identifier=None):
    '''
    Add an AkamaiAccessControl to an existing streaming endpoint.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the streaming endpoint.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - base64_key -- Base64-encoded authentication key that will be used by the CDN. The authentication key provided by Akamai is an ASCII encoded string, and must be converted to bytes and then base64 encoded.
    - expiration -- The ISO 8601 DateTime value that specifies when the Akamai authentication expires.
    - identifier -- The identifier for the authentication key. This is the nonce provided by Akamai.
    '''
    return _call_az("az ams streaming-endpoint akamai add", locals())


def remove(account_name, identifier, name, resource_group):
    '''
    Remove an AkamaiAccessControl from an existing streaming endpoint.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - identifier -- The identifier for the authentication key. This is the nonce provided by Akamai.
    - name -- The name of the streaming endpoint.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams streaming-endpoint akamai remove", locals())

