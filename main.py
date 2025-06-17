from analysis import analyze

def main():
    hex = ""
    with open("scribble.bmp", "rb") as image:
        hex = image.read().hex()
        image.close()
    print(hex)

main()