import sys
import matplotlib.pyplot as plt
from src.circuits import create_bell_state_circuit, create_teleportation_circuit, save_or_show_circuit_layout
from src.execution import run_primitive_sampler, run_simulation_with_memory
from src.utils import plot_simulation_results, plot_teleportation_memory

def run_entanglement_workflow():
    print("\n--- Starting Quantum Entanglement Workspace ---")
    bell_circuit = create_bell_state_circuit()
    print(bell_circuit)
    
    print("Rendering circuit diagram...")
    _ = save_or_show_circuit_layout(bell_circuit)
    plt.show(block=True)
    
    print("Executing circuit using StatevectorSampler...")
    counts = run_primitive_sampler(bell_circuit, total_shots=4000)
    print(f"Sampling complete! Counts: {counts}")
    
    print("Generating probability histogram...")
    plot_simulation_results(counts, title="Bell State Counts (StatevectorSampler)")

def run_teleportation_workflow():
    print("\n--- Starting Quantum Teleportation Workspace ---")
    teleport_circuit = create_teleportation_circuit()
    print(teleport_circuit)
    
    print("Rendering circuit diagram...")
    _ = save_or_show_circuit_layout(teleport_circuit)
    plt.show(block=True)
    
    print("Running local simulation engine tracking raw memory (1024 shots)...")
    shot_memory = run_simulation_with_memory(teleport_circuit, shots=1024)
    print(f"First 10 sample raw shot strings: {shot_memory[:10]}")
    
    print("Extracting and plotting Bob's teleported results...")
    plot_teleportation_memory(shot_memory, target_bit_index=2)

def main():
    print("====================================================")
    print("      Welcome to the Modular Quantum Engine         ")
    print("====================================================")
    print("Available experiments:")
    print("1: Run Quantum Entanglement Simulation (Bell State)")
    print("2: Run Quantum Teleportation Protocol")
    print("====================================================")
    
    # Check if user passed a shortcut command argument, otherwise ask interactively
    if len(sys.argv) > 1:
        choice = sys.argv[1].strip()
    else:
        choice = input("Select an option (1 or 2): ").strip()
        
    if choice == "1":
        run_entanglement_workflow()
    elif choice == "2":
        run_teleportation_workflow()
    else:
        print(f"Invalid option '{choice}'. Please select '1' or '2'.")

if __name__ == "__main__":
    main()
