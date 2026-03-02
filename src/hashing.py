import hashlib
from typing import List, Dict
from .interfaces import IHashRing

class ConsistentHashRing(IHashRing):
    """Implementation of a consistent hashing ring with virtual nodes.
    
    Adheres to the Open-Closed principle: New hashing strategies can be 
    implemented by extending IHashRing.
    """
    
    def __init__(self, replicas: int = 3):
        self.replicas = replicas
        self.ring: Dict[int, str] = {}
        self.sorted_keys: List[int] = []

    def _hash(self, key: str) -> int:
        """Internal MD5 hashing utility."""
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

    def add_node(self, node_id: str) -> None:
        for i in range(self.replicas):
            h = self._hash(f"{node_id}:{i}")
            self.ring[h] = node_id
            self.sorted_keys.append(h)
        self.sorted_keys.sort()

    def remove_node(self, node_id: str) -> None:
        # Implementation for node removal
        keys_to_remove = [k for k, v in self.ring.items() if v == node_id]
        for k in keys_to_remove:
            del self.ring[k]
            self.sorted_keys.remove(k)

    def get_primary_node(self, key: str) -> str:
        if not self.ring:
            raise ValueError("Hash ring is empty.")
        
        h = self._hash(key)
        for ring_h in self.sorted_keys:
            if h <= ring_h:
                return self.ring[ring_h]
        return self.ring[self.sorted_keys[0]]

    def get_nodes(self) -> List[str]:
        return sorted(list(set(self.ring.values())))
