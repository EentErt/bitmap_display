from analysis import byte_reverse

def create_pixel_array(image_dict):
    # Create a pixel array as a list of lists
    # # print(image_dict["image"])
    pixel_array = []

    '''
    each line may end with padding, if the length of a line is odd, so we subtract the last two
    characters for every line. 
    Each pixel is 6 bytes, so we divide by 6 to get the number of pixels.
    '''
    pixel_count = 0
    padding = 0
    if image_dict["width"] % 2 != 0:
        pixel_count = (len(image_dict["image"]) - (2 * image_dict["height"])) // 6
        padding = 2
    else:
        pixel_count = (len(image_dict["image"])) // 6
    pixel_width = pixel_count // image_dict["height"]
    image = image_dict["image"]

    for i in range(image_dict["height"]):
        pixel_array.insert(0, [])
        row, image = image[:image_dict["width"] * 6], image[image_dict["width"] * 6 + padding:] 
        for j in range(image_dict["width"]):
            pixel_array[0].append(byte_reverse(row[j*6:(j+1)*6]))
    return pixel_array