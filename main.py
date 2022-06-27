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
            if input_float > 0:
                return input_float
            else:
                print(format_text("pls input a positive number"))
        except ValueError:
            print(format_text("That was not a valid number"))


def mechanics():
    random_list = []
    for i in range(2):
        n = random.randint(1, 30)
        random_list.append(n)
        print(random_list)
    mechanics_questions = ("""a boat used to cross a river has an average speed of {} meters per second.
     the river is {} meters wide and their is a downstream current of {} meters per second""". format())
    for numbers in range(round(the_number)):




def atomic_physics():
    for numbers in range(round(the_number)):
        pass


def electromagnetism():
    for numbers in range(round(the_number)):
        ran


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

# ---------------------------------------------------------------------------------------------------------------


print(format_text("            Hello User,                ") +
      """I am a Program that is designed to help
 you with practicing and revising for 
            physics.\n""")
play_program = validate_text_input("would you like to use the program", "Yes", "No")

# ---------------------------------------------------------------------------------------------------------------

while play_program == "Yes":
    topic = validate_text_input("what would you like to learn about?", "Mechanics",
                                "Atomic Physics", "Electromagnetism")
    the_number = validate_positive_float("How many physics questions do you want")
    if topic == "Mechanics":
        mechanics()
    elif topic == "Atomic Physics":
        atomic_physics()
    elif topic == "Electromagnetism":
        electromagnetism()
