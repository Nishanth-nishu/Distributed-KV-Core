import hashlib
import json

class ConsistentHasher:
    def __init__(self, nodes=None, replicas=3):
        self.replicas = replicas
        self.ring = {}
        self.sorted_keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)

    def _hash(self, key):
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

    def add_node(self, node):
        for i in range(self.replicas):
            h = self._hash(f"{node}:{i}")
            self.ring[h] = node
            self.sorted_keys.append(h)
        self.sorted_keys.sort()

    def get_node(self, key):
        if not self.ring:
            return None
        h = self._hash(key)
        for ring_h in self.sorted_keys:
            if h <= ring_h:
                return self.ring[ring_h]
        return self.ring[self.sorted_keys[0]]

class StorageNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.data = {}

    def put(self, key, value):
        self.data[key] = value
        print(f"Node {self.node_id}: Stored {key}={value}")

    def get(self, key):
        return self.data.get(key)

class AmzKVStore:
    def __init__(self, node_ids, replication_factor=3):
        self.hasher = ConsistentHasher(node_ids)
        self.nodes = {nid: StorageNode(nid) for nid in node_ids}
        self.replication_factor = replication_factor
        self.active_nodes = sorted(node_ids)

    def put(self, key, value):
        primary_node_id = self.hasher.get_node(key)
        # In a real Dynamo system, we'd replicate to N successors on the ring
        start_idx = self.active_nodes.index(primary_node_id)
        
        for i in range(self.replication_factor):
            node_idx = (start_idx + i) % len(self.active_nodes)
            node_id = self.active_nodes[node_idx]
            self.nodes[node_id].put(key, value)

    def get(self, key):
        primary_node_id = self.hasher.get_node(key)
        # Simplified: get from primary. Real systems use Quorum (R+W > N)
        return self.nodes[primary_node_id].get(key)

if __name__ == "__main__":
    # Simulate a small cluster
    store = AmzKVStore(["node-1", "node-2", "node-3", "node-4", "node-5"])
    
    # Test distribution and replication
    print("--- Storing Data ---")
    store.put("user_123", {"name": "Alice", "email": "alice@example.com"})
    store.put("order_99", {"item": "Kindle", "price": 99.99})

    print("\n--- Retrieving Data ---")
    print(f"user_123: {store.get('user_123')}")
    print(f"order_99: {store.get('order_99')}")
