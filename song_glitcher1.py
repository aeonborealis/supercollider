from pydub import AudioSegment
from random import shuffle

# Load the audio file
audio = AudioSegment.from_file("example.mp3", format="mp3")

# Get the length of the audio in milliseconds
audio_length = len(audio)

# Define the chunk size in milliseconds
chunk_size = 5000

# Create a list of chunks
chunks = [audio[i:i+chunk_size] for i in range(0, audio_length, chunk_size)]

# Shuffle the chunks
shuffle(chunks)

# Concatenate the chunks to create the new audio
glitched_audio = chunks[0]
for i in range(1, len(chunks)):
    glitched_audio += chunks[i]

# Play the glitched audio
glitched_audio.play()
