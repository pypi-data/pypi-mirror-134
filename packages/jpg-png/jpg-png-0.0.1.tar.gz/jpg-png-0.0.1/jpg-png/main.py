import sys
import os
from PIL import Image

def main():
    _jpg_folder_ = input("Enter JPG folder name: ")
    jpg_folder = _jpg_folder_+'/'


    if not os.path.exists(jpg_folder):
        print(f"No folder named {_jpg_folder_} Exist....")

    else:
        png_folder = input("Enter PNG folder name: ")
        png_folder = png_folder+'/'

        print("Processing.....")

        # check that png_folder exist or not and if not then create it by it's on
        if not os.path.exists(png_folder):
            os.makedirs(png_folder)

        for image in os.listdir(jpg_folder):
            img = Image.open(f"{jpg_folder}{image}")
            clean_image = os.path.splitext(image)[0]
            img.save(f"{png_folder}{clean_image}.png", "png")
        print("Done...")

if __name__ == '__main__':
    main()
