import random as r
import questions as q
import functions as func
import solutions as s
solution_dict = {
    q.mechanics_questions[0]: s.solution_0,
    q.mechanics_questions[1]: s.solution_1,
    q.mechanics_questions[2]: s.solution_2,
    q.mechanics_questions[3]: s.solution_3,
    q.atomic_physics_questions[0]: s.solution_4,
    q.atomic_physics_questions[1]: s.solution_5,
    q.atomic_physics_questions[2]: s.solution_6,
    q.atomic_physics_questions[3]: s.solution_7,
    q.electromagnetism_questions[0]: s.solution_8,
    q.electromagnetism_questions[1]: s.solution_9,
    q.electromagnetism_questions[2]: s.solution_10,
    q.electromagnetism_questions[3]: s.solution_11,
}
question_dict = {
    "Mechanics": q.mechanics_questions,
    "Atomic physics": q.atomic_physics_questions,
    "Electromagnetism": q.electromagnetism_questions
}

print(
    func.format_text(
        """
                    Hello User,
        I am a Program that is designed to help
        you with practicing and revising for 
                    physics.\n
        """
    )
)
play_program = func.validate_text_input(
    "would you like to use the program",
    "Yes",
    "No"
)
while play_program == "Yes":
    topic = func.validate_text_input(
        "what would you like to learn about?",
        "Mechanics", "Atomic physics", "Electromagnetism"
    )
    the_number = func.validate_positive_float(
        "How many physics questions do you want"
    )
    for numbers in range(round(the_number)):
        chosen_question = r.choice(question_dict[topic])
        list_of_numbers = func.get_random_list(
            chosen_question.count("{}")
        )
        answer = solution_dict[chosen_question](*list_of_numbers)
        final_question = func.validate_positive_float(
            chosen_question.format(*list_of_numbers)
        )
        func.give_another_go(final_question, answer)
    play_program = func.re_use()
