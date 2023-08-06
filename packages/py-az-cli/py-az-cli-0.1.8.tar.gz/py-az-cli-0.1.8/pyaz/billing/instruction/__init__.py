'''
Manage billing instruction
'''
from ... pyaz_utils import _call_az

def list(account_name, profile_name):
    '''
    List the instructions by billing profile id.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - profile_name -- The ID that uniquely identifies a billing profile.
    '''
    return _call_az("az billing instruction list", locals())


def show(account_name, name, profile_name):
    '''
    Show the instruction by name. These are custom billing instructions and are only applicable for certain customers.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- Instruction Name.
    - profile_name -- The ID that uniquely identifies a billing profile.
    '''
    return _call_az("az billing instruction show", locals())


def create(account_name, name, profile_name, amount=None, creation_date=None, end_date=None, start_date=None):
    '''
    Create an instruction. These are custom billing instructions and are only applicable for certain customers.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- Instruction Name.
    - profile_name -- The ID that uniquely identifies a billing profile.

    Optional Parameters:
    - amount -- The amount budgeted for this billing instruction.
    - creation_date -- The date this billing instruction was created.
    - end_date -- The date this billing instruction is no longer in effect.
    - start_date -- The date this billing instruction goes into effect.
    '''
    return _call_az("az billing instruction create", locals())


def update(account_name, name, profile_name, add=None, amount=None, creation_date=None, end_date=None, force_string=None, remove=None, set=None, start_date=None):
    '''
    Update an instruction. These are custom billing instructions and are only applicable for certain customers.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- Instruction Name.
    - profile_name -- The ID that uniquely identifies a billing profile.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - amount -- The amount budgeted for this billing instruction.
    - creation_date -- The date this billing instruction was created.
    - end_date -- The date this billing instruction is no longer in effect.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - start_date -- The date this billing instruction goes into effect.
    '''
    return _call_az("az billing instruction update", locals())

