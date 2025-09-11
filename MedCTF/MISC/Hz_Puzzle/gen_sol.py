from scipy.io import wavfile
import numpy as np

sample_rate, data = wavfile.read("secret.wav")
time_per_char = 0.2  # Known segment length
segment_length = int(time_per_char * sample_rate)
flag = ""

for i in range(0, len(data), segment_length):
    segment = data[i:i+segment_length]
    if len(segment) < 10:
        break
    
    # Compute FFT
    fft = np.abs(np.fft.rfft(segment))
    freqs = np.fft.rfftfreq(len(segment), 1/sample_rate)
    
    # Find peak frequency (skip base freq)
    peak_idx = np.argmax(fft[50:]) + 50  # Skip frequencies below 50Hz
    peak_freq = freqs[peak_idx]
    
    # Decode character (clamp to valid ASCII)
    char_code = int(round((peak_freq - 1000) / 10))
    char_code = max(32, min(126, char_code))  # Ensure printable ASCII
    flag += chr(char_code)

print(f"Extracted Flag: {flag}")