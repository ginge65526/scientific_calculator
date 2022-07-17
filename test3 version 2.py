import random
import math

the_number = 2


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


def solution(*list_of_numbers):

    pythag = math.sqrt(x ** 2 + z ** 2)
    answer = y / math.sin(math.tan(x / y))
    answer = round(answer / pythag, 2)
    print(answer)
    return answer


def get_random_list(length_of_list):
    random_list = []
    for i in range(length_of_list):
        x = round(random.uniform(1, 60), 2)
        random_list.append(x)
    return random_list


def mechanics():
    mechanics_questions = [
        """
         a boat used to cross a river has an average speed of {} meters per second.
         the river is {} meters wide and their is a downstream current of {} meters per second. 
         how long did it take the boat to reach the other side?
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
        # chosen_question = random.choice(mechanics_questions)
        chosen_question = mechanics_questions[0]
        list_of_numbers_i_will_work_with = get_random_list(chosen_question.count("{}"))
        print(list_of_numbers_i_will_work_with)
        answer = solution(*list_of_numbers_i_will_work_with)
        print(answer)
        final_question = float(input(chosen_question.format(*list_of_numbers_i_will_work_with)))
        give_another_go(final_question, answer)


mechanics()
