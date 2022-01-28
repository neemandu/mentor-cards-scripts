from PIL import Image
import os

source = 'C:\\Users\\dneeman\\Downloads\\powers'
destination = 'C:\\Users\\dneeman\\Google Drive\\mentor-cards\\reduced_size_images\\'
os.chdir(source)
files = os.listdir()
images = [file for file in files if file.endswith(('jpg', 'png'))]
start_pos = 0
for index, image in enumerate(images, start=1):
    prefix = "power"
    if prefix != "":
        image_name = prefix + "_" + str(start_pos + index)
    else:
        image_name = image
    print(image_name)
    img = Image.open(image)
    output = destination + image_name + "." + img.format.lower()
    img.save(output, optimize=True, quality=30)