import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, filtfilt, freqz

# Sampling frequency
fs = 117.3491e6  # 117.3491 MHz

# Passband frequencies
lowcut = 30.5e6   # 30.5 MHz
highcut = 37.0e6  # 37.0 MHz

# Bandpass filter design function
def butter_bandpass(lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs  # Nyquist frequency
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band', analog=False)
    return b, a

# Get filter coefficients
b, a = butter_bandpass(lowcut, highcut, fs)

# Generate a test signal (mix of 25MHz, 33MHz, and 40MHz)
t = np.arange(0, 10e-6, 1/fs)  # 10 microseconds of data
input_signal = (
    np.sin(2 * np.pi * 25e6 * t) +  # 25 MHz (should be attenuated)
    np.sin(2 * np.pi * 33e6 * t) +  # 33 MHz (should pass)
    np.sin(2 * np.pi * 40e6 * t)    # 40 MHz (should be attenuated)
)

# Apply the IIR filter
filtered_signal = lfilter(b, a, input_signal)

# Alternative: Use filtfilt for zero-phase filtering
filtered_signal_zero_phase = filtfilt(b, a, input_signal)

# Frequency Response of the filter
w, h = freqz(b, a, worN=1024, fs=fs)
plt.figure(figsize=(10, 5))
plt.plot(w / 1e6, 20 * np.log10(abs(h)))  # Convert frequency to MHz
plt.title("Frequency Response of Bandpass Filter (30.5MHz - 37MHz)")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Gain (dB)")
plt.grid()
plt.show()

# Plot the filtered signals
plt.figure(figsize=(10, 4))
plt.plot(t * 1e6, input_signal, label="Input Signal", alpha=0.5)
plt.plot(t * 1e6, filtered_signal, label="Filtered Signal (lfilter)", linewidth=2)
plt.plot(t * 1e6, filtered_signal_zero_phase, label="Filtered Signal (filtfilt)", linewidth=2, linestyle='dashed')
plt.xlabel("Time (µs)")
plt.ylabel("Amplitude")
plt.title("Bandpass Filtered Signal (30.5MHz - 37MHz)")
plt.legend()
plt.grid()
plt.xlim(0, 1)  # Zoom into the first microsecond for clarity
plt.show()

