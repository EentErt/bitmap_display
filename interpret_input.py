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
            message = change_display(array)
            return message
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
                return
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
                return
            except Exception as e:
                print(e)
                print(f'Enter a valid highlight level, or enter "back" to cancel')
                value = input("Enter value: ")
                if value.upper() == "BACK":
                    return
                data[1] = value

    if data[0].upper() == "DISPLAY":
        change_display(array, data[1])

    if data[0].upper() == "SAVE":
        return save_data(array, data[1])

def change_display(array, mode = None):
    while True:
        if mode is None or mode.upper() == "DISPLAY":
            with open("display.txt") as file:
                print(file.read())
            mode = input("Enter display mode: ")

        if mode.upper() == "EDGES":
            array.find_edges()
            return f'Display mode set to "edges"'

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
    
