import sys
import matplotlib.pyplot as plt
from src.circuits import (create_bell_state_circuit, 
                          create_teleportation_circuit, 
                          create_labeled_teleportation_circuit,
                          create_deutsch_jozsa_circuit,
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
    _ = save_or_show_circuit_layout(bell_circuit)
    plt.show(block=True)
    counts = run_primitive_sampler(bell_circuit, total_shots=4000)
    plot_simulation_results(counts, title="Bell State Counts (StatevectorSampler)")

def run_teleportation_workflow():
    print("\n--- Starting Quantum Teleportation Workspace ---")
    teleport_circuit = create_teleportation_circuit()
    print(teleport_circuit)
    _ = save_or_show_circuit_layout(teleport_circuit)
    plt.show(block=True)
    shot_memory = run_simulation_with_memory(teleport_circuit, shots=1024)
    plot_teleportation_memory(shot_memory, target_bit_index=2)

def run_qsphere_teleportation_workflow():
    print("\n--- Starting Teleportation with QSphere Visualization ---")
    qc = create_labeled_teleportation_circuit()
    print(qc)
    sv = extract_circuit_statevector(qc)
    plot_qsphere_visualization(sv, title="Final 3-qubit Statevector Phase Space")
    qc.h(2)
    qc.measure(2, 2)
    counts = run_local_simulation(qc, shots=4096)
    plot_final_verification_counts(counts, title="Verification of Teleported State")

def run_deutsch_jozsa_workflow():
    print("\n--- Starting Deutsch-Jozsa Algorithm Suite ---")
    num_qubits = 3  
    
    print("\nSelect the Oracle function type to generate:")
    print("1: Constant Function")
    print("2: Balanced Function")
    oracle_choice = input("Enter choice (1 or 2): ").strip()
    
    mode = "constant" if oracle_choice == "1" else "balanced"
    
    print(f"\nConstructing {mode.upper()} algorithm workspace...")
    dj_circuit = create_deutsch_jozsa_circuit(num_qubits, mode=mode)
    print(dj_circuit)
    
    print("Rendering circuit diagram architecture...")
    _ = save_or_show_circuit_layout(dj_circuit)
    plt.show(block=True)
    
    print(f"Executing circuit on AerSimulator engine (1024 shots)...")
    counts = run_local_simulation(dj_circuit, shots=1024)
    print(f"Readout Counts Result: {counts}")
    
    constant_key = "0" * num_qubits
    if constant_key in counts and counts[constant_key] == 1024:
        print("\n[ANALYSIS RESULT]: Circuit output evaluated strictly to |000>.")
        print(">>> SUCCESS: The quantum engine deterministically proved the function is CONSTANT.")
    else:
        print("\n[ANALYSIS RESULT]: Circuit output evaluated strictly to non-zero states.")
        print(">>> SUCCESS: The quantum engine deterministically proved the function is BALANCED.")
        
    print("\nDisplaying measurement profile distribution...")
    plot_final_verification_counts(counts, title=f"Deutsch-Jozsa Output ({mode.capitalize()} Oracle)")

def main():
    print("====================================================")
    print("               Modular Quantum Engine               ")
    print("====================================================")
    print("Available experiments:")
    print("1: Run Quantum Entanglement Simulation (Bell State)")
    print("2: Run Quantum Teleportation Protocol (Shot Memory Analysis)")
    print("3: Run Quantum Teleportation Protocol (QSphere Phase Tracking)")
    print("4: Run Deutsch-Jozsa Quantum Speedup Verification")
    print("====================================================")
    
    if len(sys.argv) > 1:
        choice = sys.argv[1].strip()
    else:
        choice = input("Select an option (1, 2, 3, or 4): ").strip()
        
    if choice == "1":
        run_entanglement_workflow()
    elif choice == "2":
        run_teleportation_workflow()
    elif choice == "3":
        run_qsphere_teleportation_workflow()
    elif choice == "4":
        run_deutsch_jozsa_workflow()
    else:
        print(f"Invalid option '{choice}'. Please select '1', '2', '3', or '4'.")

if __name__ == "__main__":
    main()
