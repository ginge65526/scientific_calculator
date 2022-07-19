import random as r
import questions as q
import test1 as func
import solutions as s
the_number = 9

topic = func.validate_text_input(
    "what would you like to learn about?",
    "Mechanics", "Atomic physics", "Electromagnetism"
)
question_dict = {
    "Mechanics": q.mechanics_questions,
    "Atomic physics": q.atomic_physics_questions,
    "Electromagnetism": q.electromagnetism_questions
}
for numbers in range(round(the_number)):
    chosen_question = r.choice(question_dict[topic])
    list_of_numbers = func.get_random_list(
        chosen_question.count("{}")
    )
    solution_dict = {
        q.mechanics_questions[0]: s.solution_0,
        q.mechanics_questions[1]: s.solution_1,
        q.mechanics_questions[2]: s.solution_2,
        q.mechanics_questions[3]: s.solution_3,
        q.atomic_physics_questions[0]: s.solution_4}
    """q.atomic_physics_questions[1]: s.solution_5,
    q.atomic_physics_questions[2]: s.solution_6,
    q.atomic_physics_questions[3]: s.solution_7,
    q.electromagnetism_questions[0]: s.solution_8,
    q.electromagnetism_questions[1]: s.solution_9,
    q.electromagnetism_questions[2]: s.solution_10,
    q.electromagnetism_questions[3]: s.solution_11,"""

    print(list_of_numbers)
    answer = solution_dict[chosen_question](*list_of_numbers)
    print(answer)
    print(chosen_question.format(*list_of_numbers))
    final_question = answer
    '''final_question = func.validate_positive_float(
        chosen_question.format(*list_of_numbers)
    )'''
    func.give_another_go(final_question, answer)
