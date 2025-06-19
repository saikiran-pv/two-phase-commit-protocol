# 🧠 Two-Phase Commit Protocol in Distributed Systems

This project simulates a distributed transaction system using the **Two-Phase Commit (2PC)** protocol, implemented in **Python** with **XML-RPC** communication. It includes a **Transaction Coordinator**, multiple **Participants**, and a **Client/Transaction Initializer**. The system demonstrates core distributed systems principles including **fault tolerance**, **failure recovery**, and **transactional atomicity**.

---

## 📂 Project Structure

```
.
👉── coordinator/
    └── transaction_coordinator.py
👉── participant/
    └── transaction_participant.py
👉── coordinator_node.py
👉── participant_node.py
👉── start_transaction.py
👉── setup_logger.py
```

---

## 🚀 Getting Started

### ✅ Prerequisites

* Python 3.11.0+
* Git
* Terminal (Linux/Mac) or Command Prompt/PowerShell (Windows)

### ⚙️ Setup & Run

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/distributed-2pc.git
cd distributed-2pc
```

2. **Open four terminal windows/tabs in the project directory** and run:

* **Coordinator Terminal**:

```bash
python3 coordinator_node.py
```

* **Participant 1 Terminal**:

```bash
python3 participant_node.py 8001
```

* **Participant 2 Terminal**:

```bash
python3 participant_node.py 8002
```

* **Transaction Initializer Terminal**:

```bash
python3 start_transaction.py <fail_scenario>
```

Replace `<fail_scenario>` with an integer between `0` and `4` to simulate different failure modes.

---

## 🧰 Components

### 1. Transaction Coordinator

* Coordinates prepare and commit phases
* Communicates with participants via XML-RPC
* Logs all events
* Simulates timeout/failure scenarios

### 2. Participants

* Participate in transaction voting and committing
* Handle simulated failure cases
* Log every step and decision
* Communicate with the coordinator via XML-RPC

### 3. Threaded XML-RPC Server

* Supports concurrent requests in both coordinator and participant nodes using multi-threaded RPC servers

---

## 🧪 Failure Scenarios

The `fail_scenario` argument in `start_transaction.py` can simulate:

* Coordinator or participant timeout
* Crash before/after voting
* Crash before/after committing
* Recovery and logging after failures

---

## 📘 Features

* Simulates Two-Phase Commit (2PC) with RPC messaging
* Thread-safe communication via multi-threaded servers
* Logs to both console and `.log` files
* Fault injection and recovery simulation

---

## 🧠 What I Learned

* Implementation of distributed transaction protocols
* Fault tolerance and recovery strategies in distributed systems
* Coordinated decision-making and atomicity in multi-node environments
* Handling node failures and log-based recovery

---

## 🐞 Challenges Faced

* Simulating and managing node crashes gracefully
* Managing timing issues during timeouts
* Achieving consistency in logs and RPC message ordering

---
