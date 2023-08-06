'''
Create a connection between a webapp and a target resource
'''
from .... pyaz_utils import _call_az

def postgres(client_type=None, connection=None, database=None, name=None, new=None, no_wait=None, resource_group=None, secret=None, server=None, source_id=None, target_id=None, target_resource_group=None):
    '''
    Create a webapp connection to postgres.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - database -- Name of postgres database. Required if '--target-id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - new -- Indicates whether to create a new postgres when creating the webapp connection
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - server -- Name of postgres server. Required if '--target-id' is not specified.
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    - target_id -- The resource id of target service. Required if ['--target-resource-group', '--server', '--database'] are not specified.
    - target_resource_group -- The resource group which contains the postgres service. Required if '--target-id' is not specified.
    '''
    return _call_az("az webapp connection create postgres", locals())


def postgres_flexible(client_type=None, connection=None, database=None, name=None, no_wait=None, resource_group=None, secret=None, server=None, source_id=None, target_id=None, target_resource_group=None):
    '''
    Create a webapp connection to postgres-flexible.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - database -- Name of postgres flexible database. Required if '--target-id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - server -- Name of postgres flexible server. Required if '--target-id' is not specified.
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    - target_id -- The resource id of target service. Required if ['--target-resource-group', '--server', '--database'] are not specified.
    - target_resource_group -- The resource group which contains the flexible postgres service. Required if '--target-id' is not specified.
    '''
    return _call_az("az webapp connection create postgres-flexible", locals())


def mysql(client_type=None, connection=None, database=None, name=None, no_wait=None, resource_group=None, secret=None, server=None, source_id=None, target_id=None, target_resource_group=None):
    '''
    Create a webapp connection to mysql.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - database -- Name of the mysql database. Required if '--target-id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - server -- Name of the mysql server. Required if '--target-id' is not specified.
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    - target_id -- The resource id of target service. Required if ['--target-resource-group', '--server', '--database'] are not specified.
    - target_resource_group -- The resource group which contains the mysql server. Required if '--target-id' is not specified.
    '''
    return _call_az("az webapp connection create mysql", locals())


def mysql_flexible(client_type=None, connection=None, database=None, name=None, no_wait=None, resource_group=None, secret=None, server=None, source_id=None, target_id=None, target_resource_group=None):
    '''
    Create a webapp connection to mysql-flexible.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - database -- Name of the mysql flexible database. Required if '--target-id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - server -- Name of the mysql flexible server. Required if '--target-id' is not specified.
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    - target_id -- The resource id of target service. Required if ['--target-resource-group', '--server', '--database'] are not specified.
    - target_resource_group -- The resource group which contains the mysql flexible server. Required if '--target-id' is not specified.
    '''
    return _call_az("az webapp connection create mysql-flexible", locals())


def cosmos_cassandra(account=None, client_type=None, connection=None, key_space=None, name=None, no_wait=None, resource_group=None, secret=None, service_principal=None, source_id=None, system_identity=None, target_id=None, target_resource_group=None, user_identity=None):
    '''
    Create a webapp connection to cosmos-cassandra.

    Optional Parameters:
    - account -- Name of the cosmos database account. Required if '--target-id' is not specified.
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - key_space -- Name of the keyspace. Required if '--target-id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - service_principal -- The service principal auth info
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    - system_identity -- The system assigned identity auth info
    - target_id -- The resource id of target service. Required if ['--target-resource-group', '--account', '--key-space'] are not specified.
    - target_resource_group -- The resource group which contains the cosmos database account. Required if '--target-id' is not specified.
    - user_identity -- The user assigned identity auth info
    '''
    return _call_az("az webapp connection create cosmos-cassandra", locals())


