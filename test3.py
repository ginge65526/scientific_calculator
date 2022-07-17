import random
import math
import questions
import test1
the_number = 2


def solution(, *list_of_numbers):


    x = list_of_numbers[0]
    y = list_of_numbers[1]
    z = list_of_numbers[2]
    pythag = math.hypot(x, z)
    answer = y / math.sin(math.atan(x / z))
    answer = round(answer / pythag, 2)
    print(answer)
    return answer


def the_main():
    topic = test1.validate_text_input("what would you like to learn about?", "Mechanics",
                                      "Atomic Physics", "Electromagnetism"
                                      )
    question_dict = {"Mechanics": questions.mechanics_questions,
                     "Atomic Physics": questions.atomic_physics_questions,
                     "Electromagnetism": questions.electromagnetism_questions
                     }
    topic = question_dict[topic]
    for numbers in range(round(the_number)):
        chosen_question = random.choice(topic)
        list_of_numbers = test1.get_random_list(chosen_question.count("{}"))
        print(list_of_numbers)
        answer = solution(*list_of_numbers)
        print(answer)
        final_question = test1.validate_positive_float(chosen_question.format(*list_of_numbers))
        test1.give_another_go(final_question, answer)


the_main()
