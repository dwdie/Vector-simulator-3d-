import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def simulate_and_plot_vector():
    """
    Prompts the user for i, j, k components, creates a 3D vector,
    prints its details, and plots it in 3D space.
    """
    print("--- 3D Vector Simulation ---")
    print("Please enter the components of your 3D vector (i, j, k).")

    # Get user input for i, j, k components
    while True:
        try:
            i_component = float(input("Enter the i component (X-axis value): "))
            j_component = float(input("Enter the j component (Y-axis value): "))
            k_component = float(input("Enter the k component (Z-axis value): "))
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value for each component.")

    # Create the 3D vector using NumPy
    vector = np.array([i_component, j_component, k_component])

    print(f"\n--- Vector Details ---")
    print(f"Your vector V = {i_component}i + {j_component}j + {k_component}k")
    print(f"As a NumPy array: {vector}")
    print(f"Magnitude of the vector: {np.linalg.norm(vector):.2f}") # Calculate magnitude

    # --- Plotting the Vector in 3D ---
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Define the origin of the vector (starting point)
    origin = np.array([0, 0, 0])

    # Plot the vector using ax.quiver
    # U, V, W are the components of the vector starting from X, Y, Z
    ax.quiver(origin[0], origin[1], origin[2],  # Start points (X, Y, Z)
              vector[0], vector[1], vector[2],  # Components (U, V, W)
              color='blue', arrow_length_ratio=0.15, linewidth=2, label='Vector V')

    # Set axis labels
    ax.set_xlabel('X-axis (i)')
    ax.set_ylabel('Y-axis (j)')
    ax.set_zlabel('Z-axis (k)')
    ax.set_title('3D Vector Visualization')
    ax.legend()

    # Set dynamic limits for better visualization based on vector components
    # Add a buffer to the limits
    max_component = max(abs(i_component), abs(j_component), abs(k_component))
    plot_range = max(5, max_component + 1) # Ensure a minimum range of 5 units

    ax.set_xlim([-plot_range, plot_range])
    ax.set_ylim([-plot_range, plot_range])
    ax.set_zlim([-plot_range, plot_range])

    # Add grid
    ax.grid(True)

    # Show plot
    plt.show()

# Run the simulation
if __name__ == "__main__":
    simulate_and_plot_vector()