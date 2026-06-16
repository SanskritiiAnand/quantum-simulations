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
