import random
import questions
import test1
import solutions
from scipy import constants as sci

def fun_print_line():
    print("==="*15)


def readfile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")


print(sci.g)

"""topic = "Mechanics"

question_dict = {"Mechanics": questions.mechanics_questions,
                 "Atomic Physics": questions.atomic_physics_questions,
                 "Electromagnetism": questions.electromagnetism_questions
                 }
chosen_question = random.choice(question_dict[topic])
list_of_numbers = test1.get_random_list(
    chosen_question.count("{}")
)
solution_dict = {
    questions.mechanics_questions[0]: soutions.solution_0,
    questions.mechanics_questions[1]: soutions.solution_1,
    questions.mechanics_questions[2]: soutions.solution_2,
    questions.mechanics_questions[3]: soutions.solution_3
}

print(list_of_numbers)
answer = solution_dict[chosen_question](*list_of_numbers)
print(answer)
final_question = test1.validate_positive_float(
    chosen_question.format(*list_of_numbers)
)
test1.give_another_go(final_question, answer)"""
















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
