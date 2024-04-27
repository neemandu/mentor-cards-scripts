from PIL import Image
import os

def pngs_to_pdf(directory, output_pdf):
    # Get all png files from the directory
    png_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.png')]

    images = [Image.open(png) for png in png_files]
    converted_images = []

    for img in images:
        # Convert to RGB (necessary for PDF conversion)
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        converted_images.append(img)

    # Save the first image as a PDF and append the rest
    converted_images[0].save(output_pdf, save_all=True, append_images=converted_images[1:])

# Directory containing PNG files
directory = r'C:\Users\neema\Downloads\feelings\reduced'

# Output PDF file
output_pdf = r'C:\Users\neema\Downloads\feelings\reduced\output.pdf'

pngs_to_pdf(directory, output_pdf)
