from openai import OpenAI
import os
from dotenv import load_dotenv

# Retrieve sensitive information from environment variables
api_key = os.getenv('OPENAI_API_KEY')
organization = os.getenv('OPENAI_ORGANIZATION')
project = os.getenv('OPENAI_PROJECT')

# Initialize the OpenAI client with environment variables
client = OpenAI(
  api_key=api_key,
  organization=organization,
  project=project,
)
# Load the audio file
audio_file = open("audios/wait-on-the-lord.mp3", "rb")

# Transcribe the audio
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
# Print the transcription
print(transcription.text)
