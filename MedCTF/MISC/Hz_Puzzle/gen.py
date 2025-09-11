import numpy as np
from scipy.io import wavfile

SAMPLE_RATE = 44100
DURATION = 15  
BASE_FREQ = 1000 
FLAG = "MED{4ud10_573g0gr4phy_15_4w350m3_4nd_fun}"

t = np.linspace(0, DURATION, SAMPLE_RATE * DURATION)
signal = np.zeros_like(t)

time_per_char = 0.2
total_chars = len(FLAG)

for i, char in enumerate(FLAG):
    start = int(i * time_per_char * SAMPLE_RATE)
    end = int((i + 1) * time_per_char * SAMPLE_RATE)
    freq = BASE_FREQ + ord(char) * 10  # Encoding: BASE_FREQ + (ASCII * 10)
    signal[start:end] += np.sin(2 * np.pi * freq * t[start:end])

signal = np.int16(signal / np.max(np.abs(signal)) * 32767)
wavfile.write("secret.wav", SAMPLE_RATE, signal)
