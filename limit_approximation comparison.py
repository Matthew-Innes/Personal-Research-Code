import math

def exp_limit_approximation(x, n=1000000):
    """
    Approximates the exponential function using the limit definition.
    
    e^x = lim (n -> infinity) (1 + x/n)^n
    
    Args:
        x (float): The exponent.
        n (int): The number of terms used in the approximation (default: 1e6).
    
    Returns:
        float: Approximation of e^x.
    """
    try:
        return (1 + x / n) ** n
    except OverflowError:
        return float('inf')  # Return infinity if overflow occurs

# Expand the range of x values for comparison
x_values = [-1000, 0, 1000]  # Reduced values to avoid overflow

# Calculate the limit approximation and standard math.exp() values
approximations = [exp_limit_approximation(x) for x in x_values]
standard_exp = [math.exp(x) if x <= 700 else float('inf') for x in x_values]  # math.exp() overflows for large x

# Compare the results
print(f"{'x':>8} | {'Limit Approximation':>20} | {'Standard exp()':>15} | {'Difference':>15}")
print('-' * 65)
for x, approx, std_exp in zip(x_values, approximations, standard_exp):
    difference = abs(approx - std_exp)
    print(f"{x:>8} | {approx:>20.10f} | {std_exp:>15.10f} | {difference:>15.10f}")
