# Text to Audio Code
# text to audio
from gtts import gTTS
import os

# Input text
text = "Hello! This is a simple text-to-speech conversion example."
print (text)
# Convert text to audio
tts = gTTS(text=text, lang='en')

# Save the audio file
output_file = "output.mp3"
tts.save(output_file)

# Play the audio (optional, requires an audio player installed)
os.system(f"start {output_file}")  # For Windows
# os.system(f"open {output_file}")  # For macOS
# os.system(f"xdg-open {output_file}")  # For Linux

print(f"Audio saved as {output_file}")
