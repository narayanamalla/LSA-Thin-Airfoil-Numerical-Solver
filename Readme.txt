
AE 244: Assignment 2 – Thin Airfoil Theory Solver

---

1. Project Overview

This project provides an analytical tool for two-dimensional aerodynamic analysis based on Thin Airfoil Theory (TAT). Developed for the AE 244 course, the solver replaces the physical airfoil geometry with a continuous vortex sheet distributed along its mean camber line.

The implementation enables:

• Rapid computation of lift and moment coefficients
• Visualization of the local velocity field over a **4c × 3c domain**
• Verification of total circulation through a numerical **line-integral approach**

The entire system is executed through a Jupyter Notebook interface, where users run cells sequentially to perform the analysis and generate plots.

---

2. System Architecture & Modules

The project is divided into specialized modules orchestrated by a central Jupyter Notebook.

main.ipynb
The primary interface for the user. It collects inputs, controls the workflow, calls all modules, and displays the computed results and visualizations.

camber.py
Computes the geometric coordinates of the mean camber line and determines the local surface gradient (dyc/dx).

fourier.py
Solves for the Glauert Fourier coefficients (A0, A1, A2) using numerical trapezoidal integration.

velocity_field.py
Computes the velocity vector field (u, v) around the airfoil by superimposing the freestream velocity with the induced velocity from discrete vortex segments distributed along the chord.

circulation.py
Performs a numerical line integral around the airfoil to verify that the total circulation matches theoretical predictions.

plotting.py
Provides the visualization utilities required for plotting camber lines, camber slopes, and velocity vector fields.

---

3. Operational Instructions

Preparation

Ensure that the following files are located in the same working directory:

main.ipynb
camber.py
fourier.py
velocity_field.py
circulation.py
plotting.py

Execution

Open main.ipynb using a Jupyter environment such as:

• Jupyter Notebook
• JupyterLab
• Visual Studio Code

Run the notebook **cell by cell in sequence from top to bottom**.

Input Section

In Cell 3A of the notebook**, the user will be prompted to provide the required input parameters:

• NACA Number (example: 2412)
• Angle of Attack (α) in degrees
• Freestream Velocity (U) in meters per second

For Noval fucntion I have added my own functions in that, and when you select 3 and if you enter your NACA specification it'll generate the plots of camber line in comparision with input NACA number given by the user, You can edit the fucntions in the Novel Camber line fucntion and for custom functions (more than 2 to 3)

Result Visualization

After the inputs are provided, the notebook will automatically generate the results and plots in the subsequent cells, including:

• Camber line plot
• Camber slope distribution
• Fourier coefficient calculations
• Circulation distribution plot
• Velocity vector field around the airfoil

---

4. Design Customization

Modifying the Custom Airfoil

To test a specific mathematical camber shape, edit the function:

custom_airfoil(x)

inside camber.py.

The solver automatically recomputes the required slopes using the built-in numerical derivative tool.

Adjusting Novel Designs

To experiment with alternative camber geometries for Section 4 comparison tasks, modify the function:

Noval_camber_functions(x)

inside camber.py.

Re-run the notebook to observe how these geometric changes affect the lift and moment coefficients.

---

5. Technical Specifications & Assumptions

Chord Normalization

The solver assumes a normalized chord length:

c = 1.0

All internal aerodynamic calculations are performed using this normalized coordinate system.

Numerical Stability

To prevent singularities near the leading edge, the solver uses:

• Cosine spacing for chordwise discretization
• Midpoint sampling for vortex segment placement

Visualization Domain

The velocity field is evaluated and displayed over a computational domain of:

4c in the streamwise direction
3c in the vertical direction

Sign Convention

A positive angle of attack (α) corresponds to positive lift generation.

---

6. Credits

The aerodynamic theory and mathematical derivations implemented in this solver are based on classical **Thin Airfoil Theory** and lecture material from the AE 244 course curriculum.


