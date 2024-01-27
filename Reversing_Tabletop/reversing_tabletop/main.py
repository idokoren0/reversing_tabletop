from PIL import Image
import os
import json

def retrive_workshopFileInfo_json():
    path_to_workshop_file_info = r"C:\Users\Ido\Documents\My Games\Tabletop Simulator\Mods\Workshop\WorkshopFileInfos.json"
    
    try:
        with open(path_to_workshop_file_info, 'r') as f:
            workhopFileInfo = json.load(f)
    except FileNotFoundError:
        print("The file WorkshopFileInfos.json does not exist at the specified path.")
        return
    except json.JSONDecodeError:
        print("The file WorkshopFileInfos.json is not in valid JSON format.")
        return

    print("These are the recognized mods")

    for i in workhopFileInfo:
        print(i["Name"])
    mod = input("Which mod to extract?")
    for i in workhopFileInfo:
        if i["Name"] == mod:
            return i['Directory']



def parsejson(modFile_path):
    try:
        with open(modFile_path, 'r') as f:
            mod = json.load(f)
    except FileNotFoundError:
        print("The file WorkshopFileInfos.json does not exist at the specified path.")
        return
    deck_dicts = []
    for x in mod['ObjectStates']:
        saved_dicts_id = set()
        try:
            first_key = list(x["CustomDeck"].keys())[0]
            if first_key not in saved_dicts_id:
                deck_dicts.append(x["CustomDeck"])
                saved_dicts_id.add(first_key)
        except KeyError:
            pass
    return deck_dicts
        
    #print(mod["ObjectStates": "36"])
    #print(len(mod["ObjectStates"]))
    #for x in mod["ObjectStates"]:
    #    print(x)
    #    if x == "CustomDeck":
    #        print(x)


        
# Crops The Image into Cards , Accepts as input file to perform action on, where to output results and to how many pieces to cut image (H,W)
def imgcrop(uncroped_image, output_dir, xPieces, yPieces):
    filename , file_extension = os.path.splitext(os.path.basename(uncroped_image))

    img = Image.open(uncroped_image)
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


if __name__ == "__main__":
    
    print(parsejson(modFile_path=retrive_workshopFileInfo_json()))

    
    """
    first_batch_path = "C:\\Users\\Ido\\Pictures\\python_tabletop\\raw_cards\\HGeVDgI.jpg"
    second_batch_path = "C:\\Users\\Ido\\Pictures\\python_tabletop\\raw_cards\\EuYf7yD.jpg"
    output = "C:\\Users\\Ido\\Pictures\\python_tabletop\\croped_cards\\"
    xPieces = 10
    yPieces = 7

    ###
    one_color = "C:\\Users\\Ido\\Pictures\\python_tabletop\\croped_cards\\EuYf7yD-6-3.jpg"
    normal_card = "C:\\Users\\Ido\\Pictures\\python_tabletop\\croped_cards\\HGeVDgI-0-4.jpg"
   #imgcrop(second_batch_path, output, xPieces, yPieces)
    """
