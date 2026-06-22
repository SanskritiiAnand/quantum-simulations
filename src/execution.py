from qiskit import transpile, QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import Statevector

def run_local_simulation(circuit: QuantumCircuit, shots: int = 4096) -> dict:
    """
    Takes any quantum circuit, transpiles it for the AerSimulator, 
    runs it, and returns the resulting measurement counts.
    """
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
    
    #Extract counts from the primitive result data stream dynamically
    data_pub = result[0].data
    register_name = list(data_pub.keys())[0] 
    return data_pub[register_name].get_counts()

def run_simulation_with_memory(circuit: QuantumCircuit, shots: int = 1024) -> list:
    """
    Executes a circuit on the AerSimulator and tracks individual shot data sequences 
    by setting memory=True. Returns the raw bitstring list array.
    """
    sim = AerSimulator()
    tqc = transpile(circuit, sim)
    job = sim.run(tqc, shots=shots, memory=True)
    return job.result().get_memory()

def extract_circuit_statevector(circuit: QuantumCircuit) -> Statevector:
    """
    Clones the target circuit framework, safely handles and strips any final measurement 
    operations, and returns the pure uncollapsed quantum statevector.
    """
    qc_snapshot = circuit.copy()
    if qc_snapshot.cregs:
        qc_snapshot.remove_final_measurements()
        
    return Statevector.from_instruction(qc_snapshot)
