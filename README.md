# Distributed-KV-Core: High-Availability Key-Value Store

## Project Overview
**Distributed-KV-Core** is a peer-to-peer distributed key-value storage system designed for high availability, fault tolerance, and horizontal scalability. Inspired by modern distributed database architectures (like Dynamo), this project implements a decentralized storage engine that eliminates single points of failure.

## Key Technical Features
- **Consistent Hashing:** Implemented with a virtual node system to ensure uniform data distribution across a dynamic cluster. This minimizes data movement during node joins or leaves.
- **Factor Replication (N-Replication):** Ensures high availability by automatically replicating data to multiple successor nodes in the hash ring.
- **Fault Tolerance:** Designed to remain operational during individual node failures, ensuring data accessibility through replicated copies.
- **Decentralized Architecture:** A peer-to-peer model where no single node acts as a bottleneck, allowing the system to scale linearly.

## System Architecture
1. **Hashing Ring:** Nodes are mapped to a circular 128-bit hash space. Every node is assigned multiple "virtual nodes" to balance the load and prevent hotspots.
2. **Data Partitioning:** Each key is hashed and assigned to the first node on the ring with a hash value greater than the key's hash (the "coordinator node").
3. **Replication Logic:** Each write operation triggers synchronous replication to `N` consecutive nodes on the ring to maintain consistency and durability.

## SOLID Implementation & Best Practices
The core engine has been architected following **SOLID principles** to ensure maintainability and extensibility:

- **Single Responsibility (SRP):** Distinct modules for hashing logic, storage management, and cluster orchestration.
- **Open-Closed (OCP):** Use of Abstract Base Classes (ABCs) allows for pluggable hashing algorithms and storage backends (e.g., swapping MD5 for MurmurHash or In-Memory for Disk-level storage).
- **Dependency Inversion (DIP):** High-level orchestration depends on interfaces, not concrete implementations, facilitating easy testing and component swapping.
- **Modern Python Standards:** Extensive use of Type Hinting, Google-style Docstrings, and modular packaging.

## Technical Stack
- **Languages:** Python 3.x
- **Core Modules:** `hashlib`, `unittest`, `abc`, `typing`
- **Design Patterns:** Interface-driven design, Consistent Hashing (DHT), Strategy Pattern.

## How to Run
### Standard Simulation
```bash
python main.py
```
### SOLID Professional Version
```bash
python main_solid.py
```

## Testing
Comprehensive unit tests are included to verify the hashing ring distribution and storage node operations.
```bash
python -m unittest amz-kv/tests/test_core.py
```
