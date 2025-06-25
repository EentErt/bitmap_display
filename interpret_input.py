from file_handling import save_data
from enum import Enum

Options = Enum("Option", ["HELP", "COMPRESS", "EXPAND", "FULL", "DISPLAY", "SAVE"])
LongOptions = Enum("LongOption", ["THRESHOLD", "HIGHLIGHT", "DISPLAY", "SAVE"])

def test_input(data):

def interpret(array, data):
    match data.upper():
        case "HELP":
            with open("help.txt") as file:
                print(file.read())
            user_input = input("Input command: ")
            interpret(array, user_input)
            return None
        case "BACK":
            return None

        case "COMPRESS":
            try:
                array.compress(1)
                return "Image compressed"
            except Exception as e:
                return e
                
        case "EXPAND":
            try:
                array.expand(1)
                return "Image expanded"
            except Exception as e:
                return e
        
        case "FULL":
            try:
                array.expand(0)
                return "Image expanded to full size"
            except Exception as e:
                return e

        case "DISPLAY":
            try:
                message = change_display(array)
                return message
            except Exception as e:
                return e

        case "SAVE":
            try:
                message = save_data(array)
                return message
            except Exception as e:
                return e

    return interpret_long(array, data.split(" "))



def interpret_long(array, data):
    if len(data) > 2:
        raise ValueError("Invalid command. Please try again.")
    if len(data) < 2:
        print(f'Enter a valid {data[0].lower()} level, or enter "back" to cancel')
        value = input("Enter value: ")
        if value.upper() == "BACK":
            return
    else:
        value = data[1]

    if data[0].upper() == "THRESHOLD":
        while True:
            try:
                array.set_threshold(value)
                return f"Threshold set to {value}"
            except Exception as e:
                print(e)
                print(f'Enter a valid threshold level, or enter "back" to cancel')
                value = input("Enter value: ")
                if value.upper() == "BACK":
                    return
                data[1] = value

    if data[0].upper() == "HIGHLIGHT":
        while True:
            try:
                array.set_highlight(value)
                return f"Highlight level set to {value}"
            except Exception as e:
                print(e)
                print(f'Enter a valid highlight level, or enter "back" to cancel')
                value = input("Enter value: ")
                if value.upper() == "BACK":
                    return
                data[1] = value

    if data[0].upper() == "DISPLAY":
        return change_display(array, data[1])

    if data[0].upper() == "SAVE":
        return save_data(array, data[1])

def change_display(array, mode = None):
    while True:
        if mode is None or mode.upper() == "DISPLAY":
            with open("display.txt") as file:
                print(file.read())
            mode = input("Enter display mode: ")

        try:
            array.set_display_mode(mode.upper())
            return f'Display mode set to "{mode.lower()}"'
        except Exception as e:
            print(e)
            print(f'Enter a valid display mode, or enter "back" to cancel')
            value = input("Enter value: ")
            if value.upper() == "BACK":
                return
            mode = value
    
