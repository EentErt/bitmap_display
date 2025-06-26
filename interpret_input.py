from file_handling import save_data
from enum import Enum

Options = Enum("Option", ["HELP", "COMPRESS", "EXPAND", "FULL"])
LongOptions = Enum("LongOption", ["THRESHOLD", "HIGHLIGHT", "DISPLAY", "SAVE"])

#def test_input(data):

def interpret(array, data):
    if data.split(" ")[0].upper() in LongOptions.__members__:
        try:
            message = interpret_long(array, data.split(" "))
            return message
        except Exception as e:
            return e
    match data.upper():
        case "HELP":
            with open("documentation/help.txt") as file:
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
        case _:
            return "Invalid command"


def interpret_long(array, data):
    if len(data) > 2:
        raise ValueError("Invalid command. Please try again.")
    match data[0].upper():
        case "THRESHOLD":
            if len(data) == 1:
                value = input("Enter a threshold value: ")
                data.append(value)
            while True:
                try:
                    array.set_threshold(data[-1])
                    return f"Threshold set to {data[-1]}"
                except Exception as e:
                    print(e)
                    print(f'Enter a valid threshold level, or enter "back" to cancel')
                    value = input("Enter a threshold value: ")
                    if value.upper() == "BACK":
                        return
                    data[1] = value
        case "HIGHLIGHT":
            if len(data) == 1:
                with open("documentation/highlight.txt") as file:
                print(file.read())
                value = input("Enter a highlight value: ")
                data.append(value)
            while True:
                try:
                    array.set_highlight(data[-1])
                    return f"Highlight level set to {data[-1]}"
                except Exception as e:
                    print(e)
                    print(f'Enter a valid highlight level, or enter "back" to cancel')
                    value = input("Enter value: ")
                    if value.upper() == "BACK":
                        return
                    data[1] = value
        case "DISPLAY":
            if len(data) == 1:
                return change_display(array)
            return change_display(array, data[1])
        case "SAVE":
            if len(data) == 1:
                return save_data(array)
            return save_data(array, data[1])

def change_display(array, mode = None):
    while True:
        if mode is None:
            with open("documentation/display.txt") as file:
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
    
