import sys
import matplotlib.pyplot as plt
from src.circuits import (create_bell_state_circuit, 
                          create_teleportation_circuit, 
                          create_labeled_teleportation_circuit,
                          create_deutsch_jozsa_circuit,
                          create_grover_search_circuit
                          creat_bernstein_vazirani_circuit,
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

def run_bernstein_vazirani_workflow():
    print("\n--- Starting Bernstein-Vazirani Algorithm Suite ---")
    
    user_input = input("Enter a binary string to hide (or press Enter for default '1001'): ").strip()
    hidden_str = user_input if user_input and all(c in '01' for c in user_input) else "1001"
    
    print(f"\nConstructing workspace for hidden parameter string: '{hidden_str}'...")
    bv_circuit = create_bernstein_vazirani_circuit(hidden_str)
    print(bv_circuit)
    
    print("Rendering circuit diagram architecture...")
    _ = save_or_show_circuit_layout(bv_circuit)
    plt.show(block=True)
    
    print(f"Executing circuit on AerSimulator engine (1024 shots)...")
    counts = run_local_simulation(bv_circuit, shots=1024)
    print(f"Executing counts array: {counts}")
    
    if hidden_str in counts and counts[hidden_str] == 1024:
        print(f"\n[ANALYSIS]: Final registration state is strictly |{hidden_str}>")
        print(">>>> SUCCESS: Hidden bitstring extracted perfectly in one single step.")
    else:
        print("\n[ANALYSIS]: Mismatch or statistical dispersion detected.")
        print(">>>> FAILURE")
        
    print("\nDisplaying measurement profile distribution...")
    plot_final_verification_counts(counts, title=f"Bernstein-Vazirani Output (Secret: {hidden_str})")

def run_grover_search_workflow():
    print("\n--- Starting Grover's Unstructured Search Suite ---")
    
    print("Select a 2-qubit binary target search space index:")
    print("Options: '00', '01', '10', or '11'")
    user_input = input("Enter target string (default '10'): ").strip()
    target_str = user_input if user_input in ["00", "01", "10", "11"] else "10"
    
    print(f"\nConstructing Grover workspace targeting state vector: |{target_str}>...")
    grover_circuit = create_grover_search_circuit(target_str)
    print(grover_circuit)
    
    print("Rendering circuit diagram architecture...")
    _ = save_or_show_circuit_layout(grover_circuit)
    plt.show(block=True)
    
    print(f"Executing circuit on AerSimulator engine (1024 shots)...")
    counts = run_local_simulation(grover_circuit, shots=1024)
    print(f"Readout Counts Result: {counts}")
    
    # Analysis Verification
    if target_str in counts and counts[target_str] == 1024:
        print(f"\n[ANALYSIS]: Target key state |{target_str}> amplified to maximum probability density.")
        print(">>>> SUCCESS: Grover's search successfully isolated the unindexed target item.")
    else:
        print(f"\n[ANALYSIS]: Non-deterministic convergence or state leakage detected.")
        print(">>>> FAILURE")
        
    print("\nDisplaying measurement profile distribution...")
    plot_final_verification_counts(counts, title=f"Grover Search Results (Target: {target_str})")

def main():
    print("====================================================")
    print("               Modular Quantum Engine               ")
    print("====================================================")
    print("Available experiments:")
    print("1: Run Quantum Entanglement Simulation (Bell State)")
    print("2: Run Quantum Teleportation Protocol (Shot Memory Analysis)")
    print("3: Run Quantum Teleportation Protocol (QSphere Phase Tracking)")
    print("4: Run Deutsch-Jozsa Quantum Speedup Verification")
    print("5: Run Bernstein-Vazirani Single-Query Target Capture")
    print("6: Run Grover's Search Algorithm (Amplitude Amplification Database)")
    print("====================================================")
    
    if len(sys.argv) > 1:
        choice = sys.argv[1].strip()
    else:
        choice = input("Select an option (1, 2, 3, 4, 5): ").strip()
        
    if choice == "1":
        run_entanglement_workflow()
    elif choice == "2":
        run_teleportation_workflow()
    elif choice == "3":
        run_qsphere_teleportation_workflow()
    elif choice == "4":
        run_deutsch_jozsa_workflow()
    elif choice == "5":
        run_bernstein_vazirani_workflow()
    elif choice == "6":
        run_grover_search_workflow()
    else:
        print(f"Invalid option '{choice}'. Please select '1', '2', '3', '4', '5', or '6'.")

if __name__ == "__main__":
    main()
