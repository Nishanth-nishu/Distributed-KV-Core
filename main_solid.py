from src.hashing import ConsistentHashRing
from src.storage import InMemoryStorageNode
from src.engine import DistributedKVStore

def main():
    """Entry point for the SOLID Amz-KV demonstration."""
    
    # 1. Setup Components (Dependency Injection)
    node_ids = ["node-alpha", "node-beta", "node-gamma", "node-delta", "node-epsilon"]
    
    # Instantiate concrete implementations
    ring = ConsistentHashRing(replicas=10) # 10 virtual nodes per physical node
    storage_nodes = {nid: InMemoryStorageNode(nid) for nid in node_ids}
    
    # Register nodes in ring
    for nid in node_ids:
        ring.add_node(nid)
        
    # 2. Initialize Engine
    store = DistributedKVStore(
        hash_ring=ring, 
        nodes=storage_nodes, 
        replication_factor=3
    )
    
    # 3. Perform Operations
    print("=== SOLID Amz-KV Simulation Started ===\n")
    
    print("Storing user session...")
    store.put("session_445", {"user": "admin", "theme": "dark"})
    
    print("\nStoring shopping cart...")
    store.put("cart_992", ["Kindle Paperwhite", "Echo Dot"])
    
    print("\n--- Retrieval Results ---")
    print(f"session_445: {store.get('session_445')}")
    print(f"cart_992: {store.get('cart_992')}")
    
    print("\n=== Simulation Finished ===")

if __name__ == "__main__":
    main()
