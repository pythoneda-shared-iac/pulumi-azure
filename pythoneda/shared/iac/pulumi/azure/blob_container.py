# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/pulumi/azure/blob_container.py

This script defines the BlobContainer class.

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
from typing import Any


class BlobContainer(AzureResource):
    """
    A blob container in Azure.

    Class name: BlobContainer

    Responsibilities:
        - Declares an Azure blob container.

    Collaborators:
        - None
    """

    def __init__(
        self,
        stackName: str,
        projectName: str,
        location: str,
        publicAccess: str,
        storageAccount: StorageAccount,
        resourceGroup: ResourceGroup,
    ):
        """
        Creates a new Blob Container instance.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The Azure location.
        :type location: str
        :param publicAccess: The public access type.
        :type publicAccess
        :param storageAccount: The storage account.
        :type storageAccount: pulumi_azure_native.storage.StorageAccount
        :param resourceGroup: The ResourceGroup.
        :type resourceGroup: pulumi_azure_native.resources.ResourceGroup
        """
        self._public_access = publicAccess
        super().__init__(
            stackName,
            projectName,
            location,
            {"storage_account": storageAccount, "resource_group": resourceGroup},
        )

    @property
    def public_access(self) -> str:
        """
        Retrieves the public access value.
        :return: Such information.
        :rtype: str
        """
        return self._public_access if self._public_access is not None else "Blob"

    @classmethod
    @property
    def type(cls) -> str:
        """
        Retrieves the type of resource.
        :return: Such type.
        :rtype: str
        """
        return "Microsoft.Storage/storageAccounts/blobServices/containers"

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
        return "bc"

    # @override
    def _create(self, name: str) -> Any:
        """
        Creates a new Blob Container instance.
        :param name: The name of the resource.
        :type name: str
        :return: The blob container.
        :rtype: pulumi_azure_native.storage.BlobContainer
        """
        return pulumi_azure_native.storage.BlobContainer(
            name,
            account_name=self.storage_account.name,
            resource_group_name=self.resource_group.name,
            public_access=self.public_access,
        )

    # @override
    def _post_create(self, resource: pulumi_azure_native.storage.BlobContainer):
        """
        Post-create hook.
        :param resource: The resource.
        :type resource: pulumi_azure_native.storage.BlobContainer
        """
        pulumi.export(Outputs.BLOB_CONTAINER.value, resource.name)
        pulumi.export(Outputs.BLOB_CONTAINER_ID.value, resource.id)

    @classmethod
    def from_id(
        cls, id: str, name: str = None
    ) -> pulumi_azure_native.storage.BlobContainer:
        """
        Retrieves a BlobContainer instance from an ID.
        :param name: The Pulumi name.
        :type name: str
        :param id: The ID.
        :type id: str
        :return: The BlobContainer.
        :rtype: pulumi_azure_native.storage.BlobContainer
        """
        return pulumi.Output.all(name, id).apply(
            lambda args: pulumi_azure_native.storage.BlobContainer.get(
                resource_name=args[0], opts=pulumi.ResourceOptions(id=args[1])
            )
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
