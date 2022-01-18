from PIL import Image
import os

os.chdir(r'C:\Users\dneeman\Google Drive\mentor-cards\production_cards')
files = os.listdir()
images = [file for file in files if file.endswith(('jpg', 'png'))]
for image in images:
    print(image)
    img = Image.open(image)
    img.save("C:\\Users\\dneeman\\Google Drive\\mentor-cards\\b\\"+image, optimize=True, quality=30)