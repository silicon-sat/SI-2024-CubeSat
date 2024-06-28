#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
## For saving plots to a file. Just couldn't get it to work from commandline
import matplotlib
matplotlib.use('Agg')

# Parameters
fc = 4e6        # Carrier Frequency
fc2 = 2e6        # Carrier Frequency
fs = 256*4e6    # Sampling frequency
ncycl = 32          # No of cycles of fc 
Tsim = ncycl/fc       # Total Simulation time
t = np.arange(0, Tsim, 1/fs)  # Time vector

# Carrier signal
carrier = np.cos(2 * np.pi * fc * t)
carrier2 = np.cos(2 * np.pi * fc2 * t)
carrier = carrier + carrier2

#FFT
N = len(carrier)
yf = fft(carrier)
xf = fftfreq(N, 1/fs)

#Plotting 
fig, axs = plt.subplots(2, 1)

axs[0].plot(t, carrier)
axs[0].set_title('4MHz Signal')
axs[0].set_xlim([0, Tsim])
#axs[0].set_ylim([-1.2, 1.2])
#
axs[1].plot(xf,np.abs(yf))
axs[1].set_title('FFT')
axs[1].set_xlim([0, 2*fc])
#axs[1].set_ylim([-1.2, 1.2])

#plt.figure(figsize=(8,11))
plt.show();
plt.savefig("fft.png")

# Plot 
#fig, axs = plt.subplots(2, 1)
#plt.figure(1)
#plt.clf()
#plt.plot(t,carrier)
#plt.grid()
#plt.show()
#plt.savefig("carrier.png")
#
#plt.clf()
#plt.plot(xf,np.abs(yf))
#plt.xlim([0, 2*fc])
#plt.savefig("fft.png")
