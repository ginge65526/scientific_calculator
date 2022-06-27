def format_text(text):
    for i in range(len(text)):
        print("#", end="")
    print("")
    text1 = text + "\n"
    return text1


def validate_positive_float(prompt):
    while True:
        try:
            input_float = float(input(format_text(prompt)))
            if input_float >= 0:
                return input_float
            else:
                print(format_text("pls input a positive number"))
        except ValueError:
            print(format_text("That was not a valid number"))


def validate_text_input(prompt, *options):
    while True:
        try:
            option = ", ".join(options[0:-1])
            ask_for_correct_inputs = "Please input {} or {} only.".format(option, options[-1])
            print(format_text(prompt))
            validate_text = input(format_text(ask_for_correct_inputs)).strip().capitalize()
            if validate_text in options:
                return validate_text
            else:
                print(format_text("That was not a valid input."))
        except TypeError:
            print(format_text("That was not a valid input."))


def mechanics():
    the_number = validate_positive_float("How many physics questions do you want")
    for i in range(round(the_number)):
        pass


def atomic_physics():
    the_number = validate_positive_float("How many physics questions do you want")
    for i in range(round(the_number)):
        pass


def electromagnetism():
    the_number = validate_positive_float("How many physics questions do you want")
    for i in range(round(the_number)):
        pass
