# import necessary libraries
from random import choice
import questions as q
import functions as func
import solutions as s
# a dictionary linking each question to the math equation the computer needs to solve it
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
# a dictionary linking a user input to a list questions
question_dict = {
    "Mechanics": q.mechanics_questions,
    "Atomic physics": q.atomic_physics_questions,
    "Electromagnetism": q.electromagnetism_questions
}
# introduces the program to the user
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
# asks the user "would you like to use the program" and store's the input in a variable
play_program = func.validate_text_input(
    "would you like to use the program",
    "Yes",
    "No"
)
# a while loop only running the program when play_program == "Yes"
while play_program == "Yes":
    # asks the user "what would you like to learn about?" and store's the input in a variable
    topic = func.validate_text_input(
        "what would you like to learn about?",
        "Mechanics", "Atomic physics", "Electromagnetism"
    )
    # asks the user "How many physics questions do you want" and store's the input in a variable
    the_number = func.validate_positive_float(
        "How many physics questions do you want"
    )
    # asks as many questions as the user has asked for
    for numbers in range(round(the_number)):
        # chooses a random question to ask the user from the indicated topic
        chosen_question = choice(question_dict[topic])
        # generates a random list
        list_of_numbers = func.get_random_list(
            chosen_question.count("{}")
        )
        answer = solution_dict[chosen_question](*list_of_numbers)
        final_question = func.validate_positive_float(
            chosen_question.format(*list_of_numbers)
        )
        # lets the user have extra goes 
        func.give_another_go(final_question, answer)
    # asks the user if they would like to re-use the program
    play_program = func.re_use()
