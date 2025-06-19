from analysis import analyze, get_values
from pixel_array import create_pixel_array
from char_map import value_array_to_char_array
from array_object import PixelArray
from interpret_input import interpret
import sys
import os
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
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(array)
        user_input = input("Input command: ")
        if user_input.upper() == "EXIT":
            break
        interpret(user_input, array)
        
        

main()