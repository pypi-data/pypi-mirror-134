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
"""Factory to register all components."""
from typing import Callable, Dict, Type

from zenml.artifact_stores import LocalArtifactStore
from zenml.core.base_component import BaseComponent
from zenml.enums import ArtifactStoreTypes, MLMetadataTypes, OrchestratorTypes
from zenml.logger import get_logger
from zenml.metadata_stores import MySQLMetadataStore, SQLiteMetadataStore
from zenml.orchestrators import LocalOrchestrator

logger = get_logger(__name__)
BaseComponentType = Type[BaseComponent]


class ComponentFactory:
    """Definition of ComponentFactory to track all BaseComponent subclasses.

    All BaseComponents (including custom ones) are to be
    registered here.
    """

    def __init__(self, name: str):
        """Constructor for the factory.

        Args:
            name: Unique name for the factory.
        """
        self.name = name
        self.components: Dict[str, BaseComponentType] = {}

    def get_components(self) -> Dict[str, BaseComponentType]:
        """Return all components"""
        return self.components

    def get_single_component(self, key: str) -> BaseComponentType:
        """Get a registered component from a key."""
        if key in self.components:
            return self.components[key]
        raise KeyError(
            f"Type '{key}' does not exist! Available options: "
            f"{[str(k) for k in self.components.keys()]}"
        )

    def get_component_key(self, component: BaseComponentType) -> str:
        """Gets the key of a registered component."""
        for k, v in self.components.items():
            if v == component:
                return k
        raise KeyError(
            f"Type '{component}' does not exist! Available options: "
            f"{[str(v) for v in self.components.values()]}"
        )

    def register_component(
        self, key: str, component: BaseComponentType
    ) -> None:
        """Registers a single component class for a given key."""
        self.components[str(key)] = component

    def register(
        self, name: str
    ) -> Callable[[BaseComponentType], BaseComponentType]:
        """Class decorator to register component classes to
        the internal registry.

        Args:
            name: The name of the component.

        Returns:
            A function which registers the class at this ComponentFactory.
        """

        def inner_wrapper(
            wrapped_class: BaseComponentType,
        ) -> BaseComponentType:
            """Inner wrapper for decorator."""
            if name in self.components:
                logger.debug(
                    "Executor %s already exists for factory %s, replacing it..",
                    name,
                    self.name,
                )
            self.register_component(name, wrapped_class)
            return wrapped_class

        return inner_wrapper


# Register the base stacks
artifact_store_factory: ComponentFactory = ComponentFactory(name="artifact")
artifact_store_factory.register_component(
    ArtifactStoreTypes.local, LocalArtifactStore
)

metadata_store_factory: ComponentFactory = ComponentFactory(name="metadata")
metadata_store_factory.register_component(
    MLMetadataTypes.mysql, MySQLMetadataStore
)
metadata_store_factory.register_component(
    MLMetadataTypes.sqlite, SQLiteMetadataStore
)

orchestrator_store_factory: ComponentFactory = ComponentFactory(
    name="orchestrator"
)

orchestrator_store_factory.register_component(
    OrchestratorTypes.local, LocalOrchestrator
)
