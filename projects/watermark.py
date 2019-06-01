"""
Watermarking Application - Have some pictures you want copyright protected? Add your own logo
or text lightly across the background so that no one can simply steal your graphics off your
site. Make a program that will add this watermark to the picture. Optional: Use threading to
process multiple images simultaneously.
"""
import os
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

if __name__ == '__main__':
    print("1. Text only")
    print("2. Logo only")
    print("3. Both text and logo")
    CHOICE = int(input("choose (1 or 2 or 3) : "))
    PATH = "images/"
    LOGO_PATH = "logo/"
    PATHS = "water_marked_images"
    TXT_SIZE = 72
    TXT = "TEXT"
    LOGO = ''
    LGO = LOGO
    if not os.path.exists(PATHS):
        os.makedirs('water_marked_images')

    DIRS = os.listdir(PATH)

    if CHOICE == 2:
        TRANS = int(input("Transparent level(default=100): "))
        DIRS1 = os.listdir(LOGO_PATH)
        FILE = "logo".join(DIRS1)
        LGO_PTH = LOGO_PATH + FILE
        LOGO = Image.open(LGO_PTH)
        LGO = LOGO.size

    if CHOICE == 1:
        TXT = input("enter water_marker text: ")
        TXT_SIZE = int(input("enter the text size(default=72): "))
        TRANS = int(input("Transparent level(default=100): "))

    if CHOICE == 3:
        TXT = input("enter water_marker text: ")
        TXT_SIZE = int(input("enter the text size(default=72): "))
        TRANS = int(input("Transparent level(default=100): "))
        DIRS1 = os.listdir(LOGO_PATH)
        FILE = "logo".join(DIRS1)
        LGO_PTH = LOGO_PATH + FILE
        LOGO = Image.open(LGO_PTH)
        LGO = LOGO.size

    for FILE in DIRS:
        image_path = PATH + FILE
        # a = f.append(file)
        # print a
        print(image_path)
        im = Image.open(image_path)
        print(im.size)
        if CHOICE == 1:

            transparent = Image.new("RGBA", im.size)
            draw = ImageDraw.ImageDraw(transparent, "RGBA")
            font = ImageFont.truetype("arial.ttf", TXT_SIZE)

            a = font.getsize(TXT)
            print("getsize", a)

            draw.line((0, 0) + im.size, fill=(160, 161, 161))
            draw.line((0, im.size[1], im.size[0], 0), fill=(161, 161, 161))
            if CHOICE == 1:
                draw.text((im.size[0] / 2 - a[0] / 2, im.size[1] / 2), TXT, font=font,
                          fill=(255, 255, 255))
                mask = transparent.convert("L").point(lambda x_param: min(x_param, TRANS))
                transparent.putalpha(mask)
                im.paste(transparent, None, transparent)
                print("water_marked")
                im.save("water_marked_images/WM_" + FILE + ".jpg")

        elif CHOICE == 2:

            mask_logo = LOGO.convert("L").point(lambda x_param: min(x_param, TRANS))
            print("logo_water_marked")
            x = im.size[0] / 2 - LGO[0] / 2
            y = im.size[1] / 2 - LGO[1] / 2
            im.paste(LOGO, (x, y), mask_logo)
            im.save("water_marked_images/WM_" + FILE + ".jpg")

        if CHOICE == 3:
            mask_logo = LOGO.convert("L").point(lambda x_param: min(x_param, TRANS))
            print("logo_water_marked")
            x = im.size[0] / 2 - LGO[0] / 2
            y = im.size[1] / 2 - LGO[1] / 2
            im.paste(LOGO, (x, y), mask_logo)
            # im.save("water_marked_images/WM_"+file+".jpg")
            transparent = Image.new("RGBA", im.size)
            draw = ImageDraw.ImageDraw(transparent, "RGBA")
            font = ImageFont.truetype("Arial.ttf", TXT_SIZE)
            a = font.getsize(TXT)
            print("getsize", a)

            draw.line((0, 0) + im.size, fill=(160, 161, 161))
            draw.line((0, im.size[1], im.size[0], 0), fill=(161, 161, 161))
            # if choice == 1:
            draw.text((im.size[0] / 2 - a[0] / 2, im.size[1] / 2 + LGO[1] / 2), TXT, font=font,
                      fill=(255, 255, 255))
            mask = transparent.convert("L").point(lambda x_param: min(x_param, TRANS))
            transparent.putalpha(mask)
            im.paste(transparent, None, transparent)
            print("water_marked")
            im.save("water_marked_images/WM_" + FILE + ".jpg")

    print("saving.....")
    time.sleep(2)
    print("finished")
