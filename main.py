import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from tabulate import tabulate


class FiniteDifferenceAnalyzer:
    def __init__(self):
        """Initialize the analyzer with some real-world functions"""
        # Temperature profile of a heat sink (1D)
        self.heat_profile = lambda x: 80 * np.exp(-0.1 * x) + 25

        # Atmospheric pressure distribution (2D)

        # Known derivatives for error calculation
        self.heat_profile_derivative = lambda x: -8 * np.exp(-0.1 * x)


    def forward_difference(self, f, x, h):
        """Forward difference approximation"""
        return (f(x + h) - f(x)) / h

    def central_difference(self, f, x, h):
        """Central difference approximation"""
        return (f(x + h) - f(x - h)) / (2 * h)

    def second_order_central(self, f, x, h):
        """Second-order central difference"""
        return (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)

    def analyze_1d_differences(self):
        """Analyze different finite difference methods in 1D"""
        print("\n1. Heat Sink Temperature Profile Analysis")
        print("=======================================")

        # Point of interest (distance from heat source in cm)
        x0 = 5.0
        h_values = [1.0, 0.5, 0.1, 0.05, 0.01]

        results = []
        for h in h_values:
            # Calculate approximations
            forward = self.forward_difference(self.heat_profile, x0, h)
            central = self.central_difference(self.heat_profile, x0, h)
            second = self.second_order_central(self.heat_profile, x0, h)

            # True derivative
            true_derivative = self.heat_profile_derivative(x0)

            # Calculate errors
            errors = {
                'forward': abs(forward - true_derivative),
                'central': abs(central - true_derivative),
                'second': abs(second - true_derivative)
            }

            results.append([
                h,
                forward,
                errors['forward'],
                central,
                errors['central'],
                second,
                errors['second']
            ])

        print("\nTemperature Gradient Approximation Analysis:")
        print(tabulate(results,
                       headers=['Step h', 'Forward', 'Forward Error',
                                'Central', 'Central Error',
                                '2nd Order', '2nd Order Error'],
                       floatfmt=".8f"))

        self.visualize_1d_errors(x0)

    def visualize_1d_errors(self, x0):
        """Visualize errors in 1D approximations"""
        h_range = np.logspace(-4, 0, 100)
        errors = {
            'Forward': [],
            'Central': [],
            'Second Order': []
        }

        true_val = self.heat_profile_derivative(x0)

        for h in h_range:
            errors['Forward'].append(abs(self.forward_difference(self.heat_profile, x0, h) - true_val))
            errors['Central'].append(abs(self.central_difference(self.heat_profile, x0, h) - true_val))
            errors['Second Order'].append(abs(self.second_order_central(self.heat_profile, x0, h) - true_val))

        plt.figure(figsize=(10, 6))
        for method, error in errors.items():
            plt.loglog(h_range, error, label=method)

        plt.grid(True)
        plt.xlabel('Step Size (h)')
        plt.ylabel('Absolute Error')
        plt.title('Error Convergence in Temperature Gradient Calculation')
        plt.legend()
        plt.show()



    def convergence_analysis(self):
        """Analyze convergence rates as h approaches zero"""
        print("\n3. Convergence Analysis")
        print("=====================")

        h_values = np.logspace(-6, 0, 20)
        x0 = 5.0

        # Calculate errors for different methods
        errors = {
            'Forward': [],
            'Central': [],
            'Second Order': []
        }

        true_val = self.heat_profile_derivative(x0)

        for h in h_values:
            errors['Forward'].append(
                abs(self.forward_difference(self.heat_profile, x0, h) - true_val))
            errors['Central'].append(
                abs(self.central_difference(self.heat_profile, x0, h) - true_val))
            errors['Second Order'].append(
                abs(self.second_order_central(self.heat_profile, x0, h) - true_val))

        # Calculate convergence rates
        convergence_rates = {}
        for method in errors:
            rates = np.diff(np.log(errors[method])) / np.diff(np.log(h_values))
            convergence_rates[method] = np.mean(rates[10:])  # Use last few points

        print("\nConvergence Rates Analysis:")
        for method, rate in convergence_rates.items():
            print(f"{method}: Order {abs(rate):.2f}")

        # Visualize convergence
        plt.figure(figsize=(10, 6))
        for method, error in errors.items():
            plt.loglog(h_values, error, 'o-', label=f"{method}")

        plt.grid(True)
        plt.xlabel('Step Size (h)')
        plt.ylabel('Absolute Error')
        plt.title('Convergence Analysis')
        plt.legend()
        plt.show()




if __name__ == "__main__":
    analyzer = FiniteDifferenceAnalyzer()

    # Run complete analysis
    analyzer.analyze_1d_differences()
    # analyzer.analyze_2d_differences()
    analyzer.convergence_analysis()