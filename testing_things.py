import questions


def fun_print_line():
    print("==="*15)


def readfile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")


"""topic = input(
        """"""what would you like to learn about? Mechanics"
        Atomic Physics Electromagnetism""""""
)

question_dict = {"Mechanics": questions.mechanics_questions,
                 "Atomic Physics": questions.atomic_physics_questions,
                 "Electromagnetism": questions.electromagnetism_questions
                 }

question_dict[topic]"""

"""list_of_numbers = [5, 8, 12, 6]

variable_list = []
for i in range(len(list_of_numbers)):
    variable_list.append(i)
print(variable_list)"""


"""while i >= 0:
    
    i = len(list_of_numbers) - i
    str(i)
    my_dict = {}
    """
