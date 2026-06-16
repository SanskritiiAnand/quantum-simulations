import matplotlib.pyplot as plt
from src.circuits import create_teleportation_circuit, save_or_show_circuit_layout
from src.execution import run_simulation_with_memory
from src.utils import plot_teleportation_memory

def main():
    print("Initializing Quantum Teleportation Workflow...")
    
    # 1. Structural compilation
    teleport_circuit = create_teleportation_circuit()
    print("\n--- Circuit Text Representation ---")
    print(teleport_circuit)
    
    # 2. Render graphical layout diagram
    print("\nRendering graphical architecture layout...")
    _ = save_or_show_circuit_layout(teleport_circuit)
    plt.show(block=True)
    
    # 3. Simulate and parse sequential bit strings
    print("\nRunning local simulation engine tracking raw memory (1024 shots)...")
    shot_memory = run_simulation_with_memory(teleport_circuit, shots=1024)
    print(f"First 10 sample raw shot strings: {shot_memory[:10]}")
    
    # 4. Filter and visualize Bob's teleported state data distribution
    print("\nExtracting and plotting Bob's teleported results...")
    plot_teleportation_memory(shot_memory, target_bit_index=2)
    print("Teleportation execution verified successfully!")

if __name__ == "__main__":
    main()
