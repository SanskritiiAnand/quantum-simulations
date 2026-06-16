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
