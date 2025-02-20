# AWS Lambda Book Narrator

This is a serverless text-to-speech converter using AWS Lambda, Amazon Polly, and S3. It converts text into speech and stores the audio file in S3.

## Features
- Uses Amazon Polly to generate speech
- Stores MP3 files in S3
- Returns a public URL for the audio file

## Setup
1. Configure AWS credentials.
2. Set environment variables:
   ```sh
   export BUCKET_NAME="your-s3-bucket-name"
   export POLLY_VOICE="Joanna"
