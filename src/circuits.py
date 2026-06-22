from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import circuit_drawer
import numpy as np

def save_or_show_circuit_layout(circuit: QuantumCircuit):
    """
    Renders and displays the visual layout diagram of a given quantum circuit.
    """
    fig = circuit_drawer(circuit, output="mpl", plot_barriers=False)
    return fig

# =====================================================================
# 1. BELL STATE & TELEPORTATION INFRASTRUCTURE
# =====================================================================

def create_bell_state_circuit() -> QuantumCircuit:
    """
    Creates a standard 2-qubit Bell State circuit: (|00> + |11>) / sqrt(2)
    """
    qc = QuantumCircuit(2)
    qc.h(0)        # Apply Hadamard to qubit 0
    qc.cx(0, 1)    # Apply CNOT from qubit 0 to qubit 1
    qc.measure_all()
    return qc

def create_teleportation_circuit() -> QuantumCircuit:
    """
    Builds a 3-qubit Quantum Teleportation circuit featuring state preparation,
    entangled Bell-pair linking, mid-circuit measurements, and conditional feed-forward.
    """
    q_reg = QuantumRegister(3, name='q')
    c_reg = ClassicalRegister(3, name='c')
    qc = QuantumCircuit(q_reg, c_reg)
    
    #State Preparation (Alice's secret state |+>)
    qc.h(0)
    qc.barrier()
    
    #Creating the shared EPR Bell pair between Alice and Bob
    qc.h(1)
    qc.cx(1, 2)
    qc.barrier()
    
    #Alice's bell-basis measurement preparation
    qc.cx(0, 1)
    qc.h(0)
    qc.barrier()
    
    #Mid-circuit measurements mapping quantum states to classical channels
    qc.measure(q_reg[0], c_reg[0])
    qc.measure(q_reg[1], c_reg[1])
    qc.barrier()
    
    #Bob's conditional correction based on classical feed-forward bits
    with qc.if_test((c_reg[0], 1)):
        qc.z(q_reg[2])
    qc.barrier()
    
    #Transform Bob's qubit back to computational basis to verify transfer
    qc.h(q_reg[2])
    qc.measure(q_reg[2], c_reg[2])
    
    return qc

def create_labeled_teleportation_circuit() -> QuantumCircuit:
    """
    Builds a 3-qubit teleportation circuit with custom section barriers
    and complete conditional feed-forward recovery gates (X and Z).
    """
    q_reg = QuantumRegister(3, name='q')
    c_reg = ClassicalRegister(3, name='c')
    qc = QuantumCircuit(q_reg, c_reg)

    #Alice: Message Preparation (|+) state)
    qc.h(q_reg[0])
    qc.barrier(label="Msg Prep")

    #EPR Bell Pair creation
    qc.h(q_reg[1])
    qc.cx(q_reg[1], q_reg[2])
    qc.barrier(label="Bell Pair")

    #Alice's Entangling Operations
    qc.cx(q_reg[0], q_reg[1])
    qc.h(q_reg[0])
    qc.barrier(label="Alice's Ops")

    #Mid-circuit measurement channel mapping
    qc.measure(q_reg[0], c_reg[0])
    qc.measure(q_reg[1], c_reg[1])
    qc.barrier(label="Alice's Meas")

    # Bob's Complete Conditional Recovery Protocol
    with qc.if_test((c_reg[1], 1)):
        qc.x(q_reg[2])
    with qc.if_test((c_reg[0], 1)):
        qc.z(q_reg[2])
    qc.barrier(label="Bob's Recovery")
    
    return qc

# =====================================================================
# 2. DEUTSCH-JOZSA & BERNSTEIN-VAZIRANI ALGORITHMS
# =====================================================================

def create_dj_oracle(num_qubits: int, mode: str = "balanced") -> QuantumCircuit:
    """
    Generates a Deutsch-Jozsa oracle circuit for 'num_qubits' input lines.
    Modes:
      - 'constant': Returns 0 or 1 for all inputs.
      - 'balanced': Returns 0 for half the states, 1 for the other half.
    """
    oracle_circuit = QuantumCircuit(num_qubits + 1, name=f"DJ_Oracle_{mode.capitalize()}")
    
    if mode == "constant":
        import random
        if random.choice([True, False]):
            oracle_circuit.x(num_qubits)
            
    elif mode == "balanced":
        for qubit in range(num_qubits):
            oracle_circuit.cx(qubit, num_qubits)
            
    return oracle_circuit

