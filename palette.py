from PIL import Image, ImageDraw, ImageFont
import numpy as np
from collections import Counter

def rgb_to_hex(rgb_tuple):
    """
    Converts an RGB tuple to a hexadecimal color string.

    Args:
        rgb_tuple (tuple): A tuple containing three integer values
                           representing Red, Green, and Blue components (0-255).

    Returns:
        str: The hexadecimal color code string (e.g., '#RRGGBB').
    """
    r, g, b = rgb_tuple
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def generatePalette(file_path):
    img = Image.open(file_path)
    w,h = img.size

    resized_img = img.resize((w//2,h//2))
    resized_img.size
    resized_img

    img_array = np.array(resized_img)
    reshaped_array = img_array.reshape(-1,3)

    hexcode_array = np.array([rgb_to_hex(tuple(i)) for i in reshaped_array])

    frequentHexcode = Counter(hexcode_array)
    sorted_dict = dict((str(k), v) for k, v in frequentHexcode.most_common())

    temp = []
    topEle = []
    for k,v in sorted_dict.items():
        if k[1] not in temp:
            temp.append(k[1])
            topEle.append(k)

    if len(topEle) >= 10:
        topEle = topEle[:10]
    else:
        temp = 10 - len(topEle)
        for i in range(temp):
            topEle.append("#000000")

    w, h = 500,240

    palette = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(palette)
    font = ImageFont.truetype(font="./OpenSans-Regular.ttf",size=15)

    draw.rectangle([(10, 20), (100,100)], fill=topEle[0])
    draw.text((10, 0), topEle[0], (255,255,255),font=font)
    draw.rectangle([(110, 20), (200,100)], fill=topEle[1])
    draw.text((110, 0), topEle[1], (255,255,255),font=font)
    draw.rectangle([(210, 20), (300,100)], fill=topEle[2])
    draw.text((210, 0), topEle[2], (255,255,255),font=font)
    draw.rectangle([(310, 20), (400,100)], fill=topEle[3])
    draw.text((310, 0), topEle[3], (255,255,255),font=font)
    draw.rectangle([(410, 20), (500,100)], fill=topEle[4])
    draw.text((410, 0), topEle[4], (255,255,255),font=font)

    draw.rectangle([(10, 140), (100, 220)], fill=topEle[5])
    draw.text((10, 120), topEle[5], (255,255,255),font=font)
    draw.rectangle([(110, 140), (200, 220)], fill=topEle[6])
    draw.text((110, 120), topEle[6], (255,255,255),font=font)
    draw.rectangle([(210, 140), (300, 220)], fill=topEle[7])
    draw.text((210, 120), topEle[7], (255,255,255),font=font)
    draw.rectangle([(310, 140), (400, 220)], fill=topEle[8])
    draw.text((310, 120), topEle[8], (255,255,255),font=font)
    draw.rectangle([(410, 140), (500, 220)], fill=topEle[9])
    draw.text((410, 120), topEle[9], (255,255,255),font=font)

    return palette