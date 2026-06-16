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
---------------------------------------------------------------------------------------------------------------------------------------------------
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
--------------------------------------------------------------------------------------------------------------------------------------------------
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
