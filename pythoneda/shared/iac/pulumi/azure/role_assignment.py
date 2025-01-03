# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/pulumi/azure/role_assignment.py

This script defines the RoleAssignment class.

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
import abc
from .azure_resource import AzureResource
import pulumi
import pulumi_azure_native
from .resource_group import ResourceGroup
from .role_definition import RoleDefinition


class RoleAssignment(AzureResource, abc.ABC):
    """
    Azure Role Assignment for Licdata's Functions.

    Class name: RoleAssignment

    Responsibilities:
        - Define the Azure Role Assignment for Licdata's Functions.

    Collaborators:
        - None
    """

    def __init__(
        self,
        stackName: str,
        projectName: str,
        location: str,
        roleDefinition: RoleDefinition,
        resourceGroup: ResourceGroup,
    ):
        """
        Creates a new RoleAssignment instance.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The Azure location.
        :type location: str
        :param roleDefinition: The role definition.
        :type roleDefinition: pythoneda.iac.pulumi.azure.RoleDefinition
        :param resourceGroup: The ResourceGroup.
        :type resourceGroup: pythoneda.iac.pulumi.azure.ResourceGroup
        """
        super().__init__(
            stackName,
            projectName,
            location,
            {
                "role_definition": roleDefinition,
                "resource_group": resourceGroup,
            },
        )

    @classmethod
    @property
    def type(cls) -> str:
        """
        Retrieves the type of resource.
        :return: Such type.
        :rtype: str
        """
        return "Microsoft.Authorization/roleAssignments"

    @classmethod
    def from_id(
        cls, id: str, name: str = None
    ) -> pulumi_azure_native.authorization.RoleAssignment:
        """
        Retrieves a RoleAssignment instance from an ID.
        :param name: The Pulumi name.
        :type name: str
        :param id: The ID.
        :type id: str
        :return: The RoleAssignment.
        :rtype: pulumi_azure_native.authorization.RoleAssignment
        """
        return pulumi.Output.all(name, id).apply(
            lambda args: pulumi_azure_native.authorization.RoleAssignment.get(
                resource_name=args[0], opts=pulumi.ResourceOptions(id=args[1])
            )
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
