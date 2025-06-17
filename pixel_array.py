from analysis import byte_reverse

def create_pixel_array(image_dict):
    # Create a pixel array as a list of lists
    # # print(image_dict["image"])
    pixel_array = []

    '''
    each line ends with a 00, so we subtract 2 * height 
    from the length. Each pixel is 6 bytes, so we divide by 6
    to get the number of pixels.
    '''
    pixel_count = (len(image_dict["image"]) - (2 * image_dict["height"])) // 6
    pixel_width = pixel_count // image_dict["height"]
    image = image_dict["image"]

    for i in range(image_dict["height"]):
        pixel_array.insert(0, [])
        row, image = image[:pixel_width * 6], image[pixel_width * 6 + 2:] 
        for j in range(pixel_width):
            pixel_array[0].append(byte_reverse(row[j*6:(j+1)*6]))
    return pixel_array