def cosmos_gremlin(account=None, client_type=None, connection=None, database=None, graph=None, name=None, no_wait=None, resource_group=None, secret=None, service_principal=None, source_id=None, system_identity=None, target_id=None, target_resource_group=None, user_identity=None):
    '''
    Create a webapp connection to cosmos-gremlin.

    Optional Parameters:
    - account -- Name of the cosmos database account. Required if '--target-id' is not specified.
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - database -- Name of the database. Required if '--target-id' is not specified.
    - graph -- Name of the graph. Required if '--target-id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - service_principal -- The service principal auth info
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    - system_identity -- The system assigned identity auth info
    - target_id -- The resource id of target service. Required if ['--target-resource-group', '--account', '--database', '--graph'] are not specified.
    - target_resource_group -- The resource group which contains the cosmos database account. Required if '--target-id' is not specified.
    - user_identity -- The user assigned identity auth info
    '''
    return _call_az("az webapp connection create cosmos-gremlin", locals())


def cosmos_mongo(account=None, client_type=None, connection=None, database=None, name=None, no_wait=None, resource_group=None, secret=None, service_principal=None, source_id=None, system_identity=None, target_id=None, target_resource_group=None, user_identity=None):
    '''
    Create a webapp connection to cosmos-mongo.

    Optional Parameters:
    - account -- Name of the cosmos database account. Required if '--target-id' is not specified.
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - database -- Name of the database. Required if '--target-id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - service_principal -- The service principal auth info
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    - system_identity -- The system assigned identity auth info
    - target_id -- The resource id of target service. Required if ['--target-resource-group', '--account', '--database'] are not specified.
    - target_resource_group -- The resource group which contains the cosmos database account. Required if '--target-id' is not specified.
    - user_identity -- The user assigned identity auth info
    '''
    return _call_az("az webapp connection create cosmos-mongo", locals())


def cosmos_table(account=None, client_type=None, connection=None, name=None, no_wait=None, resource_group=None, secret=None, service_principal=None, source_id=None, system_identity=None, table=None, target_id=None, target_resource_group=None, user_identity=None):
    '''
    Create a webapp connection to cosmos-table.

    Optional Parameters:
    - account -- Name of the cosmos database account. Required if '--target-id' is not specified.
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - service_principal -- The service principal auth info
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    - system_identity -- The system assigned identity auth info
    - table -- Name of the table. Required if '--target-id' is not specified.
    - target_id -- The resource id of target service. Required if ['--target-resource-group', '--account', '--table'] are not specified.
    - target_resource_group -- The resource group which contains the cosmos database account. Required if '--target-id' is not specified.
    - user_identity -- The user assigned identity auth info
    '''
    return _call_az("az webapp connection create cosmos-table", locals())


def cosmos_sql(account=None, client_type=None, connection=None, database=None, name=None, no_wait=None, resource_group=None, secret=None, service_principal=None, source_id=None, system_identity=None, target_id=None, target_resource_group=None, user_identity=None):
    '''
    Create a webapp connection to cosmos-sql.

    Optional Parameters:
    - account -- Name of the cosmos database account. Required if '--target-id' is not specified.
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - database -- Name of the database. Required if '--target-id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - service_principal -- The service principal auth info
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    - system_identity -- The system assigned identity auth info
    - target_id -- The resource id of target service. Required if ['--target-resource-group', '--account', '--database'] are not specified.
    - target_resource_group -- The resource group which contains the cosmos database account. Required if '--target-id' is not specified.
    - user_identity -- The user assigned identity auth info
    '''
    return _call_az("az webapp connection create cosmos-sql", locals())


def storage_blob(account=None, client_type=None, connection=None, name=None, new=None, no_wait=None, resource_group=None, secret=None, service_principal=None, source_id=None, system_identity=None, target_id=None, target_resource_group=None, user_identity=None):
    '''
    Create a webapp connection to storage-blob.

    Optional Parameters:
    - account -- Name of the storage account. Required if '--target-id' is not specified.
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - new -- Indicates whether to create a new storage-blob when creating the webapp connection
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - service_principal -- The service principal auth info
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    - system_identity -- The system assigned identity auth info
    - target_id -- The resource id of target service. Required if ['--target-resource-group', '--account'] are not specified.
    - target_resource_group -- The resource group which contains the storage account. Required if '--target-id' is not specified.
    - user_identity -- The user assigned identity auth info
    '''
    return _call_az("az webapp connection create storage-blob", locals())


