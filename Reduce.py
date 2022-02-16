from PIL import Image
import os

source = r'C:\Users\dneeman\Downloads\good'
os.chdir(source)
files = os.listdir()
images = [file for file in files if file.endswith(('jpg', 'png'))]
should_rename =  True
rename_name = "power_"
ind = 1
destination = source + "\\b"
isExist = os.path.exists(destination)
if not isExist:
  os.makedirs(destination)
for image in images:
    print(image)
    img = Image.open(image)
    name = image
    if should_rename:
        name = rename_name + str(ind) + "." + image.split(".")[1]
    img.save(destination + "\\" + name, optimize=True, quality=30)
    ind = ind + 1