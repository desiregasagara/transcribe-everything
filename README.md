# 🧠 AI Language Translation – Reconnecting with My Roots

This repository contains the code, tools, and notes from my personal journey to translate and understand an old audio interview of my grandparents speaking Kinyarwanda — my mother tongue that I’ve yet to fully master.

What started as a moment of frustration turned into an exploration of how AI can bridge language barriers, especially for minority languages.

## 📚 Project Overview

This project explores and compares multiple AI transcription and translation tools to understand their support for lesser-known languages like Kinyarwanda:

- 🎙️ OpenAI Whisper (speech-to-text)
- 🗣️ Google Cloud Speech-to-Text
- 🧠 AWS Transcribe
- 💬 GPT-4 translation

Along the way, I encountered limitations, workarounds, and even a surprise reply on a GitHub issue that kept the journey going.

> 📖 You can read the full story here: [AI for Minority Language Translation](#)  
> *(replace with Medium article link once published)*

## 🛠️ Included

- `open-ai-transcribe-audio.py`: Script to transcribe audio using OpenAI's Whisper API
- `split-audio.py`: Python script using `pydub` to split large MP3 files into smaller chunks
- `aws_transcribe_setup.md`: Step-by-step notes for configuring AWS Transcribe with Kinyarwanda support
- `transcriptions/`: Example output files
- `README.md`: This file

## 🗂️ Prerequisites

- Python 3.8+
- API keys and access to:
  - [OpenAI](https://platform.openai.com/)
  - [AWS Transcribe](https://aws.amazon.com/transcribe/)
- Optional: Google Cloud account


