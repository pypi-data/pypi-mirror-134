'''
Manage a Data Lake Store filesystem.
'''
from ... pyaz_utils import _call_az
from . import access


def show(account, path):
    '''
    Get file or folder information in a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - path -- The path in the specified Data Lake Store account where the action should take place. In the format '/folder/file.txt', where the first '/' after the DNS indicates the root of the file system.
    '''
    return _call_az("az dls fs show", locals())


def list(account, path):
    '''
    List the files and folders in a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - path -- The path in the specified Data Lake Store account where the action should take place. In the format '/folder/file.txt', where the first '/' after the DNS indicates the root of the file system.
    '''
    return _call_az("az dls fs list", locals())


def create(account, path, content=None, folder=None, force=None):
    '''
    Creates a file or folder in a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - path -- The path in the specified Data Lake Store account where the action should take place. In the format '/folder/file.txt', where the first '/' after the DNS indicates the root of the file system.

    Optional Parameters:
    - content -- None
    - folder -- Indicates that this new item is a folder and not a file.
    - force -- Indicates that, if the file or folder exists, it should be overwritten
    '''
    return _call_az("az dls fs create", locals())


def append(account, content, path):
    '''
    Append content to a file in a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - content -- None
    - path -- The path in the specified Data Lake Store account where the action should take place. In the format '/folder/file.txt', where the first '/' after the DNS indicates the root of the file system.
    '''
    return _call_az("az dls fs append", locals())


def delete(account, path, recurse=None):
    '''
    Delete a file or folder in a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - path -- The path in the specified Data Lake Store account where the action should take place. In the format '/folder/file.txt', where the first '/' after the DNS indicates the root of the file system.

    Optional Parameters:
    - recurse -- Indicates this should be a recursive delete of the folder.
    '''
    return _call_az("az dls fs delete", locals())


def upload(account, destination_path, source_path, block_size=None, buffer_size=None, chunk_size=None, overwrite=None, thread_count=None):
    '''
    Upload a file or folder to a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - destination_path -- None
    - source_path -- None

    Optional Parameters:
    - block_size -- Number of bytes for a block. Within each chunk, we write a smaller block for each API call. This block cannot be bigger than a chunk.
    - buffer_size -- Number of bytes for internal buffer. This block cannot be bigger than a chunk and cannot be smaller than a block.
    - chunk_size -- Number of bytes for a chunk. Large files are split into chunks. Files smaller than this number will always be transferred in a single thread.
    - overwrite -- Indicates that, if the destination file or folder exists, it should be overwritten
    - thread_count -- Specify the parallelism of the upload. Default is the number of cores in the local machine.
    '''
    return _call_az("az dls fs upload", locals())


def download(account, destination_path, source_path, block_size=None, buffer_size=None, chunk_size=None, overwrite=None, thread_count=None):
    '''
    Download a file or folder from a Data Lake Store account to the local machine.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - destination_path -- None
    - source_path -- None

    Optional Parameters:
    - block_size -- Number of bytes for a block. Within each chunk, we write a smaller block for each API call. This block cannot be bigger than a chunk.
    - buffer_size -- Number of bytes for internal buffer. This block cannot be bigger than a chunk and cannot be smaller than a block.
    - chunk_size -- Number of bytes for a chunk. Large files are split into chunks. Files smaller than this number will always be transferred in a single thread.
    - overwrite -- Indicates that, if the destination file or folder exists, it should be overwritten
    - thread_count -- Specify the parallelism of the download. Default is the number of cores in the local machine.
    '''
    return _call_az("az dls fs download", locals())


def test(account, path):
    '''
    Test for the existence of a file or folder in a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - path -- The path in the specified Data Lake Store account where the action should take place. In the format '/folder/file.txt', where the first '/' after the DNS indicates the root of the file system.
    '''
    return _call_az("az dls fs test", locals())


def preview(account, path, force=None, length=None, offset=None):
    '''
    Preview the content of a file in a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - path -- The path in the specified Data Lake Store account where the action should take place. In the format '/folder/file.txt', where the first '/' after the DNS indicates the root of the file system.

    Optional Parameters:
    - force -- Indicates that, if the preview is larger than 1MB, still retrieve it. This can potentially be very slow, depending on how large the file is.
    - length -- None
    - offset -- None
    '''
    return _call_az("az dls fs preview", locals())


def join(account, destination_path, source_paths, force=None):
    '''
    Join files in a Data Lake Store account into one file.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - destination_path -- None
    - source_paths -- The list of files in the specified Data Lake Store account to join.

    Optional Parameters:
    - force -- Indicates that, if the destination file already exists, it should be overwritten
    '''
    return _call_az("az dls fs join", locals())


def move(account, destination_path, source_path, force=None):
    '''
    Move a file or folder in a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - destination_path -- None
    - source_path -- None

    Optional Parameters:
    - force -- Indicates that, if the destination file or folder already exists, it should be overwritten and replaced with the file or folder being moved.
    '''
    return _call_az("az dls fs move", locals())


def set_expiry(account, expiration_time, path):
    '''
    Set the expiration time for a file.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - expiration_time -- The absolute value of the expiration time expressed as milliseconds since the epoch.
    - path -- The path in the specified Data Lake Store account where the action should take place. In the format '/folder/file.txt', where the first '/' after the DNS indicates the root of the file system.
    '''
    return _call_az("az dls fs set-expiry", locals())


def remove_expiry(account, path):
    '''
    Remove the expiration time for a file.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - path -- The path in the specified Data Lake Store account where the action should take place. In the format '/folder/file.txt', where the first '/' after the DNS indicates the root of the file system.
    '''
    return _call_az("az dls fs remove-expiry", locals())

