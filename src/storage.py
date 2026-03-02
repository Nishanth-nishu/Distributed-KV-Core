from typing import Any, Optional
from .interfaces import IStorageNode

class InMemoryStorageNode(IStorageNode):
    """A concrete implementation of a storage node using an in-memory dictionary.
    
    Single Responsibility: Managing local data state for a specific node.
    """
    
    def __init__(self, node_id: str):
        self._node_id = node_id
        self._data: dict = {}

    @property
    def node_id(self) -> str:
        return self._node_id

    def put(self, key: str, value: Any) -> bool:
        self._data[key] = value
        print(f"Node {self.node_id}: Logged 'PUT' for key '{key}'")
        return True

    def get(self, key: str) -> Optional[Any]:
        return self._data.get(key)
