import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta, gamma, pi

# Define completed zeta function Λ(s, 1)
def Lambda(s):
    return zeta(s)

# Define the range of sigma (real part), fixed imaginary part t = 3
sigma_vals = np.linspace(-2, 3, 500)
t_val = 3.0
s_vals = [complex(sigma, t_val) for sigma in sigma_vals]
s_compl_vals = [complex(1 - sigma, t_val) for sigma in sigma_vals]

# Evaluate Λ(s,1) and Λ(1-s,1)
Lambda_vals = np.array([Lambda(s) for s in s_vals], dtype=np.complex128)
Lambda_comp_vals = np.array([Lambda(s) for s in s_compl_vals], dtype=np.complex128)

# Extract real and imaginary parts
real_Lambda = Lambda_vals.real
imag_Lambda = Lambda_vals.imag
real_Lambda_comp = Lambda_comp_vals.real
imag_Lambda_comp = -Lambda_comp_vals.imag

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# Real part
axs[0].plot(sigma_vals, real_Lambda, label=r'$\Lambda(s,1)$', color='blue')
axs[0].plot(sigma_vals, real_Lambda_comp, label=r'$\Lambda(1 - s,1)$', color='orange')
axs[0].axvline(x=0.5, linestyle='--', color='gray')
axs[0].set_title("Real")
axs[0].legend()
axs[0].grid(True)

# Imaginary part
axs[1].plot(sigma_vals, imag_Lambda, label=r'$\Lambda(s,1)$', color='blue')
axs[1].plot(sigma_vals, imag_Lambda_comp, label=r'$\Lambda(1 - s,1)$', color='orange')
axs[1].axvline(x=0.5, linestyle='--', color='gray')
axs[1].set_title("Imaginary")
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()
