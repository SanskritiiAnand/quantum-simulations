# Quantum Simulations

A structured collection of quantum circuits, algorithms, and simulation workflows built using Qiskit and Python.

## Project Architecture

This repository uses a modular design to separate quantum logic, hardware simulation execution, and data visualization to ensure scalability when adding new quantum circuits.

* **`main.py`**: CLI controller that orchestrates workspace selection and workflows.
* **`src/circuits.py`**: Contains functions for building quantum circuit structures (e.g., Bell states, Teleportation protocols etc).
* **`src/execution.py`**: Handles ideal local simulations using both `AerSimulator` and modern Qiskit `StatevectorSampler` primitives.
* **`src/utils.py`**: Handles custom data analytics and visualization utilities.

---

## Completed Simulations

### 1. Two-Qubit Bell State
This foundational circuit creates a maximally entangled Bell state:

$$\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

#### Results
When executed using the `StatevectorSampler` for **4,000 shots**, the circuit yields a near-perfect 50/50 statistical distribution between the |00⟩ and |11⟩ states, demonstrating quantum entanglement in a simulated environment:
* **Measured Counts:** `{'00': 2096, '11': 2000}` (~51% / ~49%)

### 2. Quantum Teleportation Protocol
An advanced 3-qubit implementation demonstrating the transfer of an unknown quantum state using a shared entangled resource channel and classical feed-forward communication. Features dynamic mid-circuit measurements and real-time conditional Pauli correction logic (`if_test`).

#### Results
By initializing Alice's qubit into a superposition state and performing a computational-basis rotation on Bob's terminal, a dual-bin shot memory histogram confirms identical probability states— verifying flawless state transfer across 1,024 shots. An alternate tracking pipeline renders a 3D QSphere to verify state vector phases before terminal measurement.

### 3. Quantum Teleportation Protocol (QSphere Phase Tracking)
This specialized pipeline variants the teleportation architecture by tracking the full, uncollapsed statevector profile rather than tracking bitstring memory records over time. It utilizes a cleanly labeled circuit setup to follow state transitions through distinct operational stages.

#### Results
Right before Bob applies his final conditional transformations, the workspace captures the pure quantum state vector and renders an interactive 3D QSphere layout. This maps the probability amplitudes and complex phase angles across the 3-qubit phase space, visually demonstrating how the uncollapsed state remains perfectly preserved across the system before the terminal measurement collapses it back to the computational basis.

### 4. Deutsch-Jozsa Algorithm
Demonstrates structural exponential quantum speedup over classical methods using an n-bit function space evaluator. By exploiting phase kickback mechanics over custom-synthesized mathematical black boxes (oracles), the suite evaluates whether a hidden mapping structure is uniform (constant) or split (balanced) using only a single operational execution query.

#### Results
* **Constant Verification:** Yields a 100% computational reading concentrated squarely on the ground state vector string `000`.
* **Balanced Verification:** Resolves entirely into active non-zero configurations (e.g., `111`), completely bypassing the ground state.

### 5. Bernstein-Vazirani Algorithm
Demonstrates a striking case of quantum speedup where a hidden binary string $s \in \{0,1\}^n$ is extracted from a black-box oracle function $f(x) = s \cdot x \pmod 2$ in a **single operational execution query**. While a classical machine would require $n$ individual bitwise queries to reliably guess the string, the Bernstein-Vazirani variant exploits phase kickback mechanics to reconstruct the entire string simultaneously.

#### Results

When executed using the local simulation layer for **1024 shots**, the computational measurement results demonstrate a perfect probability lock on the secret key configuration, completely bypassing classical query limitations:

* **Secret String Verification:** Reconstructing a sample hidden mask string (e.g., `1001`) yields a 100% concentrated readout returning exactly $|1001\rangle$, proving deterministic extraction

### 6. Grover's Search Algorithm

Demonstrates unstructured database search capabilities using **Amplitude Amplification**. Over an item space $N = 4$ constructed across a 2-qubit system, a target address state vector is dynamically marked by a phase oracle using a Controlled-Z ($CZ$) inversion framework. By running a geometric matrix reflection step via the Grover Diffuser, the system shifts state probabilities, transforming a uniform probability field into a 100% focused readout spike on the targeted unindexed location parameter using only a single query step— achieving an analytical quadratic optimization boundary over classical $O(N)$ scanning models.

#### Results

The algorithm pipeline features an intermediate **QSphere State Profile step**. Because the amplitude amplification maximally isolates the target vector, the 3D QSphere shows all incorrect basis state nodes drained completely to zero size, leaving a single massive node anchoring the targeted state.

* **Target Identification:** Looking for target parameter states (e.g., $|10\rangle$ or $|11\rangle$) evaluates cleanly down to 1024 standalone target output registration arrays, validating complete mathematical convergence.

### 7. Simon's Algorithm
Demonstrates a foundational example of exponential quantum speedup solving a period-finding problem over a bitwise XOR function. For a black-box function $f(x)$ guaranteed to satisfy the constraint $f(x) = f(y) \iff x \oplus y = s$, the quantum engine isolates the hidden bitstring mask $s \in \{0,1\}^n$ using significantly fewer queries than the classical lower bound of $O(2^{n/2})$.

#### Results
By preparing uniform input superpositions, evaluating the oracle, and applying a final decoding Hadamard wall, the input register resolves into a balanced superposition of valid states satisfying the strict linear system constraint $b \cdot s = 0 \pmod 2$. 
* **Mask Extraction Verification:** Testing with hidden mask $s = 11$ successfully limits measurement readouts exclusively to states $|00\rangle$ and $|11\rangle$. The classical post-processing script evaluates the system equations to extract the hidden mask flawlessly.

### 8. Shor's Algorithm 
Demonstrates polynomial-time prime factorization of numbers ($O((\log N)^3)$), exposing a vulnerability in RSA cryptography architectures. The pipeline handles the heavy lifting quantum period-finding engine for $N=15$. 

The workflow couples an initialized superposition state register across 3 counting qubits with 4 target auxiliary qubits. It pipes modular exponentiation oracles ($a^x \pmod N$) to encode global mathematical cycles into the state space, then deploys an **Inverse Quantum Fourier Transform (IQFT)** to act as an interferometric prism, shifting distributed periodicity loops into distinct, sharp, localized phase peaks.

#### Results
The workspace implements a multi-tiered visualization workflow:
1. **Interactive QSphere Profile:** Right before state collapse, the engine captures the pure state vector, rendering **4 distinct, symmetrically spaced nodes** on a 3D sphere that highlight the exact phase multiples ($0, 1/4, 2/4, 3/4$) of the hidden sequence.
2. **Classical Post-Processing:** Upon closing the phase canvas, the engine samples the counting register, extracts the denominators via continued fraction approximation to determine the period $r=4$, and computes the Greatest Common Divisors ($\text{gcd}(a^{r/2} \pm 1, N)$).
3. **Factor Discovery:** Testing with base $a=7$ successfully calculates the exact, non-trivial prime factors of 15: `[3, 5]`.

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

Select 1 for Entanglement workspace; 2 for Teleportation pipeline; 3 for QSphere Phase Tracking analysis; 4 for Deutsch-Jozsa algorithm; 5 for Bernstein-Vazirani algorithm; 6 for Grover's Search algorithm; 7 for Simon's algorithm; 8 for Shor's algorithm, when prompted, directly in your terminal line.
