import boto3
import os
import uuid

# Initialize AWS Clients
polly_client = boto3.client('polly')
s3_client = boto3.client('s3')

BUCKET_NAME = os.environ['BUCKET_NAME']
POLLY_VOICE = os.environ['POLLY_VOICE']

def lambda_handler(event, context):
    text = event.get('text', 'No text provided')

    if not text:
        return {"error": "No text provided"}

    try:
        # Convert text to speech using Amazon Polly
        response = polly_client.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId=POLLY_VOICE
        )

        # Generate a unique filename
        filename = f"{uuid.uuid4()}.mp3"

        # Save the audio stream to S3
        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=filename,
            Body=response['AudioStream'].read(),
            ContentType='audio/mpeg'
        )

        # Generate S3 URL
        file_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"

        return {"message": "Audio file created", "file_url": file_url}

    except Exception as e:
        return {"error": str(e)}
