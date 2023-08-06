'''
Update a webapp connection
'''
from .... pyaz_utils import _call_az

def postgres(client_type=None, connection=None, id=None, name=None, no_wait=None, resource_group=None, secret=None):
    '''
    Update a webapp to postgres connection.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    '''
    return _call_az("az webapp connection update postgres", locals())


def postgres_flexible(client_type=None, connection=None, id=None, name=None, no_wait=None, resource_group=None, secret=None):
    '''
    Update a webapp to postgres-flexible connection.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    '''
    return _call_az("az webapp connection update postgres-flexible", locals())


def mysql(client_type=None, connection=None, id=None, name=None, no_wait=None, resource_group=None, secret=None):
    '''
    Update a webapp to mysql connection.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    '''
    return _call_az("az webapp connection update mysql", locals())


def mysql_flexible(client_type=None, connection=None, id=None, name=None, no_wait=None, resource_group=None, secret=None):
    '''
    Update a webapp to mysql-flexible connection.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    '''
    return _call_az("az webapp connection update mysql-flexible", locals())


def cosmos_cassandra(client_type=None, connection=None, id=None, name=None, no_wait=None, resource_group=None, secret=None, service_principal=None, system_identity=None, user_identity=None):
    '''
    Update a webapp to cosmos-cassandra connection.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - service_principal -- The service principal auth info
    - system_identity -- The system assigned identity auth info
    - user_identity -- The user assigned identity auth info
    '''
    return _call_az("az webapp connection update cosmos-cassandra", locals())


def cosmos_gremlin(client_type=None, connection=None, id=None, name=None, no_wait=None, resource_group=None, secret=None, service_principal=None, system_identity=None, user_identity=None):
    '''
    Update a webapp to cosmos-gremlin connection.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - service_principal -- The service principal auth info
    - system_identity -- The system assigned identity auth info
    - user_identity -- The user assigned identity auth info
    '''
    return _call_az("az webapp connection update cosmos-gremlin", locals())


def cosmos_mongo(client_type=None, connection=None, id=None, name=None, no_wait=None, resource_group=None, secret=None, service_principal=None, system_identity=None, user_identity=None):
    '''
    Update a webapp to cosmos-mongo connection.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - service_principal -- The service principal auth info
    - system_identity -- The system assigned identity auth info
    - user_identity -- The user assigned identity auth info
    '''
    return _call_az("az webapp connection update cosmos-mongo", locals())


def cosmos_table(client_type=None, connection=None, id=None, name=None, no_wait=None, resource_group=None, secret=None, service_principal=None, system_identity=None, user_identity=None):
    '''
    Update a webapp to cosmos-table connection.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - service_principal -- The service principal auth info
    - system_identity -- The system assigned identity auth info
    - user_identity -- The user assigned identity auth info
    '''
    return _call_az("az webapp connection update cosmos-table", locals())


def cosmos_sql(client_type=None, connection=None, id=None, name=None, no_wait=None, resource_group=None, secret=None, service_principal=None, system_identity=None, user_identity=None):
    '''
    Update a webapp to cosmos-sql connection.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - service_principal -- The service principal auth info
    - system_identity -- The system assigned identity auth info
    - user_identity -- The user assigned identity auth info
    '''
    return _call_az("az webapp connection update cosmos-sql", locals())


def storage_blob(client_type=None, connection=None, id=None, name=None, no_wait=None, resource_group=None, secret=None, service_principal=None, system_identity=None, user_identity=None):
    '''
    Update a webapp to storage-blob connection.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - service_principal -- The service principal auth info
    - system_identity -- The system assigned identity auth info
    - user_identity -- The user assigned identity auth info
    '''
    return _call_az("az webapp connection update storage-blob", locals())


def storage_queue(client_type=None, connection=None, id=None, name=None, no_wait=None, resource_group=None, secret=None, service_principal=None, system_identity=None, user_identity=None):
    '''
    Update a webapp to storage-queue connection.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - service_principal -- The service principal auth info
    - system_identity -- The system assigned identity auth info
    - user_identity -- The user assigned identity auth info
    '''
    return _call_az("az webapp connection update storage-queue", locals())


def storage_file(client_type=None, connection=None, id=None, name=None, no_wait=None, resource_group=None, secret=None):
    '''
    Update a webapp to storage-file connection.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    '''
    return _call_az("az webapp connection update storage-file", locals())


def storage_table(client_type=None, connection=None, id=None, name=None, no_wait=None, resource_group=None, secret=None):
    '''
    Update a webapp to storage-table connection.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    '''
    return _call_az("az webapp connection update storage-table", locals())


def keyvault(client_type=None, connection=None, id=None, name=None, no_wait=None, resource_group=None, service_principal=None, system_identity=None, user_identity=None):
    '''
    Update a webapp to keyvault connection.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - service_principal -- The service principal auth info
    - system_identity -- The system assigned identity auth info
    - user_identity -- The user assigned identity auth info
    '''
    return _call_az("az webapp connection update keyvault", locals())


def signalr(client_type=None, connection=None, id=None, name=None, no_wait=None, resource_group=None, secret=None, service_principal=None, system_identity=None, user_identity=None):
    '''
    Update a webapp to signalr connection.

    Optional Parameters:
    - client_type -- The client type used on the webapp
    - connection -- Name of the webapp connection.
    - id -- The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - secret -- The secret auth info
    - service_principal -- The service principal auth info
    - system_identity -- The system assigned identity auth info
    - user_identity -- The user assigned identity auth info
    '''
    return _call_az("az webapp connection update signalr", locals())


def confluent_cloud(connection, bootstrap_server=None, client_type=None, kafka_key=None, kafka_secret=None, name=None, no_wait=None, resource_group=None, schema_key=None, schema_registry=None, schema_secret=None, source_id=None):
    '''
    Update a webapp to confluent-cloud connection.

    Required Parameters:
    - connection -- Name of the connection

    Optional Parameters:
    - bootstrap_server -- Kafka bootstrap server url
    - client_type -- The client type used on the webapp
    - kafka_key -- Kafka API-Key (key)
    - kafka_secret -- Kafka API-Key (secret)
    - name -- Name of the webapp. Required if '--source-id' is not specified.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- The resource group which contains the webapp. Required if '--source-id' is not specified.
    - schema_key -- Schema registry API-Key (key)
    - schema_registry -- Schema registry url
    - schema_secret -- Schema registry API-Key (secret)
    - source_id -- The resource id of a webapp. Required if ['--resource-group', '--name'] are not specified.
    '''
    return _call_az("az webapp connection update confluent-cloud", locals())

