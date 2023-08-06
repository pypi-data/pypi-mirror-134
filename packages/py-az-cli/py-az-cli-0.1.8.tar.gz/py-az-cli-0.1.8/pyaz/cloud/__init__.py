'''
Manage registered Azure clouds.
'''
from .. pyaz_utils import _call_az

def list():
    '''
    List registered clouds.
    '''
    return _call_az("az cloud list", locals())


def show(name=None):
    '''
    Get the details of a registered cloud.

    Optional Parameters:
    - name -- Name of a registered cloud.
    '''
    return _call_az("az cloud show", locals())


def register(name, cloud_config=None, endpoint_active_directory=None, endpoint_active_directory_data_lake_resource_id=None, endpoint_active_directory_graph_resource_id=None, endpoint_active_directory_resource_id=None, endpoint_gallery=None, endpoint_management=None, endpoint_resource_manager=None, endpoint_sql_management=None, endpoint_vm_image_alias_doc=None, profile=None, suffix_acr_login_server_endpoint=None, suffix_azure_datalake_analytics_catalog_and_job_endpoint=None, suffix_azure_datalake_store_file_system_endpoint=None, suffix_keyvault_dns=None, suffix_sql_server_hostname=None, suffix_storage_endpoint=None):
    '''
    Register a cloud.

    Required Parameters:
    - name -- Name of a registered cloud

    Optional Parameters:
    - cloud_config -- JSON encoded cloud configuration. Use @{file} to load from a file.
    - endpoint_active_directory -- The Active Directory login endpoint
    - endpoint_active_directory_data_lake_resource_id -- The Active Directory resource ID for data lake services
    - endpoint_active_directory_graph_resource_id -- The Active Directory resource ID
    - endpoint_active_directory_resource_id -- The resource ID to obtain AD tokens for
    - endpoint_gallery -- The template gallery endpoint
    - endpoint_management -- The management service endpoint
    - endpoint_resource_manager -- The resource management endpoint
    - endpoint_sql_management -- The sql server management endpoint
    - endpoint_vm_image_alias_doc -- The uri of the document which caches commonly used virtual machine images
    - profile -- Profile to use for this cloud
    - suffix_acr_login_server_endpoint -- The Azure Container Registry login server suffix
    - suffix_azure_datalake_analytics_catalog_and_job_endpoint -- The Data Lake analytics job and catalog service dns suffix
    - suffix_azure_datalake_store_file_system_endpoint -- The Data Lake store filesystem service dns suffix
    - suffix_keyvault_dns -- The Key Vault service dns suffix
    - suffix_sql_server_hostname -- The dns suffix for sql servers
    - suffix_storage_endpoint -- The endpoint suffix for storage accounts
    '''
    return _call_az("az cloud register", locals())


def unregister(name):
    '''
    Unregister a cloud.

    Required Parameters:
    - name -- Name of a registered cloud
    '''
    return _call_az("az cloud unregister", locals())


def set(name, profile=None):
    '''
    Set the active cloud.

    Required Parameters:
    - name -- Name of a registered cloud

    Optional Parameters:
    - profile -- Profile to use for this cloud
    '''
    return _call_az("az cloud set", locals())


def update(cloud_config=None, endpoint_active_directory=None, endpoint_active_directory_data_lake_resource_id=None, endpoint_active_directory_graph_resource_id=None, endpoint_active_directory_resource_id=None, endpoint_gallery=None, endpoint_management=None, endpoint_resource_manager=None, endpoint_sql_management=None, endpoint_vm_image_alias_doc=None, name=None, profile=None, suffix_acr_login_server_endpoint=None, suffix_azure_datalake_analytics_catalog_and_job_endpoint=None, suffix_azure_datalake_store_file_system_endpoint=None, suffix_keyvault_dns=None, suffix_sql_server_hostname=None, suffix_storage_endpoint=None):
    '''
    Update the configuration of a cloud.

    Optional Parameters:
    - cloud_config -- JSON encoded cloud configuration. Use @{file} to load from a file.
    - endpoint_active_directory -- The Active Directory login endpoint
    - endpoint_active_directory_data_lake_resource_id -- The Active Directory resource ID for data lake services
    - endpoint_active_directory_graph_resource_id -- The Active Directory resource ID
    - endpoint_active_directory_resource_id -- The resource ID to obtain AD tokens for
    - endpoint_gallery -- The template gallery endpoint
    - endpoint_management -- The management service endpoint
    - endpoint_resource_manager -- The resource management endpoint
    - endpoint_sql_management -- The sql server management endpoint
    - endpoint_vm_image_alias_doc -- The uri of the document which caches commonly used virtual machine images
    - name -- Name of a registered cloud.
    - profile -- Profile to use for this cloud
    - suffix_acr_login_server_endpoint -- The Azure Container Registry login server suffix
    - suffix_azure_datalake_analytics_catalog_and_job_endpoint -- The Data Lake analytics job and catalog service dns suffix
    - suffix_azure_datalake_store_file_system_endpoint -- The Data Lake store filesystem service dns suffix
    - suffix_keyvault_dns -- The Key Vault service dns suffix
    - suffix_sql_server_hostname -- The dns suffix for sql servers
    - suffix_storage_endpoint -- The endpoint suffix for storage accounts
    '''
    return _call_az("az cloud update", locals())


def list_profiles(name=None, show_all=None):
    '''
    List the supported profiles for a cloud.

    Optional Parameters:
    - name -- Name of a registered cloud.
    - show_all -- Show all available profiles supported in the CLI.
    '''
    return _call_az("az cloud list-profiles", locals())

