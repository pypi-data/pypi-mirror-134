'''
Bicep CLI command group.
'''
from .. pyaz_utils import _call_az

def install(target_platform=None, version=None):
    '''
    Install Bicep CLI.

    Optional Parameters:
    - target_platform -- The platform the Bicep CLI will be running on. Set this to skip automatic platform detection if it does not work properly.
    - version -- The version of Bicep CLI to be installed. Default to the latest if not specified.
    '''
    return _call_az("az bicep install", locals())


def uninstall():
    '''
    Uninstall Bicep CLI.
    '''
    return _call_az("az bicep uninstall", locals())


def upgrade(target_platform=None):
    '''
    Upgrade Bicep CLI to the latest version.

    Optional Parameters:
    - target_platform -- The platform the Bicep CLI will be running on. Set this to skip automatic platform detection if it does not work properly.
    '''
    return _call_az("az bicep upgrade", locals())


def build(file, outdir=None, outfile=None, stdout=None):
    '''
    Build a Bicep file.

    Required Parameters:
    - file -- The path to the Bicep file to build in the file system.

    Optional Parameters:
    - outdir -- When set, saves the output at the specified directory.
    - outfile -- When set, saves the output as the specified file path.
    - stdout -- When set, prints all output to stdout instead of corresponding files.
    '''
    return _call_az("az bicep build", locals())


def decompile(file):
    '''
    Attempt to decompile an ARM template file to a Bicep file.

    Required Parameters:
    - file -- The path to the ARM template to decompile in the file system.
    '''
    return _call_az("az bicep decompile", locals())


def publish(file, target):
    '''
    Publish a bicep file to a remote module registry.

    Required Parameters:
    - file -- The path to the Bicep module file to publish in the file system.
    - target -- The target location where the Bicep module will be published.
    '''
    return _call_az("az bicep publish", locals())


def version():
    '''
    Show the installed version of Bicep CLI.
    '''
    return _call_az("az bicep version", locals())


def list_versions():
    '''
    List out all available versions of Bicep CLI.
    '''
    return _call_az("az bicep list-versions", locals())

