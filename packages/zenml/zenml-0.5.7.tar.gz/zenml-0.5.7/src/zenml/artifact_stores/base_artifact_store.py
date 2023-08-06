#  Copyright (c) ZenML GmbH 2021. All Rights Reserved.
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
"""Definition of an Artifact Store"""

import os
from pathlib import Path
from typing import Any, Optional

from zenml.config.global_config import GlobalConfig
from zenml.core.base_component import BaseComponent
from zenml.io import fileio
from zenml.io.utils import get_zenml_config_dir


class BaseArtifactStore(BaseComponent):
    """Base class for all ZenML Artifact Store.

    Every ZenML Artifact Store should override this class.
    """

    path: str
    _ARTIFACT_STORE_DIR_NAME: str = "artifact_stores"

    def __init__(self, repo_path: str, **kwargs: Any) -> None:
        """Initializes a BaseArtifactStore instance.

        Args:
            repo_path: Path to the repository of this artifact store.
        """
        serialization_dir = os.path.join(
            get_zenml_config_dir(repo_path),
            self._ARTIFACT_STORE_DIR_NAME,
        )
        super().__init__(serialization_dir=serialization_dir, **kwargs)

    @staticmethod
    def get_component_name_from_uri(artifact_uri: str) -> str:
        """Gets component name from artifact URI.

        Args:
          artifact_uri: URI to artifact.

        Returns:
            Name of the component.
        """
        return fileio.get_parent(artifact_uri)

    def resolve_uri_locally(
        self, artifact_uri: str, path: Optional[str] = None
    ) -> str:
        """Takes a URI that points within the artifact store, downloads the
        URI locally, then returns local URI.

        Args:
          artifact_uri: uri to artifact.
          path: optional path to download to. If None, is inferred.

        Returns:
            Locally resolved uri.
        """
        if not fileio.is_remote(artifact_uri):
            # It's already local
            return artifact_uri

        if path is None:
            # Create a unique path in local machine
            path = os.path.join(
                GlobalConfig().get_serialization_dir(),
                str(self.uuid),
                BaseArtifactStore.get_component_name_from_uri(artifact_uri),
                Path(artifact_uri).stem,  # unique ID from MLMD
            )

        # Create if not exists and download
        fileio.create_dir_recursive_if_not_exists(path)
        fileio.copy_dir(artifact_uri, path, overwrite=True)

        return path

    class Config:
        """Configuration of settings."""

        env_prefix = "zenml_artifact_store_"
