'''
Demos for designing, developing and demonstrating Azure CLI.
'''
from .. pyaz_utils import _call_az

def style(theme=None):
    '''
    A demo showing supported text styles.

    Optional Parameters:
    - theme -- The theme to format styled text. If unspecified, the default theme is used.
    '''
    return _call_az("az demo style", locals())

