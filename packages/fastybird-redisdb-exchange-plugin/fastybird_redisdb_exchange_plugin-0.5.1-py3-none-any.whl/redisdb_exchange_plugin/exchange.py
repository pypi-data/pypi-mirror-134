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
Redis DB exchange plugin exchange service
"""

# Python base dependencies
import json
import time
from abc import ABC
from threading import Thread
from typing import Dict, Optional, Union

# Library dependencies
import metadata.exceptions as metadata_exceptions
from kink import inject
from metadata.loader import load_schema_by_routing_key
from metadata.routing import RoutingKey
from metadata.types import ModuleOrigin
from metadata.validator import validate

# Library libs
from redisdb_exchange_plugin.connection import RedisClient
from redisdb_exchange_plugin.exceptions import HandleDataException
from redisdb_exchange_plugin.logger import Logger


class IConsumer(ABC):  # pylint: disable=too-few-public-methods
    """
    Redis exchange consumer interface

    @package        FastyBird:RedisDbExchangePlugin!
    @module         consumer

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """

    def consume(
        self,
        origin: ModuleOrigin,
        routing_key: RoutingKey,
        data: Optional[Dict[str, Union[str, int, float, bool, None]]],
    ) -> None:
        """Consume data received from exchange bus"""


@inject
class RedisExchange(Thread):
    """
    Redis data exchange

    @package        FastyBird:RedisDbExchangePlugin!
    @module         redis

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """

    __redis_client: RedisClient

    __consumer: Optional[IConsumer]

    __logger: Logger

    __stopped: bool = False

    # -----------------------------------------------------------------------------

    def __init__(
        self,
        redis_client: RedisClient,
        logger: Logger,
        consumer: IConsumer = None,  # type: ignore[assignment]
    ) -> None:
        super().__init__(name="Redis DB exchange client thread", daemon=True)

        self.__redis_client = redis_client
        self.__logger = logger

        self.__consumer = consumer

    # -----------------------------------------------------------------------------

    def start(self) -> None:
        """Start exchange services"""
        self.__stopped = False
        self.__redis_client.subscribe()

        self.__logger.info("Starting Redis DB exchange client")

        super().start()

    # -----------------------------------------------------------------------------

    def stop(self) -> None:
        """Close all opened connections & stop exchange thread"""
        self.__stopped = True

        self.__logger.info("Closing Redis DB exchange client")

    # -----------------------------------------------------------------------------

    def run(self) -> None:
        """Process Redis exchange messages"""
        self.__stopped = False

        while not self.__stopped:
            try:
                data = self.__redis_client.receive()

                if data is not None:
                    self.__receive(data)

                time.sleep(0.001)

            except OSError:
                self.__stopped = True

        # Unsubscribe from exchange
        self.__redis_client.unsubscribe()
        # Disconnect from server
        self.__redis_client.close()

        self.__logger.info("Redis DB exchange client was closed")

    # -----------------------------------------------------------------------------

    def is_healthy(self) -> bool:
        """Check if exchange is healthy"""
        return self.is_alive()

    # -----------------------------------------------------------------------------

    def register_consumer(
        self,
        consumer: IConsumer,
    ) -> None:
        """Register new consumer to server"""
        self.__consumer = consumer

    # -----------------------------------------------------------------------------

    def __receive(self, data: Dict) -> None:
        try:
            origin = self.__validate_origin(origin=data.get("origin", None))
            routing_key = self.__validate_routing_key(
                routing_key=data.get("routing_key", None),
            )

            if (
                routing_key is not None
                and origin is not None
                and data.get("data", None) is not None
                and isinstance(data.get("data", None), dict) is True
            ):
                data = self.__validate_data(
                    origin=origin,
                    routing_key=routing_key,
                    data=data.get("data", None),
                )

                if self.__consumer is not None:
                    self.__consumer.consume(
                        origin=origin,
                        routing_key=routing_key,
                        data=data,
                    )

            else:
                self.__logger.warning("Received exchange message is not valid")

        except HandleDataException as ex:
            self.__logger.exception(ex)

    # -----------------------------------------------------------------------------

    @staticmethod
    def __validate_origin(origin: Optional[str]) -> Optional[ModuleOrigin]:
        if origin is not None and isinstance(origin, str) is True and ModuleOrigin.has_value(origin):
            return ModuleOrigin(origin)

        return None

    # -----------------------------------------------------------------------------

    @staticmethod
    def __validate_routing_key(routing_key: Optional[str]) -> Optional[RoutingKey]:
        if routing_key is not None and isinstance(routing_key, str) is True and RoutingKey.has_value(routing_key):
            return RoutingKey(routing_key)

        return None

    # -----------------------------------------------------------------------------

    def __validate_data(self, origin: ModuleOrigin, routing_key: RoutingKey, data: Dict) -> Dict:
        """Validate received exchange message against defined schema"""
        try:
            schema: str = load_schema_by_routing_key(routing_key)

        except metadata_exceptions.FileNotFoundException as ex:
            self.__logger.error(
                "Schema file for origin: %s and routing key: %s could not be loaded",
                origin.value,
                routing_key.value,
            )

            raise HandleDataException("Provided data could not be validated") from ex

        except metadata_exceptions.InvalidArgumentException as ex:
            self.__logger.error(
                "Schema file for origin: %s and routing key: %s is not configured in mapping",
                origin.value,
                routing_key.value,
            )

            raise HandleDataException("Provided data could not be validated") from ex

        try:
            return validate(json.dumps(data), schema)

        except metadata_exceptions.MalformedInputException as ex:
            raise HandleDataException("Provided data are not in valid json format") from ex

        except metadata_exceptions.LogicException as ex:
            self.__logger.error(
                "Schema file for origin: %s and routing key: %s could not be parsed & compiled",
                origin.value,
                routing_key.value,
            )

            raise HandleDataException("Provided data could not be validated") from ex

        except metadata_exceptions.InvalidDataException as ex:
            raise HandleDataException("Provided data are not valid") from ex
