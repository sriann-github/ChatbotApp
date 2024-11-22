from azure.identity import DefaultAzureCredential
from azure.mgmt.cosmosdb import CosmosDBManagementClient

# Define your Azure subscription details and Cosmos DB account details
subscription_id = 'your-subscription-id'
resource_group = 'your-resource-group'
cosmosdb_account_name = 'your-cosmosdb-account-name'

# Authenticate with Azure
credential = DefaultAzureCredential()

# Initialize the Cosmos DB Management client
cosmos_client = CosmosDBManagementClient(credential, subscription_id)

try:
    # Delete the Cosmos DB account
    delete_operation = cosmos_client.database_accounts.begin_delete(
        resource_group_name=resource_group,
        account_name=cosmosdb_account_name
    )
    
    # Wait for the delete operation to complete
    delete_operation.wait()

    print(f"Cosmos DB account '{cosmosdb_account_name}' deleted successfully.")
    
except Exception as e:
    print(f"Error deleting Cosmos DB account: {e}")
