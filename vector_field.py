"""
Function: velocity_field, mesh_generation
Description: Computes the 2D velocity vector field around the airfoil by 
             representing the chord as a distributed vortex sheet.
Inputs:
    - x_grid, y_grid: Meshgrid coordinates for the flow domain
    - theta: Angular discretization of the chord
    - A0, A1, A2: Fourier coefficients
    - U: Freestream velocity magnitude
    - alpha_deg: Angle of attack in degrees
Outputs:
    - u, v: Horizontal and vertical velocity components at each grid point
    - V_mag: Resultant velocity magnitude
Assumptions:
    - Discrete vortex segments represent the continuous vortex sheet.
    - Biot-Savart law applies to each discrete segment.
"""
import numpy as np

def mesh_generation():
    # Defines the 4c x 3c domain grid for plotting the velocity field
    x = np.linspace(-1.5, 2.5, 40) # 4c width
    y = np.linspace(-1.0, 2.0, 30) # 3c height
    return np.meshgrid(x, y)

def velocity_field(x_grid, y_grid, theta, A0, A1, A2, U, alpha_deg):
    alpha = np.deg2rad(alpha_deg) # AoA in radians
    
    # Chord discretization into vortex segments
    theta_v = 0.5 * (theta[:-1] + theta[1:]) # Midpoint sampling to avoid singularities
    x_v = 0.5 * (1 - np.cos(theta_v)) # Chordwise location of each vortex segment
    dx_v = np.diff(0.5 * (1 - np.cos(theta))) # Width of each vortex segment

    # Glauert expansion for circulation strength gamma(theta)
    gamma = 2 * U * (((A0 * (1 + np.cos(theta_v))) / np.sin(theta_v)) + 
                     (A1 * np.sin(theta_v)) + (A2 * np.sin(2 * theta_v)))

    u_ind = np.zeros_like(x_grid) # Horizontal induced velocity array
    v_ind = np.zeros_like(y_grid) # Vertical induced velocity array
    eps = 1e-6 # Small number to prevent division by zero at vortex location

    # Nested summation of induced velocities from each chord segment k
    for k in range(len(x_v)):
        dx = x_grid - x_v[k] # Distance from vortex k along x
        rsq = dx**2 + y_grid**2 + eps # Squared distance to grid point
        
        # Clockwise vortex induces positive u above and negative u below
        u_ind += (gamma[k] / (2 * np.pi)) * (y_grid / rsq) * dx_v[k]
        v_ind += -(gamma[k] / (2 * np.pi)) * (dx / rsq) * dx_v[k]

    # Combine freestream and induced components
    u = U * np.cos(alpha) + u_ind # Total horizontal velocity
    v = U * np.sin(alpha) + v_ind # Total vertical velocity
    V_mag = np.sqrt(u**2 + v**2) # Total velocity magnitude

    return u, v, V_mag, gamma, x_v



def calculate_pressure_distribution(U, gamma):
    """
    Calculates Cp on the surfaces using Thin Airfoil Theory linearized Bernoulli.
    Cp_upper = -gamma/U (Suction side)
    Cp_lower = +gamma/U (Pressure side)
    """
    # Linearized Cp assumes small perturbations
    cp_upper = -gamma / U
    cp_lower = gamma / U
    
    return cp_upper, cp_lower