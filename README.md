# Quantum Simulations

A professionally structured collection of quantum circuits, algorithms, and simulation workflows built using Qiskit and Python.

## Project Architecture

This repository uses a modular design to separate quantum logic, hardware simulation execution, and data visualization. This ensures scalability when adding new quantum circuits.

*   **`main.py`**: The central controller that orchestrates the entire workflow.
*   **`src/circuits.py`**: Contains functions for building quantum circuit structures (e.g., Bell states, GHZ states etc).
*   **`src/execution.py`**: Configures and runs transpiled circuits on the local `AerSimulator`.
*   **`src/utils.py`**: Handles data visualization utilities and plotting results.

---

## Completed Simulations

### 1. Two-Qubit Bell State
The foundational circuit creates a maximally entangled Bell state:

$$\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

#### Results
When executed on the local `AerSimulator` for **4,096 shots**, the circuit yields a near-perfect 50/50 statistical distribution between the $|00\rangle$ and $|11\rangle$ states, demonstrating quantum entanglement in a simulated environment:

*   **Measured Counts:** `{'00': 2096, '11': 2000}`

---

## Setup & Installation

1. **Clone the repository**
```bash
   git clone [https://github.com/SanskritiiAnand/quantum-simulations.git](https://github.com/SanskritiiAnand/quantum-simulations.git)
   cd quantum-simulations
2. **Install dependencies**
'''bash
    pip install -r requirements.txt
3. **Run master workflow**
'''bash
   python main.py
