import math

#I asked ChatGPT to help me with this code. This is what it shot back to me.
#I asked ChatGPT to explain each step to me so that I could truly learn why,
#it coded it this way.

def Probability(PDF, args, c, GT=True):
    """
    Calculate the probability using Simpson's 1/3 rule.

    Parameters:
    - PDF: Callback function for the Gaussian/normal probability density function.
    - args: Tuple containing μ and σ.
    - c: Floating point value (upper limit of integration).
    - GT: Boolean indicating if we want the probability of x being greater than c (GT=True) or less than c (GT=False).

    Returns:
    - Probability value.
    """
    mu, sigma = args

    # Define the limits of integration
    lower_limit = mu - 5 * sigma
    upper_limit = c

    # Calculate the step size for Simpson's 1/3 rule
    step_size = (upper_limit - lower_limit) / 1000  # Using 1000 intervals for integration

    # Initialize the probability
    probability = 0

    # Apply Simpson's 1/3 rule
    for i in range(0, 1001, 2):
        x_i = lower_limit + i * step_size
        probability += PDF((x_i, mu, sigma)) + 4 * PDF((x_i + step_size, mu, sigma)) + PDF((x_i + 2 * step_size, mu, sigma))

    probability = probability * step_size / 3

    # If GT is False, calculate the probability of x<c
    if not GT:
        probability = 1 - probability

    return round(probability, 2)


def normal_pdf(values):
    """
    Gaussian/normal probability density function.

    Parameters:
    - values: Tuple containing x, μ, and σ.

    Returns:
    - Probability density function value.
    """
    x, mu, sigma = values
    exponent = -(x - mu) ** 2 / (2 * sigma ** 2)
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(exponent)


def main():
    # Find and print the probabilities
    prob_1 = Probability(normal_pdf, (100, 12.5), 105, GT=False)
    prob_2 = Probability(normal_pdf, (100, 3), 100 + 2 * 3, GT=True)

    print(f"P(x<105|N(100,12.5))={prob_1:.2f}")
    print(f"P(x>{100 + 2 * 3}|N(100,3))={prob_2:.2f}")


# Run the main function
if __name__ == "__main__":
    main()
