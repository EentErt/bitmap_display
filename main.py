from analysis import analyze, get_values
from pixel_array import create_pixel_array
from char_map import value_array_to_char_array
from array_object import PixelArray
from interpret_input import interpret
import sys
import os
import shutil
import time

def main():
    hex = ""
    image_name = sys.argv[1]
    with open(image_name, "rb") as image:
        hex = image.read().hex()
        image.close()
    image_dict = analyze(hex)
    image = create_pixel_array(image_dict)
    image_values = get_values(image)
    value_array_to_char_array(image_values)
    array = PixelArray(image_dict.get("width"), image_dict.get("height"), image_values)

    warning = None

    terminal_size = shutil.get_terminal_size()
    array_width, array_height = array.get_size()
    while terminal_size.columns < array_width or terminal_size.lines < array_height:
        array.compress(1)
        array_width, array_height = array.get_size()
    if array.compression > 1:
        warning = f'Image compressed {array.compression} times to fit in terminal. Enter "expand" to expand the image or "full" to see full size'
    
    while True:
        #os.system('cls' if os.name == 'nt' else 'clear')
        print(image_name)
        print(array)
        if warning is not None:
            print(warning)
        user_input = input("Input command: ")
        if user_input.upper() == "EXIT":
            break
        warning = interpret(array, user_input)
        
        

main()