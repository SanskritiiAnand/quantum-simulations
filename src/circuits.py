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
