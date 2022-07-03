`import random


def solution(question):
    pass


def clear_screen():
    print("\n" * 15)


def get_random_list(length_of_list):
    random_list = []
    for i in range(length_of_list):
        x = random.randint(1, 60)
        random_list.append(x)
    return random_list


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
    mechanics_questions = [
        """
         a boat used to cross a river has an average speed of {} meters per second.
         the river is {} meters wide and their is a downstream current of {} meters per second. 
         what is the relative velocity?
         """,
        """
         A bridge has two support pillars and there is a car parked {} meters from one pillar and {} meters
         from the second pillar. the car has a has a mass of {} kilograms and the bridge has a mass of {} kilograms
         find the size of the two support forces on each pillar in newtons?
         """,
        """
        Mr Nayler is testing out his rugby kicking techniques when Mr Barrat oversees and uses his powers 
        to deduce that the rugby ball had an initial vertical speed of {} meters per second and Horizontal speed of 
        {} meters per second but he wants to know the total velocity of the rugby ball. what is the total velocity?
        """,
        """
        Mr barrat got fed up one day and chucked a student out the window. they had a mass of {} kilograms 
        but on that day gravity was acting a bit silly goofy and they fell with an acceleration of
        {} meters per second per second and they fell from a height of {} meters. what was their final velocity before
        hitting the cold hard ground and how kinetic energy did they have at this moment?
        """
    ]
    for numbers in range(round(the_number)):
        chosen_question = random.choice(mechanics_questions)
        list_of_numbers_i_will_work_with = get_random_list(chosen_question.count("{}"))
        final_question = input(chosen_question.format(*list_of_numbers_i_will_work_with))
        answer = solution(list_of_numbers_i_will_work_with, chosen_question)
        while i >= 0:
            if final_question != answer:
                print("that is incorrect")
    clear_screen()


def atomic_physics():
    for numbers in range(round(the_number)):
        pass


def electromagnetism():
    for numbers in range(round(the_number)):
        pass


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
clear_screen()
# ---------------------------------------------------------------------------------------------------------------

while play_program == "Yes":
    topic = validate_text_input("what would you like to learn about?", "Mechanics",
                                "Atomic Physics", "Electromagnetism")
    the_number = validate_positive_float("How many physics questions do you want")
    clear_screen()
    if topic == "Mechanics":
        mechanics()
    elif topic == "Atomic Physics":
        atomic_physics()
    elif topic == "Electromagnetism":
        electromagnetism()
