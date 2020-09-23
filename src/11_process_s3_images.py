# connect to s3 bucket and process images
import os
from PIL import Image
from io import BytesIO
import s3fs 
from dotenv import load_dotenv
load_dotenv()


AWS_CLIENT_KWARGS = {'key': os.getenv('ACCESS_KEY'), 
'secret': os.getenv('SECRET_ACCESS_KEY')}

BUCKET_NAME = os.getenv('BUCKET_NAME')
IMG_SIZE = (300,200)


def connect_to_s3(bucket, dir_name, file_name):
    s3 = s3fs.S3FileSystem(**AWS_CLIENT_KWARGS)
    full_path = 's3://'+ bucket + '/' + dir_name + '/' + file_name
    print(f"{file_name}, File size: {s3.du(full_path)}")

def get_image_list(bucket,dir_name):
    s3 = s3fs.S3FileSystem(**AWS_CLIENT_KWARGS)
    full_path = 's3://'+ bucket + '/' + dir_name
    image_list =[]
    for i in s3.ls(full_path):
        if i.endswith('.jpg'):
            # print(i)
            image_list.append(i)
    return image_list
    
def process_imgs(list_images, dir_out='test_convert'):    
    s3 = s3fs.S3FileSystem(**AWS_CLIENT_KWARGS)
    for img in list_images:
        transform_images(path=img)


def transform_images(path, dir_out='converted'):
    s3 = s3fs.S3FileSystem(**AWS_CLIENT_KWARGS)
    full_path = 's3://'+ path
    #print(full_path)
    

    # read the bucket, dir name from path
    split_path = str.split(path,'/')
    bucket=split_path[0]
    dir_in = split_path[1]
    file_name=split_path[2]
    new_file_path = 's3://'+ bucket + '/' + dir_out + '/' + file_name
    #print(new_file_path)

    # open an image
    img = Image.open(s3.open(full_path))
    print(f"{file_name}, File size: {s3.du(full_path)}")
    
    #convert to grayscale
    img_gray = img.convert('L')
    
    # resize this 
    img_resize = img_gray.resize(IMG_SIZE )

    # save converted image to buffer
    tmp_file = BytesIO()
    img_resize.save(tmp_file, format='JPEG')

    # save to new path
    with s3.open(new_file_path, 'wb') as f:
        f.write(tmp_file.getvalue())
    print(f"Resized and Grayscaled image is saved to {new_file_path}, File size: {s3.du(new_file_path)}")



if __name__ == '__main__':
    
    list_files = get_image_list(bucket=BUCKET_NAME, dir_name='images')
    #print(list_files)
    process_imgs(list_files)
    # for i in list_files:
    #     if i.endswith('.jpg'):
    #         print(i)
    #connect_to_s3(bucket = BUCKET_NAME, dir_name ='images', file_name = 'bird.jpg')
    # grayscale_img()