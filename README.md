# Amz-KV: Distributed Key-Value Store (Dynamo-Inspired)

## Project Overview
Amz-KV is a peer-to-peer distributed key-value storage system designed for high availability and scalability. It is heavily inspired by the architecture described in the **Amazon Dynamo** paper. This project demonstrates core SDE competencies in distributed systems, consistent hashing, and replication strategies.

## Key Features
- **Consistent Hashing:** Uses a consistent hashing ring to partition data across multiple nodes, minimizing data movement when nodes are added or removed.
- **Replication:** Implements a replication factor (N) where data is copied to the primary node and its successors on the ring to ensure fault tolerance.
- **Fault Tolerance:** Designed to remain available even if individual storage nodes fail.
- **Scalability:** Easily add more nodes to the cluster with minimal reconfiguration.

## Technical Stack
- **Languages:** Python
- **Core Concepts:** MD5 Hashing, Ring Partitioning, Object-Oriented Design.

## System Architecture
1. **Hashing Ring:** Nodes are mapped to a 128-bit hash space using MD5. "Virtual nodes" (replicas) are used to ensure uniform data distribution.
2. **Data Partitioning:** Each key is hashed and assigned to the first node on the ring with a hash value greater than the key's hash.
3. **Replication Logic:** Each `put` operation replicates data to `N` consecutive nodes on the ring.

## How to Run
```bash
python main.py
```

## Amazon SDE I Alignment
- **Leadership Principles:** Customer Obsession (ensuring 100% availability for customer data), Invent and Simplify (simple yet powerful distribution logic).
- **Technical Excellence:** Deep dive into distributed hash tables (DHT) and replication protocols.

## SOLID & Best Practices (Pro Version)
This project has been refactored (`main_solid.py`) to demonstrate production-grade software engineering:
- **Single Responsibility (SRP):** Isolated hashing, storage, and orchestration logic.
- **Open-Closed (OCP):** Interfaces allow for new hashing or storage types without modifying existing code.
- **Liskov Substitution (LSP):** Concrete storage locations can be swapped seamlessly.
- **Interface Segregation (ISP):** Minimal, focused interfaces.
- **Dependency Inversion (DIP):** Orchestrator depends on abstractions, not concrete classes.
- **Advanced Features:** Type Hinting, Abstract Base Classes (ABC), Docstrings, and Component-based Testing.
