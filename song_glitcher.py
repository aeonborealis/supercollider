from pydub import AudioSegment
from random import randint

# Load the audio file
audio = AudioSegment.from_file("example.mp3", format="mp3")

# Glitch the audio by randomly cutting out small chunks
num_glitches = 10
for i in range(num_glitches):
    start_time = randint(0, len(audio))
    end_time = start_time + randint(1, 100)
    audio = audio[:start_time] + audio[end_time:]

# Play the glitched audio
audio.play()

# This script loads an audio file "example.mp3" using the AudioSegment.from_file() 
# method from the pydub library, which allows you to load and manipulate audio files in various formats.

# Then it applies a glitch effect to the audio by randomly cutting out small chunks of the audio
# using the randint() function from the random module. The number of glitches is defined by the 
# variable num_glitches and it can be modified to make the effect more or less intense.
