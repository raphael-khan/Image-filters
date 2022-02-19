# JPG to PNG convertor that goes into the Pokedex folder, grabs all the JPG files, converts them into PNG and saves into a new folder.

# grab first and second argument i.e the folder where the JPG files are and create new folder. Pokedex/ new/ 

# check if new folder already exists. If not create.

# loop through the JPG folder, convert and save to new folder. 

import sys         # go into the JPG folder. 
import os          # can you PATHlib to create a new folder as well.
from PIL import Image   # to convert images. 

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print(image_folder, output_folder, 'all_done')