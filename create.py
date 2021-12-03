from config import layers, name
import random
from PIL import Image
import json

def create_new_image(all_images):
    image = {}

    for layer in layers:
        image[layer["name"]] = random.choices(layer["values"], layer["weights"])[0]

    if image in all_images:
        return create_new_image(all_images)
    else:
        print(image)
        return image

def start_processing(number):
    print('Generation images started')

    all_traits = {}
    for trait in layers:
        all_traits[trait["name"]] = {}
        for x, key in enumerate(trait["values"]):
            all_traits[trait["name"]][key] = trait["filename"][x]

    all_images = []
    for i in range(number):
        image = create_new_image(all_images)
        all_images.append(image)
    generate_images(all_images, all_traits, number)


# Function to generate images
# Properties
# all: conf of what an image exists off
# traits: traits with filename
# number: number of images
def generate_images(all, traits, number):
    # add to every item a token ID
    i = 0
    for item in all:
        item["tokenId"] = i
        i += 1

    # go over every item with specifics and generate an image
    for item in all:
        print(item)
        allLayers = []
        for index, attr in enumerate(item):

            # for each layer except the token ID add it to layers
            # example now is:
            # layer[0] = background_yellow.png
            # layer[1] = foreground_yellow.png
            if attr != 'tokenId':
                allLayers.append([])
                allLayers[index] = Image.open(
                    f'{layers[index]["trait_path"]}/{traits[attr][item[attr]]}.png').convert('RGBA')

        # based on the number of layers we will compose an image
        save_image(allLayers, item['tokenId'], number)


# Save image based on the layers
def save_image(layers, tokenID, number):
    if len(layers) == 1:
        rgb_im = layers[0].convert('RGB')
        file_name = str(tokenID).zfill(number) + ".png"
        rgb_im.save("./images/" + file_name)
    elif len(layers) == 2:
        main_composite = Image.alpha_composite(layers[0], layers[1])
        rgb_im = main_composite.convert('RGB')
        file_name = str(tokenID) + ".png"
        rgb_im.save("./images/" + file_name)
    elif len(layers) >= 3:
        main_composite = Image.alpha_composite(layers[0], layers[1])
        layers.pop(0)
        layers.pop(0)
        for index, remaining in enumerate(layers):
            main_composite = Image.alpha_composite(main_composite, remaining)
        rgb_im = main_composite.convert('RGB')
        file_name = str(tokenID) + ".png"
        rgb_im.save("./images/" + file_name)

start_processing(5)
