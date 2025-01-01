# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/pulumi/azure/__init__.py

This file ensures pythoneda.shared.iac.pulumi.azure is a package.

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
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from .azure_resource import AzureResource
from .resource_group import ResourceGroup
from .cosmosdb_account import CosmosdbAccount
from .cosmosdb_database import CosmosdbDatabase
from .cosmosdb_container import CosmosdbContainer
from .storage_account import StorageAccount
from .databases_storage_account import DatabasesStorageAccount
from .table import Table
from .app_service_plan import AppServicePlan
from .web_app import WebApp
from .function_storage_account import FunctionStorageAccount
from .api_management_service import ApiManagementService
from .api import Api
from .public_ip_address import PublicIpAddress
from .dns_zone import DnsZone
from .dns_record import DnsRecord
from .network_security_group import NetworkSecurityGroup
from .blob_container import BlobContainer
from .blob import Blob
from .front_door import FrontDoor
from .frontend_endpoint import FrontendEndpoint
from .web_app_deployment_slot import WebAppDeploymentSlot
from .web_app_host_name_binding import WebAppHostNameBinding
from .app_insights import AppInsights
from .container_registry import ContainerRegistry
from .role_definition import RoleDefinition
from .role_assignment import RoleAssignment
from .docker_pull_role_assignment import DockerPullRoleAssignment
from .docker_pull_role_definition import DockerPullRoleDefinition

# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
