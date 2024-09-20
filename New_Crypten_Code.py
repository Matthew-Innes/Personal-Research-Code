import crypten
import torch
import numpy as np
import matplotlib.pyplot as plt

# Initialize CrypTen
crypten.init()

# Define the range of values from -1000 to 1000
x_values = np.linspace(-1000, 1000, 100)

# Convert x_values to tensors for PyTorch and CrypTen
x_torch = torch.tensor(x_values, dtype=torch.float32)

# Compute the actual exp() using PyTorch
y_torch_exp = torch.exp(x_torch)

# Compute exp() using CrypTen
x_crypten = crypten.cryptensor(x_torch)
y_crypten_exp = x_crypten.exp().get_plain_text()

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_torch_exp.numpy(), label='PyTorch exp()', color='blue')
plt.plot(x_values, y_crypten_exp.numpy(), label='CrypTen exp() approximation', linestyle='--', color='red')
plt.title('Comparison of PyTorch exp() and CrypTen exp() Approximation (Range -1000 to 1000)')
plt.xlabel('Input')
plt.ylabel('Exp(x)')
plt.yscale('log')  # Logarithmic scale to capture large and small values
plt.legend()
plt.grid(True)
plt.show()