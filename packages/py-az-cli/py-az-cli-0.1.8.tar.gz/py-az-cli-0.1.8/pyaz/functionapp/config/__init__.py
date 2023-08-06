'''
Configure a function app.
'''
from ... pyaz_utils import _call_az
from . import access_restriction, appsettings, container, hostname, ssl


def set(name, resource_group, always_on=None, auto_heal_enabled=None, ftps_state=None, generic_configurations=None, http20_enabled=None, java_container=None, java_container_version=None, java_version=None, linux_fx_version=None, min_tls_version=None, net_framework_version=None, number_of_workers=None, php_version=None, prewarmed_instance_count=None, python_version=None, remote_debugging_enabled=None, slot=None, startup_file=None, use_32bit_worker_process=None, vnet_route_all_enabled=None, web_sockets_enabled=None):
    '''
    Set an existing function app's configuration.

    Required Parameters:
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - always_on -- ensure web app gets loaded all the time, rather unloaded after been idle. Recommended when you have continuous web jobs running
    - auto_heal_enabled -- enable or disable auto heal
    - ftps_state -- Set the Ftps state value for an app. Default value is 'AllAllowed'.
    - generic_configurations -- Provide site configuration list in a format of either `key=value` pair or `@<json_file>`. PowerShell and Windows Command Prompt users should use a JSON file to provide these configurations to avoid compatibility issues with escape characters.
    - http20_enabled -- configures a web site to allow clients to connect over http2.0.
    - java_container -- The java container, e.g., Tomcat, Jetty
    - java_container_version -- The version of the java container, e.g., '8.0.23' for Tomcat
    - java_version -- The version used to run your web app if using Java, e.g., '1.7' for Java 7, '1.8' for Java 8
    - linux_fx_version -- The runtime stack used for your linux-based webapp, e.g., "RUBY|2.5.5", "NODE|10.14", "PHP|7.2", "DOTNETCORE|2.1". See https://aka.ms/linux-stacks for more info.
    - min_tls_version -- The minimum version of TLS required for SSL requests, e.g., '1.0', '1.1', '1.2'
    - net_framework_version -- The version used to run your web app if using .NET Framework, e.g., 'v4.0' for .NET 4.6 and 'v3.0' for .NET 3.5
    - number_of_workers -- The number of workers to be allocated.
    - php_version -- The version used to run your web app if using PHP, e.g., 5.5, 5.6, 7.0
    - prewarmed_instance_count -- Number of pre-warmed instances a function app has
    - python_version -- The version used to run your web app if using Python, e.g., 2.7, 3.4
    - remote_debugging_enabled -- enable or disable remote debugging
    - slot -- the name of the slot. Default to the productions slot if not specified
    - startup_file -- The startup file for linux hosted web apps, e.g. 'process.json' for Node.js web
    - use_32bit_worker_process -- use 32 bits worker process or not
    - vnet_route_all_enabled -- Configure regional VNet integration to route all traffic to the VNet.
    - web_sockets_enabled -- enable or disable web sockets
    '''
    return _call_az("az functionapp config set", locals())


def show(name, resource_group, slot=None):
    '''
    Get the details of an existing function app's configuration.

    Required Parameters:
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp config show", locals())

