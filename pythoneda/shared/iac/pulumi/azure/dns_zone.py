# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/pulumi/azure/dns_zone.py

This script defines the DnsZone class.

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
import pulumi_azure_native


class DnsZone(AzureResource):
    """
    Azure DnsZone for Licdata.

    Class name: DnsZone

    Responsibilities:
        - Define the Azure DnsZone for Licdata.

    Collaborators:
        - None
    """

    def __init__(
        self,
        stackName: str,
        projectName: str,
        location: str,
        zoneType: str,
        domainName: str,
        resourceGroup: ResourceGroup,
    ):
        """
        Creates a new DnsZone instance.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The Azure location.
        :type location: str
        :param zoneType: The type of the zone.
        :type zoneType: str
        :param domainName: The domain name.
        :type domainName: str
        :param resourceGroup: The ResourceGroup.
        :type resourceGroup: pythoneda.iac.pulumi.azure.ResourceGroup
        """
        super().__init__(
            stackName, projectName, location, {"resource_group": resourceGroup}
        )
        self._zone_type = zoneType
        self._domain_name = domainName

    @property
    def zone_type(self) -> str:
        """
        Gets the zone type.
        :return: The zone type.
        :rtype: str
        """
        return self._zone_type if self._zone_type is not None else "Public"

    @property
    def domain_name(self) -> str:
        """
        Gets the domain name.
        :return: The domain name.
        :rtype: str
        """
        return self._domain_name

    @classmethod
    @property
    def type(cls) -> str:
        """
        Retrieves the type of resource.
        :return: Such type.
        :rtype: str
        """
        return "Microsoft.Network/dnsZones"

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
        return "dnsz"

    # @override
    def _create(self, name: str) -> pulumi_azure_native.network.Zone:
        """
        Creates a network zone.
        :param name: The name of the DNS zone.
        :type name: str
        :return: The DNS zone.
        :rtype: pulumi_azure_native.network.Zone
        """
        return pulumi_azure_native.network.Zone(
            name,
            resource_group_name=self.resource_group.name,
            zone_type=self.zone_type,
            zone_name=self.domain_name,
            location="global",
        )

    # @override
    def _post_create(self, resource: pulumi_azure_native.network.Zone):
        """
        Post-create hook.
        :param resource: The resource.
        :type resource: pulumi_azure_native.network.Zone
        """
        pulumi.export("dns_zone", resource.name)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
