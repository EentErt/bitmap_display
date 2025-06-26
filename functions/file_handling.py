import os

def save_data(array, file_name = None):
    while True:
        if file_name is None:
            file_name = input("Enter file name to write to: ")
            if file_name.upper() == "BACK":
                break
        if os.path.isfile(file_name):
            print(f'File {file_name} already exists. If you would like to overwrite it, enter "overwrite"')
            user_input = input("Overwrite?: ")
            if user_input.upper() != "OVERWRITE":
                break
        with open(file_name, "w") as file:
            file.write(''.join(array.char_array))
            return f"Successfully saved image to {file_name}"
    return f'File not saved'