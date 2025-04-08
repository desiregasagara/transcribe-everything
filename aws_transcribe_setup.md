# 📋 AWS Transcribe Setup Guide (with Kinyarwanda Support)

This guide walks you through how to use **Amazon Transcribe** to convert Kinyarwanda audio files into text — a key step in this project to reconnect with ancestral stories and heritage.

---

## 🎯 Goal

Transcribe an MP3 audio file in Kinyarwanda using Amazon Transcribe and get back a subtitle or plain text file.

### The easy way to do this is through the web UI accesible here: 

https://aws.amazon.com/transcribe/

However, if you'd like to try do it through code, the following is a potential solution:

---

## ✅ Prerequisites

- An active AWS account
- AWS CLI installed and configured with your credentials (`aws configure`)
- An S3 bucket to store your audio files and results
- IAM permissions for Transcribe and S3 access

---

## 🪜 Step-by-Step Setup

### 1. **Upload Audio to S3**

1. Create a bucket (if you don’t already have one):
   ```bash
   aws s3 mb s3://your-bucket-name
Upload your audio file:
```
aws s3 cp grandparents-audio.mp3 s3://your-bucket-name/
```
2. Start a Transcription Job
Create a JSON configuration file (transcribe-job.json):

```
{
  "TranscriptionJobName": "GrandparentsKinyarwanda",
  "LanguageCode": "rw-RW",
  "MediaFormat": "mp3",
  "Media": {
    "MediaFileUri": "s3://your-bucket-name/grandparents-audio.mp3"
  },
  "OutputBucketName": "your-bucket-name"
}

```
Start the job using the AWS CLI:
```
aws transcribe start-transcription-job --cli-input-json file://transcribe-job.json
```
3. Check Job Status
```
aws transcribe get-transcription-job --transcription-job-name 
```

Keep checking until the job status changes to COMPLETED.

4. Get the Output
Once complete, the transcript will appear as a .json file in your S3 bucket.
Example file:
```
s3://your-bucket-name/GrandparentsKinyarwanda.json
```
Download it using:

```
aws s3 cp s3://your-bucket-name/GrandparentsKinyarwanda.json .
```
You can parse this JSON to extract the raw transcript or subtitles.

## 📝 Notes & Tips
LanguageCode for Kinyarwanda is "rw-RW" (only supported in batch mode as of this writing).

Keep your audio files under 4 hours or 2 GB, per AWS limits.

Format should be .mp3, .mp4, .wav, or .flac.

You can use .vtt or .srt output formats for subtitles by adjusting the job parameters (e.g., via SDK).

## 🧪 Optional: Convert Transcript to Plain Text
Here’s a quick Python snippet to grab the transcript from the result JSON:
```

import json

with open("GrandparentsKinyarwanda.json") as f:
    data = json.load(f)
    transcript = data["results"]["transcripts"][0]["transcript"]
    print(transcript)
```
## 🛠 Troubleshooting
Access Denied? → Check S3 bucket permissions or IAM role policy.

InvalidLanguageCode? → Double-check "rw-RW" and that you’re using batch transcription.

Slow Job? → Large files or high traffic may delay processing.

## 🙌 That’s It!
You’re now ready to use AWS Transcribe to convert Kinyarwanda (or other languages) into readable text. 🎉

Let me know if you improve on this setup — or if AWS makes Kinyarwanda available in their real-time transcription tools!

