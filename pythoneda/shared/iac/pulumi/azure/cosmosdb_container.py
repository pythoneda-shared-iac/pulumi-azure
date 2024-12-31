# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/pulumi/azure/cosmosdb_container.py

This script defines the Azure CosmosDB Container for Licdata.

Copyright (C) 2024-today pythoneda-shared-iac/pulumi-azure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from .azure_resource import AzureResource
from .cosmosdb_account import CosmosdbAccount
from .cosmosdb_database import CosmosdbDatabase
from .resource_group import ResourceGroup
import pulumi
import pulumi_azure_native
from typing import Dict


class CosmosdbContainer(AzureResource):
    """
    Azure CosmosDB Container for Licdata.

    Class name: CosmosdbContainer

    Responsibilities:
        - Define the Azure CosmosDB Container for Licdata.

    Collaborators:
        - None
    """

    def __init__(
        self,
        stackName: str,
        projectName: str,
        location: str,
        partitionKey: Dict[str, str],
        resourceGroup: ResourceGroup,
        cosmosdbAccount: CosmosdbAccount,
        cosmosdbDatabase: CosmosdbDatabase,
    ):
        """
        Creates a new Azure instance.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The Azure location.
        :type location: str
        :param resourceGroup: The ResourceGroup.
        :type resourceGroup: pulumi_azure_native.resources.ResourceGroup
        :param cosmosdbAccount: The CosmosDB account.
        :type cosmosdbAccount: pythoneda.iac.pulumi.azure.CosmosdbAccount
        :param cosmosdbDatabase: The CosmosDB database.
        :param cosmosdbDatabase: pythoneda.iac.pulumi.azure.CosmosdbDatabase
        """
        super().__init__(
            stackName,
            projectName,
            location,
            {
                "cosmosdb_account": cosmosdbAccount,
                "cosmosdb_database": cosmosdb_database,
                "resource_group": resourceGroup,
            },
        )
        self._partition_key = partitionKey

    @property
    def partition_key(self) -> Dict[str, str]:
        """
        Retrieves the partition key.
        :return: Such partition key.
        :rtype: Dict[str, str]
        """
        return (
            (
                self._partition_key
                if self._partition_key is not None
                else {
                    "paths": ["/id"],
                    "kind": "Hash",
                }
            ),
        )

    # @override
    @classmethod
    def _resource_name(cls, stackName: str, projectName: str, location: str) -> str:
        """
        Builds the resource name.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The Azure location.
        :type location: str
        :return: The resource name.
        :rtype: str
        """
        return "cdbc"

    # @override
    def _create(
        self, name: str
    ) -> pulumi_azure_native.documentdb.SqlResourceSqlContainer:
        """
        Creates an Azure Cosmos DB Container.
        :param name: The name of the resource.
        :type name: str
        :return: The Azure Cosmos DB Container.
        :rtype: pulumi_azure_native.documentdb.SqlResourceSqlContainer
        """
        return pulumi_azure_native.documentdb.SqlResourceSqlContainer(
            name,
            resource_group_name=self.resource_group.name,
            account_name=self.cosmosdb_account.name,
            container_name=name,
            database_name=self.cosmosdb_database.name,
            location=self.location,
            resource=pulumi_azure_native.documentdb.SqlContainerResourceArgs(
                id=self.cosmosdb_database.name, partition_key=partitionKey
            ),
        )

    # @override
    def _post_create(
        self, resource: pulumi_azure_native.documentdb.SqlResourceSqlContainer
    ):
        """
        Post-create hook.
        :param resource: The resource.
        :type resource: pulumi_azure_native.documentdb.SqlResourceSqlContainer
        """
        pulumi.export("cosmosdb_container", resource.name)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
