# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/pulumi/azure/docker_pull_role_definition.py

This script defines the DockerPullRoleDefinition class.

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
from .container_registry import ContainerRegistry
from .outputs import Outputs
import pulumi
import pulumi_azure_native
from .resource_group import ResourceGroup
from .role_definition import RoleDefinition


class DockerPullRoleDefinition(RoleDefinition):
    """
    Azure Role Definition for Licdata's Functions.

    Class name: DockerPullRoleDefinition

    Responsibilities:
        - Define the Azure Role so Licdata's Functions can perform docker pulls.

    Collaborators:
        - None
    """

    def __init__(
        self,
        stackName: str,
        projectName: str,
        location: str,
        containerRegistry: ContainerRegistry,
        resourceGroup: ResourceGroup,
    ):
        """
        Creates a new DockerPullRoleDefinition instance.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The Azure location.
        :type location: str
        :param containerRegistry: The container registry.
        :type containerRegistry: pythoneda.iac.pulumi.azure.ContainerRegistry
        :param resourceGroup: The ResourceGroup.
        :type resourceGroup: pythoneda.iac.pulumi.azure.ResourceGroup
        """
        super().__init__(
            stackName,
            projectName,
            location,
            "ACR Pull Custom Role",
            "Custom role to allow managed identity to pull images from ACR",
            resourceGroup.id,
            [resourceGroup.id],
            [
                {
                    "actions": ["Microsoft.ContainerRegistry/registries/pull/read"],
                    "notActions": [],
                }
            ],
            {"resource_group": resourceGroup},
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
        return "rddp"

    # @override
    def _post_create(self, resource: pulumi_azure_native.authorization.RoleDefinition):
        """
        Post-create hook.
        :param resource: The resource.
        :type resource: pulumi_azure_native.authorization.RoleDefinition
        """
        pulumi.export(Outputs.DOCKER_PULL_ROLE_DEFINITION.value, resource.name)
        pulumi.export(Outputs.DOCKER_PULL_ROLE_DEFINITION_ID.value, resource.id)

    @classmethod
    def from_id(
        cls, id: str, name: str = None
    ) -> pulumi_azure_native.authorization.RoleDefinition:
        """
        Retrieves an RoleDefinition instance from an ID.
        :param name: The Pulumi name.
        :type name: str
        :param id: The ID.
        :type id: str
        :return: The RoleDefinition.
        :rtype: pulumi_azure_native.authorization.RoleDefinition
        """
        return pulumi.Output.all(name, id).apply(
            lambda args: pulumi_azure_native.authorization.RoleDefinition.get(
                resource_name=args[0], opts=pulumi.ResourceOptions(id=args[1])
            )
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
