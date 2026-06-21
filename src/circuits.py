from qiskit import QuantumCircuit

def create_bell_state_circuit() -> QuantumCircuit:
    """
    Creates a standard 2-qubit Bell State circuit: (|00> + |11>) / sqrt(2)
    """
    qc = QuantumCircuit(2)
    qc.h(0)        # Apply Hadamard to qubit 0
    qc.cx(0, 1)    # Apply CNOT from qubit 0 to qubit 1
    qc.measure_all()
    return qc


from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer

def create_bell_state_circuit() -> QuantumCircuit:
    """
    Creates a standard 2-qubit Bell State circuit: (|00> + |11>) / sqrt(2)
    """
    qc = QuantumCircuit(2)
    qc.h(0)        # Apply Hadamard to qubit 0
    qc.cx(0, 1)    # Apply CNOT from qubit 0 to qubit 1
    qc.measure_all()
    return qc

def save_or_show_circuit_layout(circuit: QuantumCircuit):
    """
    Renders and displays the visual layout diagram of a given quantum circuit.
    """
    fig = circuit_drawer(circuit, output="mpl", plot_barriers=False)
    return fig


from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def create_teleportation_circuit() -> QuantumCircuit:
    """
    Builds a 3-qubit Quantum Teleportation circuit featuring state preparation,
    entangled Bell-pair linking, mid-circuit measurements, and conditional feed-forward.
    """
    q_reg = QuantumRegister(3, name='q')
    c_reg = ClassicalRegister(3, name='c')
    qc = QuantumCircuit(q_reg, c_reg)
    
    # 1. State Preparation (Alice's secret state |+>)
    qc.h(0)
    qc.barrier()
    
    # 2. Creating the shared EPR Bell pair between Alice and Bob
    qc.h(1)
    qc.cx(1, 2)
    qc.barrier()
    
    # 3. Alice's bell-basis measurement preparation
    qc.cx(0, 1)
    qc.h(0)
    qc.barrier()
    
    # 4. Mid-circuit measurements mapping quantum states to classical channels
    qc.measure(q_reg[0], c_reg[0])
    qc.measure(q_reg[1], c_reg[1])
    qc.barrier()
    
    # 5. Bob's conditional correction based on classical feed-forward bits
    with qc.if_test((c_reg[0], 1)):
        qc.z(q_reg[2])
    qc.barrier()
    
    # 6. Transform Bob's qubit back to computational basis to verify transfer
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

    # Alice: Message Preparation (|+) state)
    qc.h(q_reg[0])
    qc.barrier(label="Msg Prep")

    # EPR Bell Pair creation
    qc.h(q_reg[1])
    qc.cx(q_reg[1], q_reg[2])
    qc.barrier(label="Bell Pair")

    # Alice's Entangling Operations
    qc.cx(q_reg[0], q_reg[1])
    qc.h(q_reg[0])
    qc.barrier(label="Alice's Ops")

    # Mid-circuit measurement channel mapping
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
    
    # 1. Initialize target qubit to |1>
    qc.x(num_qubits)
    qc.barrier(label="Initialization")
    
    # 2. Put all qubits into a superposition (|H> on inputs, |-> on target for phase kickback)
    for q in range(num_qubits + 1):
        qc.h(q)
    qc.barrier(label="Superposition")
    
    # 3. Append the chosen hidden Oracle
    oracle = create_dj_oracle(num_qubits, mode=mode)
    qc.compose(oracle, inplace=True)
    qc.barrier(label="Oracle Injection")
    
    # 4. Apply final Hadamards to the input lines to decode interference paths
    for q in range(num_qubits):
        qc.h(q)
    qc.barrier(label="Interference")
    
    # 5. Measure the input qubits
    for q in range(num_qubits):
        qc.measure(q, q)
        
    return qc


def create_bv_oracle(hidden_str: str) -> QuantumCircuit:
    """
    Generates a hidden Bernstein-Vazirani oracle circuit
    """
    num_qubits = len(hidden_str)
    oracle_circuit = QuantumCircuit(num_qubits + 1, name=f"Oracle_BV_{hidden_str}")
    
    # Iterate through the bit string
    for index, bit in enumerate(reversed(hidden_str)):
        if bit == '1':
            oracle_circuit.cx(index, num_qubits)

    return oracle_circuit

def create_bernstein_vazirani_circuit(hidden_str: str) -> QuantumCircuit:
    """
    Assembles the complete Bernstein-Vazirani algorithm workspace layout
    """
    num_qubits = len(hidden_str)
    qc = QuantumCircuit(num_qubits + 1, num_qubits)

    # Initialize target qubit to |1>
    qc.x(num_qubits)
    qc.barrier(label="Initialization")

    # Apply Hadamards to all qubits (superposition + phase kickback)
    for q in range(num_qubits + 1):
        qc.h(q)
    qc.barrier(label="Superposition")

    # Inject the chosen hidden oracle
    oracle = create_bv_oracle(hidden_str)
    qc.compose(oracle, inplace=True)
    qc.barrier(label="Oracle_Injection")

    # Final Hadamards to input qubits to decode state phase shifts
    for q in range(num_qubits):
        qc.h(q)
    qc.barrier(label="Interference")

    # Read input register
    for q in range(num_qubits):
        qc.measure(q, q)
        
    return qc


def create_grover_oracle(target_str: str) -> QuantumCircuit:
    """
    Generates a 2-qubit phase oracle that flips the sign of the target state. 
    Available targets: '00', '01', '10', '11'
    """
    oracle_ckt = QuantumCircuit(2, name=f"Oracle_Grover_{target_str}")

    # Apply X gates to flip target bit configuration to |11> to utilize standard CZ phase flip 
    if target_str == "00":
        oracle_ckt.x([0, 1])
    elif target_str == "01":
        oracle_ckt.x(1)  # little-endian ordering 
    elif target_str == "10":
        oracle_ckt.x(0)
    
    oracle_ckt.cz(0, 1)  # CZ flips sign of |11> state

    # Revert X gates to restore the base states
    if target_str == "00":
        oracle_ckt.x([0, 1])
    elif target_str == "01":
        oracle_ckt.x(1)
    elif target_str == "10":
        oracle_ckt.x(0)
    
    return oracle_ckt

def create_grover_diffuser() -> QuantumCircuit:
    """
    Generates the standard 2-qubit grover diffuser (inversion about the mean)
    """
    diffuser = QuantumCircuit(2, name="Diffuser")

    # Transform out of superposition basis
    diffuser.h([0, 1])
    diffuser.x([0, 1])

    # Apply phase flip to the ground state |00>
    diffuser.cz(0, 1)

    # Restore states back to computational basis
    diffuser.x([0, 1])
    diffuser.h([0, 1])

    return diffuser

def create_grover_search_circuit(target_str: str) -> QuantumCircuit:
    """
    Assembles the complete 2-qubit Grover Search circuit workspace
    """
    qc = QuantumCircuit(2, 2)

    # Initialize qubits to equal superposition state
    qc.h([0, 1])
    qc.barrier(label="Superposition")

    # Inject phase oracle to mark target state
    oracle = create_grover_oracle(target_str)
    qc.compose(oracle, inplace=True)
    qc.barrier(label="Oracle_Marking")

    # Apply diffuser to amplify target state's amplitude
    diffuser = create_grover_diffuser()
    qc.compose(diffuser, inplace=True)
    qc.barrier(label="Amplitude_Amplification")

    # Measure qubits
    qc.measure([0, 1], [0, 1])
    
    return qc
