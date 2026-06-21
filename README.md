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

### 3. Deutsch-Jozsa Algorithm
Demonstrates structural exponential quantum speedup over classical methods using an n-bit function space evaluator. By exploiting phase kickback mechanics over custom-synthesized mathematical black boxes (oracles), the suite evaluates whether a hidden mapping structure is uniform (constant) or split (balanced) using only a single operational execution query.

#### Results
* **Constant Verification:** Yields a 100% computational reading concentrated squarely on the ground state vector string `000`.
* **Balanced Verification:** Resolves entirely into active non-zero configurations (e.g., `111`), completely bypassing the ground state.

### 4. Bernstein-Vazirani Algorithm
Demonstrates a striking case of quantum speedup where a hidden binary string $s \in \{0,1\}^n$ is extracted from a black-box oracle function $f(x) = s \cdot x \pmod 2$ in a **single operational execution query**. While a classical machine would require $n$ individual bitwise queries to reliably guess the string, the Bernstein-Vazirani variant exploits phase kickback mechanics to reconstruct the entire string simultaneously.

#### Results

When executed using the local simulation layer for **1024 shots**, the computational measurement results demonstrate a perfect probability lock on the secret key configuration, completely bypassing classical query limitations:

* **Secret String Verification:** Reconstructing a sample hidden mask string (e.g., `1001`) yields a 100% concentrated readout returning exactly $|1001\rangle$, proving deterministic extraction

### 5. Grover's Search Algorithm

Demonstrates unstructured database search capabilities using **Amplitude Amplification**. Over an item space $N = 4$ constructed across a 2-qubit system, a target address state vector is dynamically marked by a phase oracle using a Controlled-Z ($CZ$) inversion framework. By running a geometric matrix reflection step via the Grover Diffuser, the system shifts state probabilities, transforming a uniform probability field into a 100% focused readout spike on the targeted unindexed location parameter using only a single query step— achieving an analytical quadratic optimization boundary over classical $O(N)$ scanning models.

#### Results

Running the algorithm workspace pipeline against individual system address parameters generates high-density reading arrays confirming total probability focus configuration states:

* **Target Target Identification:** Looking for target parameter states (e.g., $|10\rangle$ or $|11\rangle$) evaluates cleanly down to 1024 standalone target output registration arrays, validating complete mathematical convergence.

---

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/SanskritiiAnand/quantum-simulations.git
cd quantum-simulations

-- If git not pre-installed: Click 'Code' at top of the page, download ZIP folder, extract the files and open them in terminal/IDE --
```

### 2. Configure virtual environment
```bash
Windowws:
python -m venv venv
venv\Scripts\activate
Mac/Linux:
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run master engine
```bash
python main.py
```

Select 1 for Entanglement workspace; 2 for Teleportation pipeline; 3 for QSphere Phase Tracking analysis; 4 for Deutsch-Jozsa algorithm; 5 for Bernstein-Vazirani algorithm; 6 for Grover's Search algorithm - when prompted, directly in your terminal line.