def create_deutsch_jozsa_circuit(num_qubits: int, mode: str = "balanced") -> QuantumCircuit:
    """
    Assembles the full Deutsch-Jozsa algorithm layout by preparing superpositions,
    embedding the target oracle, and applying the final decoding Hadamard gates.
    """
    qc = QuantumCircuit(num_qubits + 1, num_qubits)
    
    #Initialize target qubit to |1>
    qc.x(num_qubits)
    qc.barrier(label="Initialization")
    
    #Put all qubits into a superposition (|H> on inputs, |-> on target for phase kickback)
    for q in range(num_qubits + 1):
        qc.h(q)
    qc.barrier(label="Superposition")
    
    #Append the chosen hidden Oracle
    oracle = create_dj_oracle(num_qubits, mode=mode)
    qc.compose(oracle, inplace=True)
    qc.barrier(label="Oracle Injection")
    
    #Apply final Hadamards to the input lines to decode interference paths
    for q in range(num_qubits):
        qc.h(q)
    qc.barrier(label="Interference")
    
    #Measure the input qubits
    for q in range(num_qubits):
        qc.measure(q, q)
        
    return qc

def create_bv_oracle(hidden_str: str) -> QuantumCircuit:
    """Generates a hidden Bernstein-Vazirani oracle circuit."""
    num_qubits = len(hidden_str)
    oracle_circuit = QuantumCircuit(num_qubits + 1, name=f"Oracle_BV_{hidden_str}")
    
    for index, bit in enumerate(reversed(hidden_str)):
        if bit == '1':
            oracle_circuit.cx(index, num_qubits)

    return oracle_circuit

def create_bernstein_vazirani_circuit(hidden_str: str) -> QuantumCircuit:
    """Assembles the complete Bernstein-Vazirani algorithm workspace layout."""
    num_qubits = len(hidden_str)
    qc = QuantumCircuit(num_qubits + 1, num_qubits)

    #Initialize target qubit to |1>
    qc.x(num_qubits)
    qc.barrier(label="Initialization")

    #Apply Hadamards to all qubits (superposition + phase kickback)
    for q in range(num_qubits + 1):
        qc.h(q)
    qc.barrier(label="Superposition")

    #Inject the chosen hidden oracle
    oracle = create_bv_oracle(hidden_str)
    qc.compose(oracle, inplace=True)
    qc.barrier(label="Oracle_Injection")

    #Final Hadamards to input qubits to decode state phase shifts
    for q in range(num_qubits):
        qc.h(q)
    qc.barrier(label="Interference")

    #Read input register
    for q in range(num_qubits):
        qc.measure(q, q)
        
    return qc

# =====================================================================
# 3. GROVER'S AMPLITUDE AMPLIFICATION SEARCH
# =====================================================================

def create_grover_oracle(target_str: str) -> QuantumCircuit:
    """
    Generates a 2-qubit phase oracle that flips the sign of the target state. 
    Available targets: '00', '01', '10', '11'
    """
    oracle_ckt = QuantumCircuit(2, name=f"Oracle_Grover_{target_str}")

    if target_str == "00":
        oracle_ckt.x([0, 1])
    elif target_str == "01":
        oracle_ckt.x(1) 
    elif target_str == "10":
        oracle_ckt.x(0)
    
    oracle_ckt.cz(0, 1)  # CZ flips sign of |11> state

    if target_str == "00":
        oracle_ckt.x([0, 1])
    elif target_str == "01":
        oracle_ckt.x(1)
    elif target_str == "10":
        oracle_ckt.x(0)
    
    return oracle_ckt

def create_grover_diffuser() -> QuantumCircuit:
    """Generates the standard 2-qubit grover diffuser (inversion about the mean)."""
    diffuser = QuantumCircuit(2, name="Diffuser")

    diffuser.h([0, 1])
    diffuser.x([0, 1])
    diffuser.cz(0, 1)
    diffuser.x([0, 1])
    diffuser.h([0, 1])

    return diffuser

def create_grover_search_circuit(target_str: str) -> QuantumCircuit:
    """Assembles the complete 2-qubit Grover Search circuit workspace."""
    qc = QuantumCircuit(2, 2)

    qc.h([0, 1])
    qc.barrier(label="Superposition")

    oracle = create_grover_oracle(target_str)
    qc.compose(oracle, inplace=True)
    qc.barrier(label="Oracle_Marking")

    diffuser = create_grover_diffuser()
    qc.compose(diffuser, inplace=True)
    qc.barrier(label="Amplitude_Amplification")

    qc.measure([0, 1], [0, 1])
    return qc

# =====================================================================
# 4. SIMON'S PERIOD HIDDEN MASK ALGORITHM
# =====================================================================

