from crop_image import *

if __name__ == "__main__":
    first_batch_path = "C:\\Users\\Ido\\Pictures\\python_tabletop\\raw_cards\\HGeVDgI.jpg"
    second_batch_path = "C:\\Users\\Ido\\Pictures\\python_tabletop\\raw_cards\\EuYf7yD.jpg"
    output = "C:\\Users\\Ido\\Pictures\\python_tabletop\\croped_cards\\"
    xPieces = 10
    yPieces = 7

    ###
    one_color = "C:\\Users\\Ido\\Pictures\\python_tabletop\\croped_cards\\EuYf7yD-6-3.jpg"
    normal_card = "C:\\Users\\Ido\\Pictures\\python_tabletop\\croped_cards\\HGeVDgI-0-4.jpg"
   #imgcrop(second_batch_path, output, xPieces, yPieces)
    is_almost_one_color2(normal_card, 95)
