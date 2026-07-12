# AE 244 – Assignment 2: Thin Airfoil Theory Solver

## Overview

This project is an analytical implementation of **Thin Airfoil Theory (TAT)** for the aerodynamic analysis of two-dimensional airfoils. Developed as part of **AE 244**, the solver models the airfoil using a continuous vortex sheet distributed along its mean camber line, allowing rapid computation of aerodynamic characteristics without solving the full flow field numerically.

The project is implemented entirely in **Python** and executed through a **Jupyter Notebook**, providing an interactive workflow for analysis and visualization.

---

## Features

- Compute lift coefficient using Thin Airfoil Theory
- Compute quarter-chord moment coefficient
- Calculate Glauert Fourier coefficients (A₀, A₁, A₂)
- Generate mean camber line and camber slope distributions
- Visualize the velocity vector field over a **4c × 3c** computational domain
- Numerically verify total circulation using a closed contour line integral
- Compare custom airfoil camber functions with standard NACA airfoils
- Support user-defined novel camber line functions

---

## Project Structure

```
.
├── main.ipynb              # Main notebook (user interface)
├── camber.py               # Camber line generation and slope calculations
├── fourier.py              # Fourier coefficient computations
├── velocity_field.py       # Velocity field calculations
├── circulation.py          # Circulation verification
├── plotting.py             # Plotting utilities
└── README.md
```

---

## Module Description

### `main.ipynb`

Acts as the primary user interface.

Responsibilities:

- Accept user inputs
- Execute all computational modules
- Display numerical results
- Generate all plots

---

### `camber.py`

Responsible for airfoil geometry.

Functions include:

- Mean camber line generation
- Camber slope (`dyc/dx`) computation
- Numerical differentiation
- Custom airfoil definitions
- Novel camber line functions

---

### `fourier.py`

Computes the Glauert Fourier coefficients required in Thin Airfoil Theory.

Calculates:

- A₀
- A₁
- A₂

using numerical trapezoidal integration.

---

### `velocity_field.py`

Computes the velocity field by superimposing:

- Uniform freestream velocity
- Induced velocity from discrete vortex elements

Outputs:

- Velocity vectors
- Flow field visualization

---

### `circulation.py`

Performs numerical verification of circulation using a closed contour around the airfoil.

The computed circulation is compared against the theoretical value predicted by Thin Airfoil Theory.

---

### `plotting.py`

Contains plotting utilities for:

- Camber line
- Camber slope
- Velocity vector field
- Circulation distribution

---

# Installation

Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

Install the required packages

```bash
pip install numpy matplotlib scipy jupyter
```

Launch Jupyter Notebook

```bash
jupyter notebook
```

Open

```
main.ipynb
```

and run all cells sequentially.

---

# How to Run

Ensure the following files are present in the same working directory:

```
main.ipynb
camber.py
fourier.py
velocity_field.py
circulation.py
plotting.py
```

Run the notebook from top to bottom.

Recommended environments:

- Jupyter Notebook
- JupyterLab
- Visual Studio Code (Jupyter Extension)

---

# User Inputs

In **Cell 3A**, enter:

| Parameter | Example |
|-----------|---------|
| NACA Number | 2412 |
| Angle of Attack (degrees) | 5 |
| Freestream Velocity (m/s) | 20 |

---

# Novel Camber Function

The project also supports **user-defined camber geometries**.

When selecting the **Novel Function** option:

- Enter your desired NACA specification.
- The solver generates the corresponding camber line.
- It simultaneously plots the user-defined camber function for comparison.

This feature enables direct visual comparison between conventional NACA airfoils and custom-designed camber profiles.

The novel function can be modified inside:

```python
Noval_camber_functions(x)
```

located in

```
camber.py
```

You may add multiple custom functions (more than two or three if required) to investigate different aerodynamic characteristics.

---

# Creating a Custom Airfoil

To completely replace the NACA camber line with your own mathematical definition, edit:

```python
custom_airfoil(x)
```

inside

```
camber.py
```

The solver automatically:

- computes numerical derivatives,
- updates the Fourier coefficients,
- recalculates lift and moment coefficients,
- regenerates all plots.

---

# Output

Running the notebook generates:

- Mean camber line
- Camber slope distribution
- Fourier coefficient calculations
- Lift coefficient
- Quarter-chord moment coefficient
- Circulation verification
- Velocity vector field
- Novel airfoil comparison plots (if selected)

---

# Technical Specifications

## Chord Normalization

The solver assumes

```
c = 1.0
```

All calculations are performed using normalized coordinates.

---

## Numerical Stability

To improve numerical accuracy near the leading edge, the implementation uses:

- Cosine spacing for discretization
- Midpoint sampling of vortex segments

---

## Visualization Domain

Velocity vectors are evaluated over

- Streamwise direction: **4c**
- Vertical direction: **3c**

---

## Sign Convention

- Positive angle of attack produces positive lift.
- Counter-clockwise circulation is treated as positive.

---

# Numerical Methods

The solver employs:

- Thin Airfoil Theory
- Glauert Fourier Series Expansion
- Numerical trapezoidal integration
- Finite-difference differentiation
- Discrete vortex element superposition
- Numerical circulation line integration

---

# Example Workflow

1. Open `main.ipynb`.
2. Run all cells sequentially.
3. Enter:
   - NACA airfoil
   - Angle of attack
   - Freestream velocity
4. View:
   - Camber geometry
   - Fourier coefficients
   - Lift coefficient
   - Moment coefficient
   - Circulation verification
   - Velocity field
5. Modify custom or novel camber functions if desired.
6. Re-run the notebook to compare results.

---

# Assumptions

- Inviscid flow
- Incompressible flow
- Thin airfoil approximation
- Small angle of attack
- Infinite span (two-dimensional flow)
- Steady flow

---

# Course Information

**Course:** AE 244 – Aerodynamics

**Assignment:** Thin Airfoil Theory Solver

This project was developed for educational purposes to demonstrate the application of Thin Airfoil Theory and numerical methods in aerodynamic analysis.

---
```
