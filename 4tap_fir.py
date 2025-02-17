import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# FIR filter coefficients
coeffs = [0.1321, 0.3679, 0.3679, 0.1321]

# Compute frequency response
w, h = freqz(coeffs, worN=1024)

# Convert to frequency (normalized to Nyquist frequency)
freqs = w / np.pi  

# Plot magnitude response
plt.figure(figsize=(8, 4))
plt.plot(freqs, 20 * np.log10(abs(h)), label="Magnitude Response")
plt.xlabel("Normalized Frequency (x π rad/sample)")
plt.ylabel("Magnitude (dB)")
plt.title("Frequency Response of 4-Tap FIR Filter")
plt.grid()
plt.legend()
plt.show()
