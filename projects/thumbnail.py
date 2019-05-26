"""
Bulk Thumbnail Creator - Picture processing can take a bit of time for some transformations.
Especially if the image is large. Create an image program which can take hundreds of images and
converts them to a specified size in the background thread while you do other things. For added
complexity, have one thread handling re-sizing, have another bulk renaming of thumbnails etc.
"""
import os
import time
from PIL import Image

if __name__ == '__main__':
    PATH = "~/Downloads"
    PATHS = "thumbnail_images"
    if not os.path.exists(PATHS):
        os.makedirs('thumbnail_images')

    DIRS = os.listdir(PATH)
    print("THUMBNAIL_CREATOR")
    WIDTH = int(input("enter the width in pixels: "))
    HEIGHT = int(input("enter the height in pixels: "))
    for file in DIRS:
        image_path = PATH + file
        print(image_path, "--thumbnail_created")
        im = Image.open(image_path)
        resize = im.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        resize.save("thumbnail_images/resized"+file+".jpg")

    time.sleep(1)
    print("finished")
