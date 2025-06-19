from char_map import get_braille

test_list = [
    (1, 0, 0, 0, 0, 0, 0, 0,),
    (0, 1, 0, 0, 0, 0, 0, 0,),
    (0, 0, 1, 0, 0, 0, 0, 0,),
    (0, 0, 0, 1, 0, 0, 0, 0,),
    (0, 0, 0, 0, 1, 0, 0, 0,),
    (0, 0, 0, 0, 0, 1, 0, 0,),
    (0, 0, 0, 0, 0, 0, 1, 0,),
    (0, 0, 0, 0, 0, 0, 0, 1,)
]
for item in test_list:
    braille, func_bin = get_braille(item)
    bin_in = ''.join(map(str, item))
    print(f"{bin_in}, {braille}, {func_bin}")