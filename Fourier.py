"""
Function: compute_fourier
Description: Solves for the Glauert Fourier coefficients (A0, A1, A2) using the 
             Thin Airfoil Theory fundamental equation and trapezoidal integration.
Inputs:
    - alpha: Angle of attack in degrees
    - theta: Angular coordinates (0 to pi)
    - slope: Camber line slope dyc/dx corresponding to theta
Outputs:
    - A0, A1, A2: First three Fourier coefficients
    - Cl: Lift Coefficient
    - Cm: Moment Coefficient about the quarter-chord
Assumptions:
    - Small angle approximation (sin alpha ~ alpha)
    - Kutta condition is satisfied at the trailing edge.
"""
import numpy as np

def compute_fourier(alpha, theta, slope):
    alpha_rad = np.deg2rad(alpha) # Convert input AoA to radians
    
    # Prevent numerical issues at endpoints (0 and pi)
    theta_safe = np.clip(theta, 1e-6, np.pi - 1e-6)

    # Perform numerical integration for Fourier Coefficients
    # A0 represents the angle of attack and mean slope effect
    A0 = alpha_rad - (1/np.pi) * np.trapezoid(slope, theta_safe)
    
    # A1 and A2 capture the camber shape distribution
    A1 = (2/np.pi) * np.trapezoid(slope * np.cos(theta_safe), theta_safe)
    A2 = (2/np.pi) * np.trapezoid(slope * np.cos(2 * theta_safe), theta_safe)

    # Final Aerodynamic Coefficients
    Cl = np.pi * (2 * A0 + A1) # Theoretical Lift Coefficient
    Cm = -(np.pi/2)*(A1-A2)# Theoretical Moment Coefficient (c/4)

    return A0, A1, A2, Cl, Cm   # Returns the values when the funtion is called