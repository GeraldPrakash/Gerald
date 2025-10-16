
#audio to text

import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Adjusting for background noise... Please wait.")
    recognizer.adjust_for_ambient_noise(source, duration=2)
    print("Listening... Speak something!")
    audio = recognizer.listen(source)

# Convert speech to text using Google Speech Recognition

print("Recognizing...")
text = recognizer.recognize_google(audio)
print("You said:", text)
