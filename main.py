# import all the libraries
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
from tqdm import tqdm

data_x = glob("images/*")

for path in tqdm(data_x, total=len(data_x)):
    name=path.split("\\")[-1].split('.')[0]
    extension=path.split(".")[-1]
    

    
    
    # to open the image
    image = Image.open(path)

    width=image.width
    height=image.height

    # image watermark
    size = (200, 100)
    crop_image = Image.open("logo.jpeg")
    # to keep the aspect ration in intact
    crop_image.thumbnail(size)

    # add watermark
    copied_image = image.copy()
    # base image

    x=width-200
    y=height-65


    copied_image.paste(crop_image, (x,y))
    # pasted the crop image onto the base image
    copied_image.save(f"watermark.{extension}")

    break
    
    
    
    
    

# # to open the image
# image = Image.open("images.jpeg")

# width=image.width
# height=image.height

# # image watermark
# size = (200, 100)
# crop_image = Image.open("logo.jpeg")
# # to keep the aspect ration in intact
# crop_image.thumbnail(size)

# # add watermark
# copied_image = image.copy()
# # base image

# x=width-200
# y=height-65


# copied_image.paste(crop_image, (x, y))
# # pasted the crop image onto the base image
# # plt.imshow(copied_image)
# copied_image.save("watermark.jpeg")

