def interpret(data, array):
    while data == "help":
        with open("help.txt") as file:
            print(file.read())
        user_input = input("Input command:")
        if user_input.upper() == "BACK":
            return
        else:
            print("Invalid command")
    if data.upper() == "COMPRESS":
        array.compress(1)
        return
    command, value = data.split(" ")[0].upper(), int(data.split(" ")[1])
    if command == "BLACK" or command == "WHITE" or command == "GRAY":
        if not value >= 0 and not value <= 255:
            raise ValueError(f"Invalid value for command {command}, expecting value between 0 and 255")
        if command == "BLACK":
            array.black = value
        if command == "WHITE":
            array.white = value
        if command == "GRAY":
            array.gray = value
        array.renew()
        