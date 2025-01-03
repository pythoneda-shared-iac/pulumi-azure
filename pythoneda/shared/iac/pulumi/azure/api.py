# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/azure/api.py

This script defines the Api class.

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
from .api_management_service import ApiManagementService
from .outputs import Outputs
import pulumi
import pulumi_azure_native
from .resource_group import ResourceGroup
from typing import List


class Api(AzureResource):
    """
    Azure Api.

    Class name: Api

    Responsibilities:
        - Define the Azure Api.

    Collaborators:
        - None
    """

    def __init__(
        self,
        stackName: str,
        projectName: str,
        location: str,
        path: str,
        protocols: List[str],
        apiManagementService: ApiManagementService,
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
        :param path: The path.
        :type path: str
        :param protocols: The protocols.
        :type protocols: List[str]
        :param apiManagementService: The ApiManagementService.
        :type apiManagementService: pythoneda.iac.pulumi.azure.ApiManagementService
        :param resourceGroup: The ResourceGroup.
        :type resourceGroup: pythoneda.iac.pulumi.azure.ResourceGroup
        """
        self._path = path
        self._protocols = protocols
        super().__init__(
            stackName,
            projectName,
            location,
            {
                "api_management_service": apiManagementService,
                "resource_group": resourceGroup,
            },
        )

    @property
    def path(self) -> str:
        """
        Retrieves the path.
        :return: The path.
        :rtype: str
        """
        return self._path

    @property
    def protocols(self) -> List[str]:
        """
        Retrieves the protocols.
        :return: The protocols.
        :rtype: List[str]
        """
        return self._protocols if self._protocols is not None else ["https"]

    @classmethod
    @property
    def type(cls) -> str:
        """
        Retrieves the type of resource.
        :return: Such type.
        :rtype: str
        """
        return "Microsoft.ApiManagement/service/apis"

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
        return "api"

    # @override
    def _create(self, name: str) -> pulumi_azure_native.apimanagement.Api:
        """
        Creates an API.
        :param name: The name of the API.
        :type name: str
        :return: The API.
        :rtype: pulumi_azure_native.apimanagement.Api
        """
        return pulumi_azure_native.apimanagement.Api(
            name,
            resource_group_name=self.resource_group.name,
            service_name=api_management_service.name,
            path=self.path,
            protocols=self.protocols,
            display_name=f"{stackName}-{projectName}-{location} API",
        )

    # @override
    def _post_create(self, resource: pulumi_azure_native.apimanagement.Api):
        """
        Post-create hook.
        :param resource: The resource.
        :type resource: pulumi_azure_native.apimanagement.Api
        """
        pulumi.export(Outputs.API.value, resource.name)
        pulumi.export(Outputs.API_ID.value, resource.id)

    @classmethod
    def from_id(
        cls, id: str, name: str = None
    ) -> pulumi_azure_native.apimanagement.Api:
        """
        Retrieves an Api instance from an ID.
        :param name: The Pulumi name.
        :type name: str
        :param id: The ID.
        :type id: str
        :return: The Api.
        :rtype: pulumi_azure_native.apimanagement.Api
        """
        return pulumi.Output.all(name, id).apply(
            lambda args: pulumi_azure_native.apimanagement.Api.get(
                resource_name=args[0], opts=pulumi.ResourceOptions(id=args[1])
            )
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
