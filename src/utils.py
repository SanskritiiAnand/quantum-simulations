from qiskit.visualization import plot_histogram
from matplotlib import pyplot as plt

def plot_simulation_results(counts: dict, title: str = "Simulation Results"):
    """
    Plots a histogram of the quantum simulation counts using Matplotlib.
    """
    fig = plot_histogram(counts, title=title)
    plt.show(block=True)
