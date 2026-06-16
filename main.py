import sys
import matplotlib.pyplot as plt
from src.circuits import (create_bell_state_circuit, 
                          create_teleportation_circuit, 
                          create_labeled_teleportation_circuit,
                          save_or_show_circuit_layout)
from src.execution import (run_primitive_sampler, 
                           run_simulation_with_memory, 
                           run_local_simulation,
                           extract_circuit_statevector)
from src.utils import (plot_simulation_results, 
                       plot_teleportation_memory,
                       plot_qsphere_visualization,
                       plot_final_verification_counts)

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

def run_qsphere_teleportation_workflow():
    print("\n--- Starting Teleportation with QSphere Visualization ---")
    qc = create_labeled_teleportation_circuit()
    print(qc)
    
    print("\n--- Extracting and Generating Q-sphere Statevector ---")
    sv = extract_circuit_statevector(qc)
    print("Displaying Q-sphere plotting matrix...")
    plot_qsphere_visualization(sv, title="Final 3-qubit Statevector Phase Space")
    
    print("\nExecuting terminal measurement rotations and finalizing sample shots (4096 shots)...")
    # Complete terminal verification rotation on the primary circuit before running counts
    qc.h(2)
    qc.measure(2, 2)
    
    counts = run_local_simulation(qc, shots=4096)
    print(f"Final Counts Array: {counts}")
    print("Displaying final registration validation histogram...")
    plot_final_verification_counts(counts, title="Verification of Teleported State")

def main():
    print("====================================================")
    print("      Welcome to the Modular Quantum Engine         ")
    print("====================================================")
    print("Available experiments:")
    print("1: Run Quantum Entanglement Simulation (Bell State)")
    print("2: Run Quantum Teleportation Protocol (Shot Memory Analysis)")
    print("3: Run Quantum Teleportation Protocol (QSphere Phase Tracking)")
    print("====================================================")
    
    if len(sys.argv) > 1:
        choice = sys.argv[1].strip()
    else:
        choice = input("Select an option (1, 2, or 3): ").strip()
        
    if choice == "1":
        run_entanglement_workflow()
    elif choice == "2":
        run_teleportation_workflow()
    elif choice == "3":
        run_qsphere_teleportation_workflow()
    else:
        print(f"Invalid option '{choice}'. Please select '1', '2', or '3'.")

if __name__ == "__main__":
    main()
