def value_array_to_char_array(array):
    for row in array:
        char_string = ""
        for item in row:
            char_string += value_to_char(item)
        # print(char_string)

def value_to_char(value):
    if value < 255 / 3:
        return " "
    elif value > 255 * 2 / 3:
        return "\u2588"
    else:
        return "/"

def get_char_map(depth):
    char_dict = {
        0: {
            1: "\u2588",
            0: " "
        },
        1: {
            (1, 1,): "\u2588",
            (1, 0,): "\u2580",
            (0, 1,): "\u2584",
            (0, 0,): " "
        }
        }
    return char_dict[depth]