def storage_queue(account=None, client_type=None, connection=None, name=None, no_wait=None, resource_group=None, secret=None, service_principal=None, source_id=None, system_identity=None, target_id=None, target_resource_group=None, user_identity=None):
    '''
    Create a webapp connection to storage-queue.

    Optional Parameters:
    - account -- Name of the storage account. Required if '--target-id' is not specified.
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - service_principal -- The service principal auth info
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    - system_identity -- The system assigned identity auth info
    - target_id -- The resource id of target service. Required if ['--target-resource-group', '--account'] are not specified.
    - target_resource_group -- The resource group which contains the storage account. Required if '--target-id' is not specified.
    - user_identity -- The user assigned identity auth info
    '''
    return _call_az("az webapp connection create storage-queue", locals())


def storage_file(account=None, client_type=None, connection=None, name=None, no_wait=None, resource_group=None, secret=None, source_id=None, target_id=None, target_resource_group=None):
    '''
    Create a webapp connection to storage-file.

    Optional Parameters:
    - account -- Name of the storage account. Required if '--target-id' is not specified.
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    - target_id -- The resource id of target service. Required if ['--target-resource-group', '--account'] are not specified.
    - target_resource_group -- The resource group which contains the storage account. Required if '--target-id' is not specified.
    '''
    return _call_az("az webapp connection create storage-file", locals())


def storage_table(account=None, client_type=None, connection=None, name=None, no_wait=None, resource_group=None, secret=None, source_id=None, target_id=None, target_resource_group=None):
    '''
    Create a webapp connection to storage-table.

    Optional Parameters:
    - account -- Name of the storage account. Required if '--target-id' is not specified.
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    - target_id -- The resource id of target service. Required if ['--target-resource-group', '--account'] are not specified.
    - target_resource_group -- The resource group which contains the storage account. Required if '--target-id' is not specified.
    '''
    return _call_az("az webapp connection create storage-table", locals())


def keyvault(client_type=None, connection=None, name=None, new=None, no_wait=None, resource_group=None, service_principal=None, source_id=None, system_identity=None, target_id=None, target_resource_group=None, user_identity=None, vault=None):
    '''
    Create a webapp connection to keyvault.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - new -- Indicates whether to create a new keyvault when creating the webapp connection
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - service_principal -- The service principal auth info
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    - system_identity -- The system assigned identity auth info
    - target_id -- The resource id of target service. Required if ['--target-resource-group', '--vault'] are not specified.
    - target_resource_group -- The resource group which contains the keyvault. Required if '--target-id' is not specified.
    - user_identity -- The user assigned identity auth info
    - vault -- Name of the keyvault. Required if '--target-id' is not specified.
    '''
    return _call_az("az webapp connection create keyvault", locals())


def signalr(client_type=None, connection=None, name=None, no_wait=None, resource_group=None, secret=None, service_principal=None, signalr=None, source_id=None, system_identity=None, target_id=None, target_resource_group=None, user_identity=None):
    '''
    Create a webapp connection to signalr.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - service_principal -- The service principal auth info
    - signalr -- Name of the signalr service. Required if '--target-id' is not specified.
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    - system_identity -- The system assigned identity auth info
    - target_id -- The resource id of target service. Required if ['--target-resource-group', '--signalr'] are not specified.
    - target_resource_group -- The resource group which contains the signalr. Required if '--target-id' is not specified.
    - user_identity -- The user assigned identity auth info
    '''
    return _call_az("az webapp connection create signalr", locals())


def confluent_cloud(bootstrap_server, kafka_key, kafka_secret, schema_key, schema_registry, schema_secret, client_type=None, connection=None, name=None, no_wait=None, resource_group=None, source_id=None):
    '''
    Create a webapp connection to confluent-cloud.

    Required Parameters:
    - bootstrap_server -- Kafka bootstrap server url
    - kafka_key -- Kafka API-Key (key)
    - kafka_secret -- Kafka API-Key (secret)
    - schema_key -- Schema registry API-Key (key)
    - schema_registry -- Schema registry url
    - schema_secret -- Schema registry API-Key (secret)

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the connection
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    '''
    return _call_az("az webapp connection create confluent-cloud", locals())

