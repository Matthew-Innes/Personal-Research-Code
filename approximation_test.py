

import torch
import crypten
import matplotlib.pyplot as plt
'''
# Initialize CrypTen
crypten.init()

# Function to calculate exp(x) using PyTorch
def pytorch_exp(x):
    return x.exp()

# Function to calculate exp(x) using CrypTen
def crypten_exp(x):
    return x.exp()

# Define the range
range_start = -10
range_end = 10

# Calculate x values for PyTorch
x_values = torch.linspace(range_start, range_end, 1000)

# Calculate exp(x) using PyTorch (actual)
pytorch_results = pytorch_exp(x_values)

# Encrypt the input values for CrypTen
x_encrypted = crypten.cryptensor(x_values)

# Calculate exp(x) using CrypTen (approximation)
crypten_results_encrypted = crypten_exp(x_encrypted)

# Decrypt the results from CrypTen
crypten_results_decrypted = crypten_results_encrypted.get_plain_text()

# Plot the results without normalization
plt.figure(figsize=(12, 8))

# Plot PyTorch (actual) results
plt.plot(x_values.numpy(), pytorch_results.numpy(), label='actual (PyTorch)', color='blue')

# Plot CrypTen (approximation) results
plt.plot(x_values.numpy(), crypten_results_decrypted.numpy(), label='approximation (CrypTen)', color='orange')

plt.title('Comparison of exp(x) using PyTorch and CrypTen')
plt.xlabel('x')
plt.ylabel('exp(x)')
plt.legend()
plt.grid(True)
plt.show()
'''
# Initialize CrypTen
crypten.init()

# Function to calculate exp(x) using PyTorch
def pytorch_exp(x):
    return x.exp()

# Function to calculate exp(x) using CrypTen
def crypten_exp(x):
    return x.exp()

def plot_comparison_around_x(input_x):
    # Define the range from 0 to the input_x
    range_start = 0
    range_end = input_x

    # Calculate x values for PyTorch
    x_values = torch.linspace(range_start, range_end, 1000)

    # Calculate exp(x) using PyTorch (actual)
    pytorch_results = pytorch_exp(x_values)

    # Encrypt the input values for CrypTen
    x_encrypted = crypten.cryptensor(x_values)

    # Calculate exp(x) using CrypTen (approximation)
    crypten_results_encrypted = crypten_exp(x_encrypted)

    # Decrypt the results from CrypTen
    crypten_results_decrypted = crypten_results_encrypted.get_plain_text()

    # Determine if y-axis values exceed threshold
    max_crypten = crypten_results_decrypted.max().item()
    max_pytorch = pytorch_results.max().item()
    '''
    if max_crypten > 1e8 or max_pytorch > 1e8:
        plt.figure(figsize=(20, 20))  # Set plot size to 20x20
        plt.yscale('log')  # Set y-axis scale to log
    else:
        plt.figure(figsize=(20, 20))  # Set plot size to 20x20
    '''

    # Plot PyTorch (actual) results
   # plt.plot(x_values.numpy(), pytorch_results.numpy(), label='actual (PyTorch)', color='blue')

    # Plot CrypTen (approximation) results
    plt.plot(x_values.numpy(), crypten_results_decrypted.numpy(), label='approximation (CrypTen)', color='orange')

    plt.title('Comparison of exp(x) from 0 to input x={} using PyTorch and CrypTen'.format(input_x))
    plt.xlabel('x')
    plt.ylabel('exp(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Input x-value from the user
input_x = float(input("Enter the x-value up to which you want to compare (as a float): "))
plot_comparison_around_x(input_x)