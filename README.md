# Quantum Simulations

A structured collection of quantum circuits, algorithms, and simulation workflows built using Qiskit and Python.

## Project Architecture

This repository uses a modular design to separate quantum logic, hardware simulation execution, and data visualization to ensures scalability when adding new quantum circuits.

* **`main.py`**: CLI controller that orchestrates workspace selection and workflows.
* **`src/circuits.py`**: Contains functions for building quantum circuit structures (e.g., Bell states, Teleportation protocols etc).
* **`src/execution.py`**: Handles ideal local simulations using both `AerSimulator` and modern Qiskit `StatevectorSampler` primitives.
* **`src/utils.py`**: Handles custom data analytics and visualization utilities.

---

## Completed Simulations

### 1. Two-Qubit Bell State
The foundational circuit creates a maximally entangled Bell state:

$$\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

#### Results
When executed using the `StatevectorSampler` for **4,000 shots**, the circuit yields a near-perfect 50/50 statistical distribution between the |00⟩ and |11⟩ states, demonstrating quantum entanglement in a simulated environment:
* **Measured Counts:** `{'00': 2096, '11': 2000}` (~51% / ~49%)

### 2. Quantum Teleportation Protocol
An advanced 3-qubit implementation demonstrating the transfer of an unknown quantum state using a shared entangled resource channel and classical feed-forward communication. Features dynamic mid-circuit measurements and real-time conditional Pauli correction logic (`if_test`).

#### Results
By initializing Alice's qubit into a superposition state and performing a computational-basis rotation on Bob's terminal, a dual-bin shot memory histogram confirms identical probability states— verifying flawless state transfer across 1,024 shots.

---

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/SanskritiiAnand/quantum-simulations.git
cd quantum-simulation
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run master engine
```bash
python main.py
```

Select 1 for Entanglement workspace; 2 for Teleportation pipeline; 3 for QSphere Phase Tracking analysis- when prompted, directly in your terminal line.
