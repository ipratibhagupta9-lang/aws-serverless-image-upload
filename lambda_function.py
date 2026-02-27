import boto3
import urllib.request

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket_name = "img-bkt-01"
    file_name = "butterfly.jpg"

    image_url = "https://img.freepik.com/free-photo/closeup-shot-beautiful-butterfly-with-interesting-textures-orange-petaled-flower_181624-7640.jpg?semt=ais_rp_progressive&w=740&q=80"

    # Download image from URL
    with urllib.request.urlopen(image_url) as response:
        image_data = response.read()

    # Upload to S3
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=image_data,
        ContentType='image/jpeg'
    )

    return {
        'statusCode': 200,
        'body': 'Real image uploaded from URL successfully'
    }
