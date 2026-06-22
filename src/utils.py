from qiskit.visualization import plot_histogram, plot_state_qsphere
from matplotlib import pyplot as plt

def plot_simulation_results(counts: dict, title: str = "Simulation Results"):
    """
    Plots a histogram of the quantum simulation counts using Matplotlib.
    """
    fig = plot_histogram(counts, title=title)
    plt.show(block=True)

def plot_teleportation_memory(measurements: list, target_bit_index: int = 2):
    """
    Extracts a targeted bit index from shot memory strings and plots a 
    dual-bin histogram verifying successful quantum teleportation.
    """
    #Parse out Bob's target bit from the overall returned data stream
    #Note: Qiskit registers bitstrings right-to-left, index inversion matched
    bit_data = [int(shot[2 - target_bit_index]) for shot in measurements]
    
    plt.figure()
    plt.hist(bit_data, bins=2, edgecolor="r", rwidth=0.85, align='left', range=[0, 2])
    plt.title("Verified Teleported State (Bob's Final Register)")
    plt.xlabel("State Value")
    plt.ylabel("Occurrences")
    plt.xticks([0, 1])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show(block=True)

def plot_qsphere_visualization(statevector, title: str = "Quantum State Vector Profile"):
    """
    Renders a 3D QSphere layout displaying state probabilities and phases.
    """
    fig = plot_state_qsphere(statevector, show_state_labels=True)
    fig.suptitle(title, fontsize=12, y=0.98)
    plt.show(block=True)

def plot_final_verification_counts(counts: dict, title: str = "Verification Counts"):
    """
    Plots a traditional Qiskit multi-bar probability histogram for final counts.
    """
    fig = plot_histogram(counts, title=title)
    plt.show(block=True)
