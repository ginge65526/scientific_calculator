# import necessary libraries
import random
import math


def add(*x):
    result = math.fsum(x)
    return result
# a simple addition function


def format_text(text):
    for i in range(len(text)):
        print("#", end="")
    print("")
    text1 = text + "\n"
    return text1
# formats a string for easy readability


def validate_positive_float(prompt):
    while True:
        try:
            input_float = float(
                input(
                    format_text(
                        prompt
                    )
                )
            )
            if input_float > 0:
                return input_float
            else:
                print(
                    format_text(
                        "pls input a positive number"
                    )
                )

        except ValueError:
            print(
                format_text(
                    "That was not a valid number"
                )
            )
# the computer will check if a user input is a number and will then return the number as a float


def validate_text_input(prompt, *options):
    while True:
        try:
            option = ", ".join(options[0:-1])
            ask_for_correct_inputs = "Please input {} or {} only.".format(option, options[-1])
            print(format_text(prompt))
            validate_text = input(
                format_text(
                    ask_for_correct_inputs
                )
            ).strip().capitalize()
            if validate_text in options:
                return validate_text
            else:
                print(
                    format_text(
                        "That was not an valid input."
                    )
                )
        except TypeError:
            print(
                format_text(
                    "That was not a valid input."
                )
            )
# the computer will check if a user input is a string and will return the input value


def give_another_go(x1, x2):
    i = 3
    while i > 0:
        if math.isclose(x1, x2, rel_tol=0.05):
            print("That is correct")
            i = -1
        else:
            x1 = validate_positive_float(
                "That's incorrect have another go. attempts left {}. \n".format(i)
            )
            i -= 1
    if not(math.isclose(x1, x2, rel_tol=0.05)):
        print("Im sorry you have used all your goes lets move on. \n")
# lets the user have extra goes incase they maka a mistake in their working


def get_random_list(length_of_list):
    random_list = []
    for i in range(length_of_list):
        x = round(random.uniform(1, 60), 2)
        random_list.append(x)
    return random_list
# generates random list of floats rounded to 2 DP


def dvt(
        displacement=None,
        velocity=None,
        time=None
):
    if velocity is not None and time is not None:
        return velocity * time
    elif displacement is not None and time is not None:
        return displacement / time
    elif displacement is not None and velocity is not None:
        return displacement / velocity
# multiplication function for displacement, velocity and time


def re_use():
    use_again = validate_text_input(
        "do you wish to use this program again",
        "Yes",
        "No"
    )
    if use_again == "Yes":
        return use_again
    else:
        print(
            """
            ########################################
                 Thank you for using my program
            #########################################
            """
        )
        return False
# asks the user if they would like to reuse the program
