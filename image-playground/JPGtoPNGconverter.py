import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# check if new/ exists, if not create new/ folder
if not os.path.exists(f'./{output_folder}'):
    os.makedirs(f'./{output_folder}')
# loop through Pokedex,
for filename in os.listdir("." + image_folder):
    # convert images to png
    clean_name = os.path.splitext(filename)[0]
    convert_images = Image.open(f'.{image_folder}/{filename}')
    # save to the new folder
    convert_images.save(f'.{output_folder}/{clean_name}.png', 'png')
    print("All Done!")
