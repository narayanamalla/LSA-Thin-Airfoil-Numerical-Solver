"""
Function: camber_line and camber_slope
Description: Computes mean camber line coordinates and local gradients (dy/dx).
Inputs: choice (ID), m (Camber), p (Location), N (Discretization), c (Chord).
Outputs: x, yc, theta coordinates and slope arrays.
Assumptions: Small camber theory holds; LE at (0,0), TE at (1,0).
"""
import numpy as np

# Defines the shapes for the three novel airfoils for Section 4
def Noval_camber_funtions(x):
    # You can experiment with these novel shapes to see how they affect Cl and Cm.
    # Just make sure your math results in yc = 0 at both x = 0 and x = 1, 
    # otherwise the Thin Airfoil Theory math will break!
    yc1 = 0.2*x*(1-x)*(1-2*x)
    yc2 = 0.1*np.sin(np.pi*x)*(1-x)
    yc3 = 0.1*x*(1-x)**2
    return yc1, yc2, yc3

# User-definable custom function for standard custom runs
def custom_airfoil(x):
    y = 0.05 * np.sin(np.pi * (x)) 
    return y

# Uses central difference formula to calculate slope dy/dx
def numerical_derivative(x, id=1, h=1e-5):
    if id == 1:
        return (custom_airfoil(x+h) - custom_airfoil(x-h)) / (2 * h) # Derivative for choice 1
    else:
        # Derivative for comparison airfoils
        y1p, y2p, y3p = Noval_camber_funtions(x + h)
        y1m, y2m, y3m = Noval_camber_funtions(x - h)
        s1 = (y1p - y1m) / (2 * h) # Slope for Novel 1
        s2 = (y2p - y2m) / (2 * h) # Slope for Novel 2
        s3 = (y3p - y3m) / (2 * h) # Slope for Novel 3
        return s1, s2, s3

# Generates chordwise distribution and vertical coordinates
def camber_line(choice, m, p, N=1000, c=1.0):
    theta = np.linspace(0, np.pi, N) # Glauert transformation variable
    x = (c / 2) * (1 - np.cos(theta)) # Cosine spacing for better LE/TE resolution
    yc = np.zeros_like(x) # Initialized Array for vertical coordinates
    p_safe = max(p, 1e-6) # Prevents division by zero for symmetric airfoils

    if choice == 3:
        # Specialized logic for Section 4 multi-airfoil comparison
        y1, y2, y3 = np.zeros_like(x), np.zeros_like(x), np.zeros_like(x) #Initialized Array for vertical coordinates for Novel Airfoils
        for i in range(N):
            y1[i], y2[i], y3[i] = Noval_camber_funtions(x[i])
            # Reference NACA shape calculation
            if x[i] <= p_safe:
                yc[i] = (m/p_safe**2) * (2*p_safe*(x[i]/c) - (x[i]/c)**2)
            else:
                yc[i] = (m/(1-p_safe)**2) * ((1-2*p_safe) + 2*p_safe*(x[i]/c) - (x[i]/c)**2)
        return x, yc, theta, y1, y2, y3
    
    # Standard choice 1 or 2 logic for single airfoil analysis
    for i in range(N):
        if choice == 1:
            yc[i] = custom_airfoil(x[i]) # Calculating camber for custom aifoil 
        elif choice == 2:
            # Piecewise NACA 4-digit equations
            if x[i] <= p_safe:
                yc[i] = (m/p_safe**2) * (2*p_safe*(x[i]/c) - (x[i]/c)**2)
            else:
                yc[i] = (m/(1-p_safe)**2) * ((1-2*p_safe) + 2*p_safe*(x[i]/c) - (x[i]/c)**2)
    return x, yc, theta


# Calculates the gradient array required for Fourier coefficients
def camber_slope(choice, m, p, x):
    slope = np.zeros_like(x) #Initializing slope array 
    p_safe = max(p, 1e-6) # Singularity handling
    
    if choice == 3:
        s1, s2, s3 = np.zeros_like(x), np.zeros_like(x), np.zeros_like(x)  #Initializing slope arrays
        for i in range(len(x)):
            s1[i], s2[i], s3[i] = numerical_derivative(x[i], id=2) # calculating slopes using numerical derivative method
        return s1, s2, s3
    
    for i in range(len(x)):
        if choice == 1:
            slope[i] = numerical_derivative(x[i]) # Using numerical derivate method to calculate slope for custom airfoil
        else:
            # NACA funtion derivative
            if x[i] <= p_safe:
                slope[i] = (2 * m / p_safe**2) * (p_safe - x[i])
            else:
                slope[i] = (2 * m / (1 - p_safe)**2) * (p_safe - x[i])
    return slope