import matplotlib.pyplot as plt
from src.circuits import create_bell_state_circuit, save_or_show_circuit_layout
from src.execution import run_primitive_sampler
from src.utils import plot_simulation_results

def main():
    print("Initializing quantum entanglement workspace...")
    
    # 1. Build the circuit architecture
    bell_circuit = create_bell_state_circuit()
    print(bell_circuit) # Prints text layout directly to terminal
    
    # 2. Trigger the Matplotlib circuit layout visualizer
    print("Rendering graphical circuit layout...")
    circuit_diagram = save_or_show_circuit_layout(bell_circuit)
    plt.show(block=True)
    
    # 3. Execute using your new primitive sampler engine (4000 shots)
    print("Executing circuit using StatevectorSampler...")
    counts = run_primitive_sampler(bell_circuit, total_shots=4000)
    print(f"Sampling complete! Counts: {counts}")
    
    # 4. Generate histogram
    print("Generating probability histogram...")
    plot_simulation_results(counts, title="Bell State Counts (StatevectorSampler)")

if __name__ == "__main__":
    main()
