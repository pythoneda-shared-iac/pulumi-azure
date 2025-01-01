# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/pulumi/azure/container_registry.py

This script defines the ContainerRegistry class.

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
from .resource_group import ResourceGroup
import pulumi
from pulumi import Output
import pulumi_azure_native
from pulumi_azure_native.containerregistry import list_registry_credentials


class ContainerRegistry(AzureResource):
    """
    Azure Container Registry for Licdata.

    Class name: ContainerRegistry

    Responsibilities:
        - Define the Azure Container Registry for Licdata.

    Collaborators:
        - None
    """

    def __init__(
        self,
        stackName: str,
        projectName: str,
        location: str,
        skuType: str,
        adminUserEnabled: bool,
        resourceGroup: ResourceGroup,
    ):
        """
        Creates a new Api instance.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The Azure location.
        :type location: str
        :param skuType: The type of SKU (either "Basic", "Standard" "Premium")
        :type skuType: str
        :param adminUserEnabled: Enable admin user for easier authentication.
        :type adminUserEnabled: bool
        :param resourceGroup: The ResourceGroup.
        :type resourceGroup: pythoneda.iac.pulumi.azure.ResourceGroup
        """
        super().__init__(
            stackName, projectName, location, {"resource_group": resourceGroup}
        )
        self._sku_type = skuType
        self._admin_user_enabled = adminUserEnabled

    @property
    def sku_type(self) -> str:
        """
        Retrieves the type of SKU.
        :return: Such value.
        :rtype: str
        """
        return self._sku_type if self._sku_type is not None else "Basic"

    @property
    def admin_user_enabled(self) -> bool:
        """
        Retrieves whether the admin user is enabled.
        :return: Such information.
        :rtype: bool
        """
        return (
            self._admin_user_enabled if self._admin_user_enabled is not None else True
        )

    @classmethod
    @property
    def type(cls) -> str:
        """
        Retrieves the type of resource.
        :return: Such type.
        :rtype: str
        """
        return "Microsoft.ContainerRegistry/registries"

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
        return "cr"

    # @override
    def _create(self, name: str) -> pulumi_azure_native.containerregistry.Registry:
        """
        Creates a container registry.
        :param name: The name of the registry.
        :type name: str
        :param resourceGroup: The Azure Resource Group.
        :type resourceGroup: pulumi_azure_native.resources.ResourceGroup
        :return: The container registry.
        :rtype: pulumi_azure_native.containerregistry.Registry
        """
        return pulumi_azure_native.containerregistry.Registry(
            name,
            resource_group_name=self.resource_group.name,
            registry_name=name,
            sku=pulumi_azure_native.containerregistry.SkuArgs(
                name=self.sku_type,
            ),
            admin_user_enabled=self.admin_user_enabled,
            location=self.location,
        )

    # @override
    def _post_create(self, resource: pulumi_azure_native.containerregistry.Registry):
        """
        Post-create hook.
        :param resource: The resource.
        :type resource: pulumi_azure_native.containerregistry.Registry
        """
        pulumi.export("container_registry", resource.name)
        credentials = Output.all(self.resource_group.name, resource.name).apply(
            lambda args: list_registry_credentials(
                resource_group_name=args[0], registry_name=args[1]
            )
        )
        username = credentials.apply(lambda c: c.username)
        pulumi.export("container_registry_username", username)
        password = credentials.apply(lambda c: c.passwords[0].value)
        pulumi.export("container_registry_password", password)
        url = resource.login_server.apply(lambda name: name)
        pulumi.export("container_registry_url", url)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
