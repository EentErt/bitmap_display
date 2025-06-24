import sys

def main():
    file_list = ["lillian_profile_dots.txt", "lillian_profile_value.txt"]
    output = combine(file_list)
    with open(sys.argv[1], "w") as write_file:
        write_file.write(output)
    



def combine(file_list):
    output = []
    line_count = 0
    for file_name in file_list:
        with open(file_name, 'r') as file:
            lines = file.read().split("\n")
            for i in range(len(lines)):
                if len(output) == i:
                    output.append(lines[i])
                else:
                    output[i] += "     " + lines[i]

    return '\n'.join(output)


main()