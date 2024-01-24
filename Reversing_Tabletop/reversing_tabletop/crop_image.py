from PIL import Image
import os
from imagedominantcolor import DominantColor

# Crops The Image into Cards , Accepts as input file to perform action on, where to output results and to how many pieces to cut image (H,W)
def imgcrop(input, output_dir, xPieces, yPieces):
    filename , file_extension = os.path.splitext(os.path.basename(input))

    img = Image.open(input)
    imgwidth, imgheight = img.size
    height = imgheight // yPieces
    width = imgwidth // xPieces
    for i in range(0, yPieces):
        for j in range(0, xPieces):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            a = img.crop(box)
            try:
                if len(set(a.getdata())) > 1:
                    a.save(output_dir + filename + "-" + str(i) + "-" + str(j) + file_extension)
            except:
                print("path not found")
                pass




def is_almost_one_color2(image_path, threshold):
    # Extract dominant color
    #print(image_path)
    dominant_color = DominantColor(image_path)
    #print(dominant_color.dominant_color_of_pixels_of_image_array)
    print(dominant_color.minimum_percent_difference_of_rgb)
    # Check percentage of dominant color in the image
    img = Image.open(image_path)
    pixels = img.getdata()
    dominant_pixels = [1 for pixel in pixels if pixel == dominant_color]
    percentage = (sum(dominant_pixels) / len(pixels)) * 100
    print(percentage)

    # Save the image if the percentage is above the threshold
    if percentage > threshold:
        print("one color")
    else: 
        print("normal card")

