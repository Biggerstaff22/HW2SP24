import math

#I asked ChatGPT to help me with this code. This is what it shot back to me.
#I asked ChatGPT to explain each step to me so that I could truly learn why
#it coded it this way.

def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    Use the Secant Method to find the root of fcn(x) in the neighborhood of x0 and x1.

    Parameters:
    - fcn: The function for which we want to find the root.
    - x0, x1: Two x values in the neighborhood of the root.
    - xtol: Exit if |xnewest - xprevious| < xtol.
    - maxiter: Exit if the number of iterations (new x values) equals this number.

    Returns:
    - The final estimate of the root (most recent new x value).
    """
    x_previous = x0
    x_current = x1

    for iteration in range(maxiter):
        f_x_previous = fcn(x_previous)
        f_x_current = fcn(x_current)

        # Calculate the new estimate using the Secant Method
        x_new = x_current - f_x_current * (x_current - x_previous) / (f_x_current - f_x_previous)

        # Check for convergence
        if abs(x_new - x_current) < xtol:
            return x_new

        # Update values for the next iteration
        x_previous = x_current
        x_current = x_new

    return x_current


def main():
    # Test cases
    solution_1 = Secant(lambda x: x - 3*math.cos(x), 1, 2, maxiter=5, xtol=1e-4)
    solution_2 = Secant(lambda x: math.cos(2*x) * x**3, 1, 2, maxiter=15, xtol=1e-8)
    solution_3 = Secant(lambda x: math.cos(2*x) * x**3, 1, 2, maxiter=3, xtol=1e-8)

    print(f"Solution 1: {solution_1:.6f}")
    print(f"Solution 2: {solution_2:.6f}")
    print(f"Solution 3: {solution_3:.6f}")


# Run the main function
if __name__ == "__main__":
    main()
