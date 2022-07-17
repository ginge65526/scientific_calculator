import random


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


def give_another_go(prompt1, prompt2):
    i = 3
    while i > 0:
        if prompt1 == prompt2:
            print("That is correct")
            i = -1
        else:
            prompt1 = float(input("That's incorrect have another go. attempts left {}. \n".format(i)))
            i -= 1
    if prompt1 != prompt2:
        print("Im sorry you have used all your goes lets move on. \n")


def get_random_list(length_of_list):
    random_list = []
    for i in range(length_of_list):
        x = round(random.uniform(1, 60), 2)
        random_list.append(x)
    return random_list


def dvt(displacement=None, velocity=None, time=None):
    if velocity is not None and time is not None:
        return velocity * time
    elif displacement is not None and time is not None:
        return displacement / time
    elif displacement is not None and velocity is not None:
        return displacement / velocity


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
