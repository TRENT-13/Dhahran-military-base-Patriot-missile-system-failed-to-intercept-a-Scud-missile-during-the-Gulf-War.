# Dhahran-military-base-Patriot-missile-system-failed-to-intercept-a-Scud-missile-during-the-Gulf-War.



Patriot Missile System Error Simulation
Overview
This Python script simulates and analyzes the floating-point arithmetic error that contributed to the failure of the Patriot missile defense system during the 1991 Gulf War, specifically the Dhahran incident. The code demonstrates how small errors in floating-point representation can accumulate over time, leading to significant positional errors in high-speed missile tracking. Additionally, it illustrates the concept of catastrophic cancellation in trajectory calculations, another critical issue in missile guidance systems.
Features

Simulates the Patriot missile system's timing error due to 24-bit floating-point representation of the clock rate (0.1 seconds).
Calculates cumulative timing and positional errors over various operational durations.
Visualizes error growth using Matplotlib.
Analyzes the Dhahran incident (100 hours of operation) and compares the error to the critical interception window.
Demonstrates catastrophic cancellation in trajectory calculations using 32-bit and 64-bit floating-point precision.

Requirements

Python 3.x
Required libraries:
numpy
matplotlib
tabulate
decimal



Install the dependencies using:
pip install numpy matplotlib tabulate

Usage

Save the script as patriot_simulation.py.
Ensure all required libraries are installed.
Run the script:python patriot_simulation.py


The script will:
Display the binary representation of the clock rate (0.1 seconds) in 24-bit precision.
Show a table of error accumulation for different operational durations (0 to 100 hours).
Generate a plot of position error growth over time.
Provide a detailed analysis of the Dhahran incident, including the time and position errors after 100 hours.
Compare the error to the critical interception window.
Demonstrate catastrophic cancellation in trajectory calculations with 32-bit and 64-bit precision.



Key Components
PatriotSystemSimulation Class

Initialization: Sets high precision for true calculations using decimal, defines the clock rate (0.1 seconds), Scud missile speed (1676 m/s), and system precision (24 bits).
binary_representation: Converts a decimal number to its binary representation with a specified number of bits.
truncated_binary_to_decimal: Converts a truncated binary representation back to a decimal value.
calculate_timing_error: Computes the cumulative timing and positional errors for a given number of operational hours.
demonstrate_error: Runs the full analysis, including binary representation, error tables, and the Dhahran incident analysis.
plot_error_growth: Generates a plot of position error growth over time.

demonstrate_catastrophic_cancellation Function

Simulates trajectory calculations using 32-bit and 64-bit floating-point precision.
Demonstrates precision loss due to subtracting nearly equal numbers, a common issue in missile guidance systems.

Output
The script produces:

A console output with:
Binary representation of the clock rate.
A table showing time and position errors for various operational durations.
Detailed analysis of the Dhahran incident.
A table demonstrating catastrophic cancellation effects.


A Matplotlib plot visualizing the growth of position errors over time.

Background
The Patriot missile system failure in Dhahran, Saudi Arabia, in 1991 was caused by a floating-point arithmetic error. The system's internal clock used a 24-bit representation of 0.1 seconds, which introduced a small error per clock tick. After 100 hours of continuous operation, this error accumulated, causing a positional error large enough to miss an incoming Scud missile, resulting in 28 deaths and numerous injuries. This script simulates this error and highlights the importance of floating-point precision in critical systems.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Author
This simulation was created to educate users about floating-point arithmetic errors in critical systems.
