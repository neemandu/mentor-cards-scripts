from PIL import Image
import os

source = r'C:\Users\neema\Downloads\vehicles'
os.chdir(source)
files = os.listdir()
images = [file for file in files if file.endswith(('jpg', 'png'))]
should_rename =  True
rename_name = "vehicles_"
ind = 1
destination = source + "\\reduced"
isExist = os.path.exists(destination)
if not isExist:
  os.makedirs(destination)
for image in images:
    print(image)
    img = Image.open(image)
    name = image
    if should_rename:
        name = rename_name + str(ind) + "." + image.split(".")[1]
    img = img.resize((707, 1000))
    img.save(destination + "\\" + name, optimize=True, quality=30)
    ind = ind + 1