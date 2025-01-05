# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/pulumi/azure/outputs.py

This script defines the Outputs class.

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
from enum import Enum


class Outputs(Enum):
    """
    Keys used to access Pulumi outputs.

    Class name: Outputs

    Responsibilities:
        - Define the keys used as Pulumi outputs to access resources by type.

    Collaborators:
        - None
    """

    API = "api"
    API_ID = "api_id"
    APP_INSIGHTS = "app_insights"
    APP_INSIGHTS_ID = "app_insights_id"
    API_MANAGEMENT_SERVICE = "api_management_service"
    API_MANAGEMENT_SERVICE_ID = "api_management_service_id"
    API_DOMAIN = "api_domain"
    APP_SERVICE_PLAN = "app_service_plan"
    APP_SERVICE_PLAN_ID = "app_service_plan_id"
    BLOB = "blob"
    BLOB_ID = "blob_id"
    BLOB_CONTAINER = "blob_container"
    BLOB_CONTAINER_ID = "blob_container_id"
    CONTAINER_REGISTRY = "container_registry"
    CONTAINER_REGISTRY_ID = "container_registry_id"
    CONTAINER_REGISTRY_USERNAME = "container_registry_username"
    CONTAINER_REGISTRY_USERNAME_ID = "container_registry_username_id"
    CONTAINER_REGISTRY_PASSWORD = "container_registry_password"
    CONTAINER_REGISTRY_PASSWORD_ID = "container_registry_password_id"
    CONTAINER_REGISTRY_URL = "container_registry_url"
    CONTAINER_REGISTRY_URL_ID = "container_registry_url_id"
    COSMOSDB_ACCOUNT = "cosmosdb_account"
    COSMOSDB_ACCOUNT_ID = "cosmosdb_account_id"
    COSMOSDB_CONTAINER = "cosmosdb_container"
    COSMOSDB_CONTAINER_ID = "cosmosdb_container_id"
    COSMOSDB_DATABASE = "cosmosdb_database"
    COSMOSDB_DATABASE_ID = "cosmosdb_database_id"
    DATABASES_STORAGE_ACCOUNT = "databases_storage_account"
    DATABASES_STORAGE_ACCOUNT_ID = "databases_storage_account_id"
    DNS_RECORD = "dns_record"
    DNS_RECORD_ID = "dns_record_id"
    DNS_ZONE = "dns_zone"
    DNS_ZONE_ID = "dns_zone_id"
    DOCKER_PULL_ROLE_ASSIGNMENT = "docker_pull_role_assignment"
    DOCKER_PULL_ROLE_ASSIGNMENT_ID = "docker_pull_role_assignment_id"
    DOCKER_PULL_ROLE_DEFINITION = "docker_pull_role_definition"
    DOCKER_PULL_ROLE_DEFINITION_ID = "docker_pull_role_definition_id"
    FRONTEND_ENDPOINT = "frontend_endpoint"
    FRONTEND_ENDPOINT_ID = "frontend_endpoint_id"
    FRONT_DOOR = "front_door"
    FRONT_DOOR_ID = "front_door_id"
    FUNCTION_STORAGE_ACCOUNT = "function_storage_account"
    FUNCTION_STORAGE_ACCOUNT_ID = "function_storage_account_id"
    NETWORK_SECURITY_GROUP = "network_security_group"
    NETWORK_SECURITY_GROUP_ID = "network_security_group_id"
    PUBLIC_IP_ADDRESS = "public_ip_address"
    PUBLIC_IP_ADDRESS_ID = "public_ip_address_id"
    PUBLIC_IP_ADDRESS_VALUE = "public_ip_address_value"
    RESOURCE_GROUP = "resource_group"
    RESOURCE_GROUP_ID = "resource_group_id"
    TABLE = "table"
    TABLE_ID = "table_id"
    WEB_APP = "web_app"
    WEB_APP_ID = "web_app_id"
    LINUX_FX_VERSION = "linux_fx_version"
    IMAGE_URL = "image_url"
    WEB_APP_DEPLOYMENT_SLOT = "webapp_deployment_slot"
    WEB_APP_DEPLOYMENT_SLOT_ID = "webapp_deployment_slot_id"
    HOST_NAME_BINDING = "host_name_binding"
    HOST_NAME_BINDING_ID = "host_name_binding_id"


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
