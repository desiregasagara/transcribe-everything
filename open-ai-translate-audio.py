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
audio_file = open("audios/3-min-grandparents-advice.mp3", "rb")

# Transcribe the audio
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file,
  language="sw"
  )

# Ensure the transcriptions directory exists
os.makedirs("transcriptions", exist_ok=True)

# Save the transcription to a file
with open("transcriptions/grandparents-advice.txt", "w") as f:
    f.write(transcription.text)

# Print the transcription
print(transcription.text)

completion =  client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful translating assistant specialised in translating kinyarwanda."},
        {
            "role": "user",
            "content": f'Translate the following text, delimited by triple quotes, to Kinyarwanda: """{transcription.text}"""'
        }
    ]
)

# Ensure the transcriptions directory exists
os.makedirs("translations", exist_ok=True)


#print(completion.choices[0].message)
