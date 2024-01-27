from PIL import Image
import os

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


