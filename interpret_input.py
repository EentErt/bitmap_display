from file_handling import save_data

def interpret(array, data):
    if data.upper() == "HELP":
        with open("help.txt") as file:
            print(file.read())
        user_input = input("Input command: ")
        interpret(user_input, array)
        return None
    if data.upper() == "BACK":
        return None

    if data.upper() == "COMPRESS":
        try:
            array.compress(1)
            return None
        except Exception as e:
            return e
            
    if data.upper() == "EXPAND":
        try:
            array.expand(1)
            return None
        except Exception as e:
            return e
    
    if data.upper() == "FULL":
        try:
            array.expand(0)
            return None
        except Exception as e:
            return e

    if data.upper() == "DISPLAY":
        try:
            change_display(array)
        except Exception as e:
            return e

    if data.upper() == "SAVE":
        try:
            save_data(array)
            return None
        except Exception as e:
            return e

    interpret_long(array, data.split(" "))



def interpret_long(array, data):
    if len(data) > 2:
        raise ValueError("Invalid command. Please try again.")
    if data[0].upper() == "BLACK" or data[0].upper() == "WHITE" or data[0].upper() == "GRAY":
        while True:
            try:
                array.set_level(*data)
                return
            except Exception as e:
                print(e)
                print(f'Enter a valid {data[0].lower()} level, or enter "back" to cancel')
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
        if mode is None or mode == "DISPLAY":
            with open("display.txt") as file:
                print(file.read())
            mode = input("Enter display mode: ")
        if mode.upper() == "VALUE" or mode.upper() == "DOTS" or mode.upper() == "CHARACTERS":
            array.set_display_mode(mode.upper())
            return None
        else:
            raise Exception('Enter a valid display mode, or enter "Back" to cancel. To see a list of display modes, enter "Display"')
    
