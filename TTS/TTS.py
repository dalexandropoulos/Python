from gtts import gTTS
import subprocess
import os

os.system("title TTS - Rizospastis Edition")

os.system("start https://www.rizospastis.gr/textOnly.do?nav=true")

# Specify the path to the input text file
input_file = "input.txt"
subprocess.run(["notepad",input_file])

# Read the contents of the input file
with open(input_file, "r", encoding="utf-8") as file:
    text = file.read()

# Set the language to Greek
language = "el"

# Create an instance of gTTS and generate the audio
tts = gTTS(text=text, lang=language)

# Specify the path to the output MP3 file
output_file = "output.mp3"

# Save the audio to the output file
tts.save(output_file)

print("MP3 file created successfully!")

# Open Site to change speed
os.system("start https://mp3cut.net/change-speed")
os.system("start.")
