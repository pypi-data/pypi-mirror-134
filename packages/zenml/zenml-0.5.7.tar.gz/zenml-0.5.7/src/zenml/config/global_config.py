#  Copyright (c) ZenML GmbH 2020. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
"""Global config for the ZenML installation."""
from typing import Any
from uuid import UUID, uuid4

from pydantic import Field

from zenml.config.constants import GLOBAL_CONFIG_NAME
from zenml.core.base_component import BaseComponent
from zenml.io import fileio
from zenml.io.utils import get_global_config_directory
from zenml.logger import get_logger

logger = get_logger(__name__)


class GlobalConfig(BaseComponent):
    """Class definition for the global config.

    Defines global data such as unique user ID and whether they opted in
    for analytics.
    """

    user_id: UUID = Field(default_factory=uuid4)
    analytics_opt_in: bool = True

    def __init__(self, **data: Any):
        """We persist the attributes in the config file. For the global
        config, we want to persist the data as soon as it is initialized for
        the first time."""
        super().__init__(
            serialization_dir=get_global_config_directory(), **data
        )

        # At this point, if the serialization file does not exist we should
        #  create it and dump our data.
        f = self.get_serialization_full_path()
        if not fileio.file_exists(str(f)):
            self._dump()

    def get_serialization_file_name(self) -> str:
        """Gets the global config dir for installed package."""
        return GLOBAL_CONFIG_NAME
