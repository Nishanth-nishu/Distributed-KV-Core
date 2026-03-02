from typing import Any, Dict, List, Optional
from .interfaces import IHashRing, IStorageNode

class DistributedKVStore:
    """The high-level engine coordinating distributed storage operations.
    
    Dependency Inversion: Depends on IHashRing and IStorageNode interfaces,
    allowing for easy swapping of hashing or storage implementations.
    """
    
    def __init__(
        self, 
        hash_ring: IHashRing, 
        nodes: Dict[str, IStorageNode], 
        replication_factor: int = 3
    ):
        self.hash_ring = hash_ring
        self.nodes = nodes
        self.replication_factor = replication_factor

    def put(self, key: str, value: Any) -> None:
        """Stores data with replication across N nodes."""
        primary_id = self.hash_ring.get_primary_node(key)
        all_node_ids = self.hash_ring.get_nodes()
        
        try:
            start_idx = all_node_ids.index(primary_id)
        except ValueError:
            print(f"Error: Node {primary_id} not found in active nodes.")
            return

        # Replicate to N successors
        for i in range(self.replication_factor):
            idx = (start_idx + i) % len(all_node_ids)
            target_id = all_node_ids[idx]
            self.nodes[target_id].put(key, value)

    def get(self, key: str) -> Optional[Any]:
        """Retrieves data from the primary node."""
        primary_id = self.hash_ring.get_primary_node(key)
        return self.nodes[primary_id].get(key)
