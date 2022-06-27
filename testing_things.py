def fun_print_line():
    print("==="*15)


def readfile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")
