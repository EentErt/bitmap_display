from analysis import analyze, get_values
from pixel_array import create_pixel_array

def main():
    hex = ""
    with open("small_bitmap.bmp", "rb") as image:
        hex = image.read().hex()
        image.close()
    # print(hex)
    image_dict = analyze(hex)
    image = create_pixel_array(image_dict)
    image_values = get_values(image)
    print(image_values)

main()