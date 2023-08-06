from ... pyaz_utils import _call_az

def init_recovery(sd_exchange_key, hsm_name=None, id=None):
    '''
    Retrieve the exchange key of the HSM.

    Required Parameters:
    - sd_exchange_key -- Local file path to store the exported key.

    Optional Parameters:
    - hsm_name -- Name of the HSM. Can be omitted if --id is specified.
    - id -- Full URI of the HSM.
    '''
    return _call_az("az keyvault security-domain init-recovery", locals())


def upload(sd_exchange_key, sd_file, sd_wrapping_keys, hsm_name=None, id=None, no_wait=None, passwords=None):
    '''
    Start to restore the HSM.

    Required Parameters:
    - sd_exchange_key -- The exchange key for security domain.
    - sd_file -- This file contains security domain encrypted using SD Exchange file downloaded in security-domain init-recovery command.
    - sd_wrapping_keys -- Space-separated file paths to PEM files containing private keys.

    Optional Parameters:
    - hsm_name -- Name of the HSM. Can be omitted if --id is specified.
    - id -- Full URI of the HSM.
    - no_wait -- Do not wait for the long-running operation to finish.
    - passwords -- Space-separated password list for --sd-wrapping-keys. CLI will match them in order. Can be omitted if your keys are without password protection.
    '''
    return _call_az("az keyvault security-domain upload", locals())


def download(sd_quorum, sd_wrapping_keys, security_domain_file, hsm_name=None, id=None, no_wait=None):
    '''
    Download the security domain file from the HSM.

    Required Parameters:
    - sd_quorum -- The minimum number of shares required to decrypt the security domain for recovery.
    - sd_wrapping_keys -- Space-separated file paths to PEM files containing public keys.
    - security_domain_file -- Path to a file where the JSON blob returned by this command is stored.

    Optional Parameters:
    - hsm_name -- Name of the HSM. Can be omitted if --id is specified.
    - id -- Full URI of the HSM.
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az keyvault security-domain download", locals())


def wait(hsm_name=None, id=None, target_operation=None):
    '''
    Place the CLI in a waiting state until HSM security domain operation is finished.

    Optional Parameters:
    - hsm_name -- Name of the HSM. Can be omitted if --id is specified.
    - id -- Full URI of the HSM.
    - target_operation -- Target operation that needs waiting.
    '''
    return _call_az("az keyvault security-domain wait", locals())

