import numpy as np
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
from tabulate import tabulate

"""PATRIOT SYSTEM CASE Floating point arithmetic error"""

class PatriotSystemSimulation:
    def __init__(self):
        # Set high precision for "true" calculations
        getcontext().prec = 28

        # Clock rate in tenths of seconds (0.1 seconds)
        self.CLOCK_RATE = Decimal('0.1')

        # Speed of Scud missile (approximately 1676 meters per second)
        self.SCUD_SPEED = 1676.0

        # 24-bit precision for the system's timing
        self.SYSTEM_PRECISION = 24

    def binary_representation(self, decimal_num, bits=24):
        """Convert decimal to binary representation with specified bits"""
        binary = ""
        num = float(decimal_num)
        for _ in range(bits):
            num *= 2
            if num >= 1:
                binary += "1"
                num -= 1
            else:
                binary += "0"
        return binary

    def truncated_binary_to_decimal(self, binary):
        """Convert truncated binary back to decimal"""
        decimal = 0
        for i, bit in enumerate(binary):
            if bit == '1':
                decimal += 2 ** -(i + 1)
        return decimal

    def calculate_timing_error(self, hours):
        """Calculate cumulative timing error after given hours of operation"""
        # True time in tenths of seconds
        true_time = hours * 3600 * 10  # Convert hours to tenths of seconds

        # Get binary representation of 0.1 (clock rate)
        clock_binary = self.binary_representation(self.CLOCK_RATE)
        truncated_clock = self.truncated_binary_to_decimal(clock_binary)

        # Calculate accumulated error
        error_per_tick = float(self.CLOCK_RATE) - truncated_clock
        total_error = error_per_tick * true_time

        # Calculate position error based on Scud speed
        position_error = total_error * self.SCUD_SPEED

        return {
            'hours': hours,
            'true_time': float(true_time),
            'error_per_tick': error_per_tick,
            'accumulated_error': total_error,
            'position_error': position_error
        }

    def demonstrate_error(self):
        """Demonstrate the error accumulation over time"""
        print("\nPatriot Missile System Error Analysis")
        print("====================================")

        # Show binary representation of 0.1
        clock_binary = self.binary_representation(self.CLOCK_RATE)
        print(f"\nBinary representation of 0.1 seconds (24 bits):")
        print(f"0.{clock_binary}")

        # Calculate and display errors for different operational durations
        hours_list = [0, 8, 16, 24, 48, 72, 100]
        results = []

        for hours in hours_list:
            error_data = self.calculate_timing_error(hours)
            results.append([
                error_data['hours'],
                error_data['accumulated_error'],
                error_data['position_error']
            ])

        print("\nError Accumulation Analysis:")
        print(tabulate(results,
                       headers=['Hours of Operation', 'Time Error (seconds)',
                                'Position Error (meters)'],
                       floatfmt=".6f"))

        # Visualize error growth
        self.plot_error_growth()

        # Specific analysis for the Dhahran incident (100 hours)
        dhahran_error = self.calculate_timing_error(100)

        print("\nDhahran Incident Analysis (after 100 hours of operation):")
        print(f"Time error: {dhahran_error['accumulated_error']:.6f} seconds")
        print(f"Position error: {dhahran_error['position_error']:.2f} meters")

        # Calculate critical threshold
        critical_distance = 20  # meters (approximate size of target)
        critical_time = critical_distance / self.SCUD_SPEED
        print(f"\nCritical Analysis:")
        print(f"Time window for successful interception: ±{critical_time:.6f} seconds")
        print(f"Actual error exceeded this by: {abs(dhahran_error['accumulated_error'] / critical_time):.1f}x")

    def plot_error_growth(self):
        """Plot error growth over time"""
        hours = np.linspace(0, 100, 100)
        position_errors = [self.calculate_timing_error(h)['position_error']
                           for h in hours]

        plt.figure(figsize=(10, 6))
        plt.plot(hours, position_errors, 'r-', label='Position Error')
        plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        plt.grid(True, alpha=0.3)
        plt.xlabel('Hours of Operation')
        plt.ylabel('Position Error (meters)')
        plt.title('Patriot System Position Error Growth Over Time')
        plt.legend()
        return plt


def demonstrate_catastrophic_cancellation():
    """
    Demonstrate how subtracting nearly equal numbers can lead to catastrophic
    precision loss - another critical issue in missile guidance systems
    """
    print("\nCatastrophic Cancellation in Trajectory Calculations")
    print("================================================")

    # Simulate trajectory calculations with different precisions
    target_distance = 1000000.0  # 1000 km in meters
    results = []

    for precision in [32, 64]:
        # Calculate trajectory components with limited precision
        if precision == 32:
            x = np.float32(target_distance)
            dx = np.float32(0.01)  # Small adjustment
        else:
            x = np.float64(target_distance)
            dx = np.float64(0.01)

        # Two different ways to calculate the same thing
        direct = x + dx - x
        indirect = dx

        results.append([
            precision,
            float(direct),
            float(indirect),
            abs(direct - indirect),
            abs(direct - indirect) / dx * 100
        ])

    print("\nPrecision Loss Analysis:")
    print(tabulate(results,
                   headers=['Bits', 'Direct Result', 'Indirect Result',
                            'Absolute Error', 'Relative Error (%)'],
                   floatfmt=".10f"))


if __name__ == "__main__":
    # Demonstrate Patriot missile system error
    simulator = PatriotSystemSimulation()
    simulator.demonstrate_error()
    simulator.plot_error_growth()

    # Demonstrate catastrophic cancellation
    demonstrate_catastrophic_cancellation()


