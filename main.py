# Import your custom modular blocks
from src.circuits import create_bell_state_circuit
from src.execution import run_local_simulation
from src.utils import plot_simulation_results

def main():
    print("Initializing quantum workspace...")
    
    # 1. Build the circuit using your logic
    bell_circuit = create_bell_state_circuit()
    print("Circuit successfully built.")
    
    # 2. Run the simulation using your execution engine
    print("Running simulation on local AerSimulator (4096 shots)...")
    counts = run_local_simulation(bell_circuit, shots=4096)
    print(f"Simulation complete! Counts: {counts}")
    
    # 3. Plot the results using your visualization tool
    print("Generating histogram...")
    plot_simulation_results(counts, title="Bell State Counts (Modular Workflow)")

if __name__ == "__main__":
    main()
