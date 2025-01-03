# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/pulumi/azure/table.py

This script defines the Table class.

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
from .outputs import Outputs
import pulumi
import pulumi_azure_native
from .resource_group import ResourceGroup
from .storage_account import StorageAccount


class Table(AzureResource):
    """
    Azure Table for Licdata.

    Class name: Table

    Responsibilities:
        - Define an Azure Table for Licdata.

    Collaborators:
        - None
    """

    def __init__(
        self,
        stackName: str,
        projectName: str,
        location: str,
        name: str,
        storageAccount: StorageAccount,
        resourceGroup: ResourceGroup,
    ):
        """
        Creates a new Table instance.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The Azure location.
        :type location: str
        :param name: The table name.
        :type name: str
        :param storageAccount: The StorageAccount.
        :type storageAccount: pythoneda.iac.pulumi.azure.StorageAccount
        :param resourceGroup: The ResourceGroup.
        :type resourceGroup: pythoneda.iac.pulumi.azure.ResourceGroup
        """
        self._name = name
        super().__init__(
            stackName,
            projectName,
            location,
            {"storage_account": storageAccount, "resource_group": resourceGroup},
        )

    @property
    def name(self) -> str:
        """
        Returns the table name.
        :return: The table name.
        :rtype: str
        """
        return self._name

    @classmethod
    @property
    def type(cls) -> str:
        """
        Retrieves the type of resource.
        :return: Such type.
        :rtype: str
        """
        return "Microsoft.Storage/storageAccounts/tableServices/tables"

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
        return "t"

    # @override
    def _create(self, name: str) -> pulumi_azure_native.storage.Table:
        """
        Creates a new table.
        :param name: The name of the resource.
        :type name: str
        :return: The table.
        :rtype: pulumi_azure_native.storage.Table
        """
        return pulumi_azure_native.storage.Table(
            name,
            account_name=self.storage_account.name,
            table_name=self.name,
            resource_group_name=self.resource_group.name,
        )

    # @override
    def _post_create(self, resource: pulumi_azure_native.storage.Table):
        """
        Post-create hook.
        :param resource: The resource.
        :type resource: pulumi_azure_native.storage.Table
        """
        pulumi.export(Outputs.TABLE.value, resource.name)
        pulumi.export(Outputs.TABLE_ID.value, resource.id)

    @classmethod
    def from_id(cls, id: str, name: str = None) -> pulumi_azure_native.storage.Table:
        """
        Retrieves a Table instance from an ID.
        :param name: The Pulumi name.
        :type name: str
        :param id: The ID.
        :type id: str
        :return: The Table.
        :rtype: pulumi_azure_native.storage.Table
        """
        return pulumi.Output.all(name, id).apply(
            lambda args: pulumi_azure_native.storage.Table.get(
                resource_name=args[0], opts=pulumi.ResourceOptions(id=args[1])
            )
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
