from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.sql import SqlManagementClient
from azure.mgmt.sql.models import Server, Database

# Define your Azure subscription details
subscription_id = 'ac08911f-e216-4330-b939-e27b0d83126f'
resource_group_name = 'rg-eastus'
location = 'eastus'
sql_server_name = 'SqlSrvr-eastus'
sql_database_name = 'Sqldb-eastus'

# Authenticate using DefaultAzureCredential (Make sure to login via Azure CLI: `az login`)
credential = DefaultAzureCredential()

# Resource Management Client for managing resources
resource_client = ResourceManagementClient(credential, subscription_id)

# Create Resource Group
resource_client.resource_groups.create_or_update(resource_group_name, {"location": location})

# SQL Management Client for managing SQL resources
sql_client = SqlManagementClient(credential, subscription_id)

# Create SQL Server
server_parameters = Server(
    location=location,
    administrator_login='SqlAdmin',
    administrator_login_password='adminPass123'
)

sql_client.servers.begin_create_or_update(resource_group_name, sql_server_name, server_parameters).result()

# Create SQL Database
db_parameters = Database(location=location)
sql_client.databases.begin_create_or_update(resource_group_name, sql_server_name, sql_database_name, db_parameters).result()

print(f"SQL Database '{sql_database_name}' created in server '{sql_server_name}'")
