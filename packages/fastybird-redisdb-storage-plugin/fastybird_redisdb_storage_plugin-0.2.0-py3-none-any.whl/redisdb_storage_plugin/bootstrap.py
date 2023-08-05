#!/usr/bin/python3

#     Copyright 2021. FastyBird s.r.o.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

"""
Redis DB storage plugin DI container
"""

# Library dependencies
from kink import di

# Library libs
from redisdb_storage_plugin.manager import StorageManagerFactory
from redisdb_storage_plugin.repository import StorageRepositoryFactory


def create_container() -> None:
    """Create Redis DB storage plugin services"""
    di[StorageRepositoryFactory] = StorageRepositoryFactory()
    di["fb-redisdb-storage-plugin_repository-factory"] = di[StorageRepositoryFactory]

    di[StorageManagerFactory] = StorageManagerFactory()
    di["fb-redisdb-storage-plugin_manager-factory"] = di[StorageManagerFactory]
