def analyze(data):
    # Analyze the bitmap header to get file data.

    # Header starts with BM (0x424d)
    if not data.startswith('424d'):
        raise ValueError("File is not a bitmap file.")
    # data = data[4:]

    # the next 4 bytes are the file size
    # !!!!!!!!!! Check this logic for file sizes ending in 0
    file_size = int(data[4:12].rstrip('0'), 16)

    # The next 4 bytes are reserved (not sure what this means)

    # The next 4 bytes are the offset to the pixel array
    offset = int(data[20:28].rstrip('0'), 16)
    image = data[offset*2:]

    width, height = get_width_and_height(data[28:offset*2])
    print(data[:offset*2])
    return {"image": image, "height": height, "width": width}

def get_width_and_height(data):
    # get height and width from the dib header
    # # print(data)
    width = int(byte_reverse(data[8:16]), 16)
    height = int(byte_reverse(data[16:24]), 16)
    print(f"Image width: {width} pixels")
    print(f"Image height: {height} pixels")
    return width, height

def byte_reverse(data):
    new_data = ""
    for i in range(len(data), 0, -2):
        new_data += data[i-2:i]
    return new_data

def get_values(pixel_array):
    new_array = []
    for row in pixel_array:
        new_array.append([])
        for pixel in row:
            pixel_value = (int(pixel[:2], 16) + int(pixel[2:4], 16) +int(pixel[4:6], 16)) // 3
            new_array[-1].append(pixel_value)
    return new_array

# def hex_to_values(data):
