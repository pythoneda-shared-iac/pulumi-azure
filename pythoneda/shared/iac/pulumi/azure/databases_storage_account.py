# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/pulumi/azure/databases_storage_account.py

This script defines the DatabasesStorageAccount class.

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
from .outputs import Outputs
import pulumi
import pulumi_azure_native
from .resource_group import ResourceGroup
from .storage_account import StorageAccount


class DatabasesStorageAccount(StorageAccount):
    """
    Azure Databases Storage Account for Licdata.

    Class name: DatabasesStorageAccount

    Responsibilities:
        - Define the Azure Databases Storage Account for Licdata.

    Collaborators:
        - None
    """

    def __init__(self, resourceGroup: ResourceGroup):
        """
        Creates a new StorageAccount instance.
        :param resourceGroup: The ResourceGroup.
        :type resourceGroup: pythoneda.iac.pulumi.azure.ResourceGroup
        """
        super().__init__("databases", resourceGroup)

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
        return "sadb"

    # @override
    def _post_create(self, resource: pulumi_azure_native.storage.StorageAccount):
        """
        Post-create hook.
        :param resource: The resource.
        :type resource: pulumi_azure_native.storage.StorageAccount
        """
        pulumi.export(Outputs.DATABASES_STORAGE_ACCOUNT.value, resource.name)
        pulumi.export(Outputs.DATABASES_STORAGE_ACCOUNT_ID.value, resource.id)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
