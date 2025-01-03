# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/pulumi/azure/app_service_plan.py

This script defines the AppServicePlan class.

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


class AppServicePlan(AzureResource):
    """
    Azure App Service Plan for Licdata.

    Class name: AppServicePlan

    Responsibilities:
        - Define the Azure App Service Plan for Licdata.

    Collaborators:
        - None
    """

    def __init__(
        self,
        stackName: str,
        projectName: str,
        location: str,
        kind: str,
        tierType: str,
        tierName: str,
        capacity: int,
        targetWorkerCount: int,
        resourceGroup: ResourceGroup,
    ):
        """
        Creates a new AppServicePlan instance.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The Azure location.
        :type location: str
        :param kind: The type of app service plan.
        :type kind: str
        :param tierType: The tier type.
        :type tierType: str
        :param tierName: The name of the tier.
        :type tierName: str
        :param capacity: The capacity.
        :type capacity: int
        :param targetWorkerCount: The number of workers.
        :type targetWorkerCount: int
        :param resourceGroup: The ResourceGroup.
        :type resourceGroup: pythoneda.iac.pulumi.azure.ResourceGroup
        """
        self._kind = kind
        self._tier_type = tierType
        self._tier_name = tierName
        self._capacity = capacity
        self._target_worker_count = targetWorkerCount
        super().__init__(
            stackName, projectName, location, {"resource_group": resourceGroup}
        )

    @property
    def kind(self) -> str:
        """
        Retrieves the kind of app service plan.
        :return: Such kind.
        :rtype: str
        """
        return self._kind if self._kind is not None else "FunctionApp"

    @property
    def tier_type(self) -> str:
        """
        Retrieves the tier type.
        :return: Such type.
        :rtype: str
        """
        return self._tier_type if self._tier_name is not None else "Dynamic"

    @property
    def tier_name(self) -> str:
        """
        Retrieves the tier name.
        :return: Such name.
        :rtype: str
        """
        return self._tier_name if self._tier_name is not None else "B1"

    @property
    def capacity(self) -> int:
        """
        Retrieves the capacity.
        :return: Such value.
        :rtype: int
        """
        return self._capacity if self._capacity is not None else 1

    @property
    def target_worker_count(self) -> int:
        """
        Retrieves the target worker count.
        :return: Such count.
        :rtype: int
        """
        return self._target_worker_count if self._target_worker_count is not None else 1

    @classmethod
    @property
    def type(cls) -> str:
        """
        Retrieves the type of resource.
        :return: Such type.
        :rtype: str
        """
        return "Microsoft.Web/serverfarms"

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
        return "appsp"

    # @override
    def _create(self, name: str) -> pulumi_azure_native.web.AppServicePlan:
        """
        Creates the resource.
        :param name: The name of the resource.
        :type name: str
        :return: The Azure App Service Plan.
        :rtype: pulumi_azure_native.web.AppServicePlan
        """
        return pulumi_azure_native.web.AppServicePlan(
            name,
            resource_group_name=self.resource_group.name,
            kind=self.kind,
            sku=pulumi_azure_native.web.SkuDescriptionArgs(
                tier=self.tier_type, name=self.tier_name, capacity=self.capacity
            ),
            location=self.location,
            reserved=True,
            target_worker_count=self.target_worker_count,
        )

    # @override
    def _post_create(self, resource: pulumi_azure_native.web.AppServicePlan):
        """
        Post-create hook.
        :param resource: The resource.
        :type resource: pulumi_azure_native.web.AppServicePlan
        """
        pulumi.export(Outputs.APP_SERVICE_PLAN.value, resource.name)
        pulumi.export(Outputs.APP_SERVICE_PLAN_ID.value, resource.id)

    @classmethod
    def from_id(
        cls, id: str, name: str = None
    ) -> pulumi_azure_native.web.AppServicePlan:
        """
        Retrieves an AppServicePlan instance from an ID.
        :param name: The Pulumi name.
        :type name: str
        :param id: The ID.
        :type id: str
        :return: The AppServicePlan.
        :rtype: pulumi_azure_native.web.AppServicePlan
        """
        return pulumi.Output.all(name, id).apply(
            lambda args: pulumi_azure_native.web.AppServicePlan.get(
                resource_name=args[0], opts=pulumi.ResourceOptions(id=args[1])
            )
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
