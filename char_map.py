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

def get_char_map(depth, cluster):
    if depth == "DOTS":
        return get_braille(cluster)
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
        },
        "CHARACTERS": {
            (1, 1, 1, 1, 1, 1, 1, 1,): "B", # ⣿
            (1, 1, 1, 1, 1, 1, 1, 0,): "9", # ⡿
            (1, 1, 1, 1, 1, 1, 0, 0,): "P", # ⡟
            (1, 1, 1, 1, 1, 1, 0, 1,): "R",
            (1, 1, 1, 1, 1, 0, 0, 0,): '\u0393',
            (1, 1, 1, 1, 1, 0, 0, 1,): '[',
            (1, 1, 1, 1, 1, 0, 1, 0,): 'F',
            (1, 1, 1, 1, 1, 0, 1, 1,): '\u0411',
            (1, 1, 1, 1, 0, 0, 0, 0,): '|',
            (1, 1, 1, 1, 0, 0, 0, 1,): 'L',
            (1, 1, 1, 1, 0, 0, 1, 0,): '{',
            (1, 1, 1, 1, 0, 0, 1, 1,): 'b',
            (1, 1, 1, 1, 0, 1, 0, 0,): 'f',
            (1, 1, 1, 1, 0, 1, 0, 1,): '\u00A3',
            (1, 1, 1, 1, 0, 1, 1, 0,): '\u00FE',
            (1, 1, 1, 1, 0, 1, 1, 1,): '\u2422',
            (1, 1, 1, 0, 0, 0, 0, 0,): '\u05F3',
            (1, 1, 1, 0, 0, 0, 0, 1,): '\u0661',
            (1, 1, 1, 0, 0, 0, 1, 0,): '\u0661',
            (1, 1, 1, 0, 0, 0, 1, 1,): '\u0196',
            (1, 1, 1, 0, 0, 1, 0, 0,): '\u06f6',
            (1, 1, 1, 0, 0, 1, 0, 1,): 'k',
            (1, 1, 1, 0, 0, 1, 1, 0,): '\u2202',
            (1, 1, 1, 0, 0, 1, 1, 1,): '\\',
            (1, 1, 1, 0, 1, 0, 0, 0,): '\u0393',
            (1, 1, 1, 0, 1, 0, 0, 1,): '[',
            (1, 1, 1, 0, 1, 0, 1, 0,): 'k',
            (1, 1, 1, 0, 1, 0, 1, 1,): '6',
            (1, 1, 1, 0, 1, 1, 0, 0,): 'P',
            (1, 1, 1, 0, 1, 1, 0, 1,): 'R',
            (1, 1, 1, 0, 1, 1, 1, 0,): '\u0414',
            (1, 1, 1, 0, 1, 1, 1, 1,): ' ', #####
            (0, 0, 0, 0, 1, 1, 1, 1,): "o",
            (0, 0, 1, 1, 1, 1, 0, 0,): "#",
            (1, 1, 0, 0, 0, 0, 1, 1,): "I", 
            (1, 0, 1, 0, 1, 0, 1, 0,): "O", 
            (0, 1, 0, 1, 0, 1, 0, 1,): "O",
            (0, 1, 0, 1, 1, 0, 1, 0,): "-",
            (1, 1, 0, 0, 1, 1, 0, 0,): "\\",
            (0, 0, 1, 1, 0, 0, 1, 1,): "/",
            (0, 0, 0, 0, 0, 0, 0, 0,): " "
        },
        "VALUE": {
            0: " ",
            1: "\u2591",
            2: "\u2592",
            3: "\u2593",
            4: "\u2588"
        },
    }
    if cluster not in char_dict[depth]:
        return None
    return char_dict[depth].get(cluster)

def get_braille(eight_cluster):
    # braille is almost a binary representation of the number, starting at \u2800
    # input pits are                01234567
    # bits from top to bottom, are  01263457
    bit_string = ''.join(map(str, eight_cluster))
    bit_string = bit_string[:3] + bit_string[4:7] + bit_string[3] + bit_string[7]
    bit_string = bit_string[::-1]
    return (chr(ord("\u2800") + int(bit_string, 2)))