def create_simon_oracle(hidden_mask: str) -> QuantumCircuit:
    """
    Generates a dynamic 2-qubit Simon's algorithm oracle for 2-to-1 mapping.
    Works for any mask: '00', '01', '10', '11'
    """
    oracle_ckt = QuantumCircuit(4, name=f"Oracle_Simon_{hidden_mask}")

    # 1:1 copy of input register to auxiliary register using CX gates
    if hidden_mask == "00":
        oracle_ckt.cx(0, 2)
        oracle_ckt.cx(1, 3)
    
    elif hidden_mask == "01":
        oracle_ckt.cx(1, 3) # f(x) must be independent of q_0, only copy q_1
    
    elif hidden_mask == "10":
        oracle_ckt.cx(0, 2) # f(x) must be independent of q_1, only copy q_0
    
    elif hidden_mask == "11":
        oracle_ckt.cx(0, 2)
        oracle_ckt.cx(1, 3)
        oracle_ckt.cx(0, 3)
        oracle_ckt.cx(1, 2)

    return oracle_ckt

def create_simon_circuit(hidden_mask: str) -> QuantumCircuit:
    """Assembles the complete 4-qubit Simon's Period Finder circuit workspace."""
    qc = QuantumCircuit(4, 2)
    
    #Initialize input register to equal superposition
    qc.h([0, 1])
    qc.barrier(label="Superposition")
    
    #Inject 1-to-1 or 2-to-1 constraint oracle
    oracle = create_simon_oracle(hidden_mask)
    qc.compose(oracle, [0, 1, 2, 3], inplace=True)
    qc.barrier(label="Oracle_Injection")
    
    #Apply final interference decoding to the input register
    qc.h([0, 1])
    qc.barrier(label="Interference")
    
    #Read the data from input channels
    qc.measure([0, 1], [0, 1])
    return qc

# =====================================================================
# 5. SHOR'S PERIOD FINDING & CORE FACTORING MODULE
# =====================================================================

def create_shor_oracle(a: int, power: int) -> QuantumCircuit:
    """
    Controlled multiplication by a^power mod 15.
    Serves as our modular exponentiation oracle for N=15.
    """
    if a not in [2, 4, 7, 8, 11, 13]:
        raise ValueError("'a' must be coprime to 15")
        
    U = QuantumCircuit(4)        
    for _ in range(power):
        if a in [2, 13]:
            U.swap(0, 1); U.swap(1, 2); U.swap(2, 3)
        if a in [7, 8]:
            U.swap(2, 3); U.swap(1, 2); U.swap(0, 1)
        if a in [4, 11]:
            U.swap(0, 2); U.swap(1, 3)
        if a in [7, 11, 13]:
            for q in range(4):
                U.x(q)
                
    U_gate = U.to_gate()
    U_gate.name = f"{a}^{power} mod 15"
    c_U = U_gate.control()
    return c_U

def inverse_qft(n: int) -> QuantumCircuit:
    """Generates an n-qubit Inverse Quantum Fourier Transform circuit."""
    iqft_circ = QuantumCircuit(n, name="IQFT")
    for qubit in range(n // 2):
        iqft_circ.swap(qubit, n - qubit - 1)
    for j in range(n):
        for m in range(j):
            iqft_circ.cp(-np.pi / float(2**(j - m)), m, j)
        iqft_circ.h(j)
    return iqft_circ

def create_shor_circuit(a: int) -> QuantumCircuit:
    """Assembles the 7-qubit phase estimation circuit architecture for Shor's core."""
    qc = QuantumCircuit(7, 3)

    #Initialize 3 counting qubits to equal superposition
    qc.h([0, 1, 2])
    qc.barrier(label="Superposition")

    #Initialize 4 target auxiliary qubits to state |1>
    qc.x(3)
    qc.barrier(label="Target_Init")

    #Cascade Controlled Modular Exponentiation operators
    qc.append(create_shor_oracle(a, 1), [0, 3, 4, 5, 6])
    qc.append(create_shor_oracle(a, 2), [1, 3, 4, 5, 6])
    qc.append(create_shor_oracle(a, 4), [2, 3, 4, 5, 6])
    qc.barrier(label="Mod_Exp")

    #Apply Inverse Quantum Fourier Transform to translate phase cycles
    iqft = inverse_qft(3)
    qc.compose(iqft, qubits=[0, 1, 2], inplace=True)
    qc.barrier(label="Inverse_QFT")

    #Measure the counting register
    qc.measure([0, 1, 2], [0, 1, 2])
    return qc
