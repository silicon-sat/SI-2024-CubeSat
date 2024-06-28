#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
## For saving plots to a file. Just couldn't get it to work from commandline
import matplotlib
matplotlib.use('Agg')

# Parameters
fc0 = 4e6        # 1 Carrier Frequency
fc1 = 2e6        # 0 Carrier Frequency
fs = 256*4e6    # Sampling frequency
ncycl = 512          # No of cycles of fc 
nfc0 = 8        # number of fc0 cycles for one symbol
Tsim = ncycl/fc0       # Total Simulation time
t = np.arange(0, Tsim, 1/fs)  # Time vector

# Message signal (binary data)
data = np.random.randint(0, 2, int(ncycl/nfc0))  # Random binary data
nupData = int(t.size/data.size) 
data = np.repeat(data, nupData)  # Upsample binary data

print(data.size, t.size)

# FSK Modulation
modulated_signal = np.zeros_like(t)
for i in range(len(t)):
    if data[i] == 0:
        modulated_signal[i] = np.cos(2 * np.pi * fc0 * t[i])
    else:
        modulated_signal[i] = np.cos(2 * np.pi * fc1 * t[i])

# FFT of the modulated signal
N = len(modulated_signal)
yf = fft(modulated_signal)
xf = fftfreq(N, 1 / fs)

# Plotting
fig, axs = plt.subplots(3, 1, figsize=(10, 12))

axs[0].plot(t, data)
axs[0].set_title('Original Binary Data')
axs[0].set_xlim([0, Tsim])
#axs[0].set_ylim([-0.2, 1.2])

axs[1].plot(t, modulated_signal)
axs[1].set_title('FSK Modulated Signal')
axs[1].set_xlim([0, Tsim])

axs[2].plot(xf, np.abs(yf))
axs[2].set_title('FFT of Modulated Signal')
axs[2].set_xlim([0, 2*fc0])
axs[2].set_xlabel('Frequency (Hz)')

plt.tight_layout()
plt.show()
plt.savefig("fsk-lab2.png")



