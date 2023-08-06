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
Redis DB exchange plugin DI container
"""

# pylint: disable=no-value-for-parameter

# Python base dependencies
import logging
from typing import Dict, Union

# Library dependencies
from kink import di

from redisdb_exchange_plugin.client import Client

# Library libs
from redisdb_exchange_plugin.connection import Connection
from redisdb_exchange_plugin.logger import Logger
from redisdb_exchange_plugin.publisher import Publisher


def create_container(
    settings: Dict[str, Union[str, int, None]],
    logger: logging.Logger = logging.getLogger("dummy"),
) -> None:
    """Create Redis DB exchange plugin services"""
    di[Logger] = Logger(logger=logger)
    di["fb-redisdb-exchange-plugin_logger"] = di[Logger]

    di[Connection] = Connection(
        host=str(settings.get("host", "127.0.0.1")) if settings.get("host", None) is not None else "127.0.0.1",
        port=int(str(settings.get("port", 6379))),
        channel_name=str(settings.get("channel_name", "fb_exchange"))
        if settings.get("channel_name", None) is not None
        else "fb_exchange",
        username=str(settings.get("username", None)) if settings.get("username", None) is not None else None,
        password=str(settings.get("password", None)) if settings.get("password", None) is not None else None,
        logger=di[Logger],
    )
    di["fb-redisdb-exchange-plugin_redis-connection"] = di[Connection]

    di[Publisher] = Publisher(
        channel_name=str(settings.get("channel_name", "fb_exchange")),
        connection=di[Connection],
        logger=di[Logger],
    )
    di["fb-redisdb-exchange-plugin_publisher"] = di[Publisher]

    di[Client] = Client(connection=di[Connection], logger=di[Logger])
    di["fb-redisdb-exchange-plugin_client"] = di[Client]
