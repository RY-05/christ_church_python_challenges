# How do computers recognise songs? 

# Targets:
# Load a song, and then have Python play the song back to you.

# Plot the waveform of the song.

# Plot the logarithm of the spectrogram of your song, against time and frequency.


# Extensions:
# When you calculate and then plot the frequency data, experiment by increasing the time resolution. 
# What do you notice about the `sharpness' of the frequency if you reduce the time step?

# What you observe is related mathematically to a well-known physics phenomenon. 
# Can you identify which phenomenon it is related to?

# A paper detailing a popular song-search algorithm is freely available online. 
# Can you find this paper? How does it use a spectrogram to find songs?


import numpy as np
from scipy.io import wavfile
from matplotlib import pyplot as plt
from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound


# Target 1
# Load a song, and then have Python play the song back to you.

file = 'curls.wav'


# opens the .wav file
# fills 'signal' array with amplitude values
# creates variable of samples per second 'sampling_rate'
sampling_rate, signal = wavfile.read(file)

# renaming signal array for ease of comprehension
amplitude_vals = signal

# plays the audio of the .wav file
playsound(file)


# Target 2
# Plot the waveform of the song.


# calculates for how much time the .wav file runs
duration = len(amplitude_vals) / sampling_rate

# fills list of values for x-axis of the graph (time)
# numpy 'arange' function evenly spaces each value in amplitude array
time = 0.0 + (1.0 / sampling_rate) * np.arange(len(amplitude_vals))

# using matplotlib to plot waveform
plt.plot(time, amplitude_vals)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Waveform of audio file')
plt.show()


# Target 3
# Plot the logarithm of the spectogram of your song,
# against time and frequency


'''
x = np.linspace(1, 200, num=200)
print(x)
y = []

for i in x:
    print(i)
    log = m.log(int(i))
    y.append(log)

plt.plot(x, y)
plt.show()
'''
