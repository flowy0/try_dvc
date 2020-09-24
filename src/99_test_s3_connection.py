# connect to s3 bucket and process images
import os
from PIL import Image
from io import BytesIO
import s3fs 
from dotenv import load_dotenv
load_dotenv()
AWS_CLIENT_KWARGS = {'key': os.getenv('ACCESS_KEY'), 'secret': os.getenv('SECRET_ACCESS_KEY')}
BUCKET_NAME = os.getenv('BUCKET_NAME')

def connect_to_s3(bucket, dir_name, file_name):
    s3 = s3fs.S3FileSystem(**AWS_CLIENT_KWARGS)
    full_path = 's3://'+ bucket + '/' + dir_name + '/' + file_name
    print(f"{file_name}, File size: {s3.du(full_path)}")



if __name__ == '__main__':
    connect_to_s3(bucket = BUCKET_NAME, dir_name ='images', file_name = 'bird.jpg')
