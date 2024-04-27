from PIL import Image
import os
import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3')

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


def upload_files(path, fn):
    bucket = 'master-cards'  # your S3 bucket here
    folder_name = fn + '/'  # your folder name here

    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
                s3_path = folder_name + file
                upload_to_aws(full_path, bucket, s3_path)

folder_name = "ways"
source = r'C:\Users\neema\Downloads\ways2'
os.chdir(source)
files = os.listdir()
images = [file for file in files if file.lower().endswith(('jpg', 'png'))]
should_rename =  True
rename_name = folder_name + "_"
ind = 69
destination = source + "\\reduced"
isExist = os.path.exists(destination)
if not isExist:
  os.makedirs(destination)
for image in images:
    print(image)
    img = Image.open(image)
    name = image
    if should_rename:
        if "back" in image:
            name = rename_name + "back_" + str(ind) + "." + image.split(".")[1]
        elif "front" in image:
            name = rename_name + "front_" + str(ind) + "." + image.split(".")[1]
        else:
            name = rename_name + str(ind) + "." + image.split(".")[1].lower()
    if img.height > img.width:
      img = img.resize((707, 1000))
    img.save(destination + "\\" + name, optimize=True, quality=30)
    ind = ind + 1
# upload files to S3
upload_files(destination, folder_name)