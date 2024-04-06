import pyaudio
import wave
import datetime

duration = 1 * 30  # 5 minutes in seconds
sample_rate = 44100  # sample rate in Hz
channels = 2  # stereo
chunk = 1024  # number of frames per buffer
format = pyaudio.paInt16

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open the audio stream
stream = audio.open(format=format,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk)

# Start recording
print("Recording started...")

frames = []
for i in range(0, int(sample_rate / chunk * duration)):
    data = stream.read(chunk)
    frames.append(data)

# Stop recording
print("Recording stopped.")

# Close the audio stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a WAV file
current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"audio_{current_time}.wav"
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(audio.get_sample_size(format))
wf.setframerate(sample_rate)
wf.writeframes(b''.join(frames))
wf.close()

print(f"Recording saved to {filename}")