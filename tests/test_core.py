import unittest
from amz_kv.src.hashing import ConsistentHashRing
from amz_kv.src.storage import InMemoryStorageNode

class TestAmzKV(unittest.TestCase):
    def test_consistent_hashing_distribution(self):
        ring = ConsistentHashRing(replicas=3)
        ring.add_node("node-1")
        ring.add_node("node-2")
        
        node_a = ring.get_primary_node("key1")
        node_b = ring.get_primary_node("key2")
        
        self.assertIn(node_a, ["node-1", "node-2"])
        self.assertIn(node_b, ["node-1", "node-2"])

    def test_storage_node_ops(self):
        node = InMemoryStorageNode("test-node")
        node.put("foo", "bar")
        self.assertEqual(node.get("foo"), "bar")
        self.assertIsNone(node.get("non-existent"))

if __name__ == "__main__":
    unittest.main()
