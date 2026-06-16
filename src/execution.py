from qiskit import transpile, QuantumCircuit
from qiskit_aer import AerSimulator

def run_local_simulation(circuit: QuantumCircuit, shots: int = 4096) -> dict:
    """
    Takes any quantum circuit, transpiles it for the AerSimulator, 
    runs it, and returns the resulting measurement counts.
    """
    # Use Aer simulator (exactly from your test_qiskit.py)
    sim = AerSimulator()
    tqc = transpile(circuit, sim)
    
    # Run simulation with custom no. of shots
    job = sim.run(tqc, shots=shots)
    result = job.result()
    
    # Get and return counts
    counts = result.get_counts(tqc)
    return counts


from qiskit.primitives import StatevectorSampler

def run_local_simulation(circuit: QuantumCircuit, shots: int = 4096) -> dict:
    """Runs the circuit using the AerSimulator backend."""
    sim = AerSimulator()
    tqc = transpile(circuit, sim)
    job = sim.run(tqc, shots=shots)
    return job.result().get_counts(tqc)

def run_primitive_sampler(circuit: QuantumCircuit, total_shots: int = 4000) -> dict:
    """
    Runs the circuit using the modern Qiskit StatevectorSampler primitive.
    """
    sampler = StatevectorSampler()
    job = sampler.run([circuit], shots=total_shots)
    result = job.result()
    
    # Extract counts from the primitive result data stream dynamically
    # Works seamlessly across both implicit and explicit classical registers
    data_pub = result[0].data
    register_name = list(data_pub.keys())[0] 
    return data_pub[register_name].get_counts()


def run_simulation_with_memory(circuit: QuantumCircuit, shots: int = 1024) -> list:
    """
    Executes a circuit on the AerSimulator and tracks individual shot data sequences 
    by setting memory=True. Returns the raw bitstring list array.
    """
    sim = AerSimulator()
    # Transpilation handles conditional dynamic if_test architectures flawlessly
    tqc = transpile(circuit, sim)
    
    job = sim.run(tqc, shots=shots, memory=True)
    result = job.result()
    return result.get_memory()


from qiskit.quantum_info import Statevector

def extract_circuit_statevector(circuit: QuantumCircuit) -> Statevector:
    """
    Clones the target circuit framework, appends a statevector save command, 
    and simulates it locally to return the full uncollapsed quantum statevector.
    """
    qc_snapshot = circuit.copy()
    qc_snapshot.save_statevector()
    
    sim = AerSimulator()
    # Transpile ensuring conditional elements are optimized for backend matrix execution
    tqc = transpile(qc_snapshot, sim)
    result = sim.run(tqc).result()
    return result.get_statevector()
