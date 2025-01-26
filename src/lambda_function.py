import boto3
import json
def lambda_handler(event, context):
 rekognition_client = boto3.client('rekognition')
 
 # Get bucket name and image name from the event
 bucket_name = event['bucket']
 image_name = event['image_name']
 
 # Call Rekognition to detect labels
 response = rekognition_client.detect_labels(
 Image={
 'S3Object': {
 'Bucket': bucket_name,
 'Name': image_name
 }
 },
 MaxLabels=10
 )
 
 # Extract labels and confidence scores
 labels = {label['Name']: label['Confidence'] for label in response['Labels']}
 
 return {
 'statusCode': 200,
 'body': json.dumps(labels)
 }
