from abc import ABC, abstractmethod
from typing import Any, List, Optional

class IStorageNode(ABC):
    """Interface for a storage node in the distributed system."""
    
    @property
    @abstractmethod
    def node_id(self) -> str:
        """Returns the unique identifier for the node."""
        pass

    @abstractmethod
    def put(self, key: str, value: Any) -> bool:
        """Stores a value associated with a key."""
        pass

    @abstractmethod
    def get(self, key: str) -> Optional[Any]:
        """Retrieves a value associated with a key."""
        pass

class IHashRing(ABC):
    """Interface for the consistent hashing mechanism."""
    
    @abstractmethod
    def add_node(self, node_id: str) -> None:
        """Adds a node to the hashing ring."""
        pass

    @abstractmethod
    def remove_node(self, node_id: str) -> None:
        """Removes a node from the hashing ring."""
        pass

    @abstractmethod
    def get_primary_node(self, key: str) -> str:
        """Returns the primary node ID for a given key."""
        pass

    @abstractmethod
    def get_nodes(self) -> List[str]:
        """Returns a list of all active nodes in the ring."""
        pass
