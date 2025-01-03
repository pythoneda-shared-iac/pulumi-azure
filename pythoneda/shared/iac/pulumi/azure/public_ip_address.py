# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/pulumi/azure/public_ip_address.py

This script defines the PublicIpAddress class.

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


class PublicIpAddress(AzureResource):
    """
    Azure PublicIpAddress for Licdata.

    Class name: PublicIpAddress

    Responsibilities:
        - Define the Azure PublicIpAddress for Licdata.

    Collaborators:
        - None
    """

    def __init__(
        self,
        stackName: str,
        projectName: str,
        location: str,
        publicIpAllocationMethod: str,
        ipAddressType: str,
        resourceGroup: ResourceGroup,
    ):
        """
        Creates a new PublicIpAddress instance.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The Azure location.
        :type location: str
        :param publicIpAllocationMethod: The public IP allocation method.
        :type publicIpAllocationMethod: str
        :param ipAddressType: The IP address type.
        :type ipAddressType: str
        :param resourceGroup: The ResourceGroup.
        :type resourceGroup: pulumi_azure_native.resources.ResourceGroup
        """
        self._public_ip_allocation_method = publicIpAllocationMethod
        self._ip_address_type = ipAddressType
        super().__init__(
            stackName, projectName, location, {"resource_group": resourceGroup}
        )

    @property
    def public_ip_allocation_method(self) -> str:
        """
        Gets the public IP allocation method.
        :return: The public IP allocation method.
        :rtype: str
        """
        return (
            self._public_ip_allocation_method
            if self._public_ip_allocation_method is not None
            else "Static"
        )

    @property
    def ip_address_type(self) -> str:
        """
        Gets the IP address type.
        :return: The IP address type.
        :rtype: str
        """
        return (
            self._ip_address_type if self._ip_address_type is not None else "Standard"
        )

    @classmethod
    @property
    def type(cls) -> str:
        """
        Retrieves the type of resource.
        :return: Such type.
        :rtype: str
        """
        return "Microsoft.Network/publicIPAddresses"

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
        return "pipa"

    # @override
    def _create(self, name: str) -> pulumi_azure_native.network.PublicIPAddress:
        """
        Creates a public IP address.
        :param name: The name of the public IP address.
        :type name: str
        :return: The public IP address.
        :rtype: pulumi_azure_native.network.PublicIPAddress
        """
        return pulumi_azure_native.network.PublicIPAddress(
            name,
            resource_group_name=self.resource_group.name,
            public_ip_allocation_method=self.public_ip_allocation_method,
            sku=pulumi_azure_native.network.PublicIPAddressSkuArgs(
                name=self.ip_address_type
            ),
        )

    # @override
    def _post_create(self, resource: pulumi_azure_native.network.PublicIPAddress):
        """
        Post-create hook.
        :param resource: The resource.
        :type resource: pulumi_azure_native.network.PublicIPAddress
        """
        pulumi.export(Outputs.PUBLIC_IP_ADDRESS.value, resource.name)
        pulumi.export(Outputs.PUBLIC_IP_ADDRESS_ID.value, resource.id)
        pulumi.export(Outputs.PUBLIC_IP_ADDRESS_VALUE, resource.ip_address)

    @classmethod
    def from_id(
        cls, id: str, name: str = None
    ) -> pulumi_azure_native.network.PublicIPAddress:
        """
        Retrieves a PublicIPAddress instance from an ID.
        :param name: The Pulumi name.
        :type name: str
        :param id: The ID.
        :type id: str
        :return: The PublicIPAddress.
        :rtype: pulumi_azure_native.network.PublicIPAddress
        """
        return pulumi.Output.all(name, id).apply(
            lambda args: pulumi_azure_native.network.PublicIPAddress.get(
                resource_name=args[0], opts=pulumi.ResourceOptions(id=args[1])
            )
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
