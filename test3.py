import random
import math

the_number = 2


def questions():
    mechanics_questions = [
        """
         a boat used to cross a river has an average speed of {} meters per second.
         the river is {} meters wide and their is a downstream current of {} meters per second. 
         which direction should the boat point in the shortest distance
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
    atomic_physics_questions = [

    ]
    electromagnetism_questions = [

    ]


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


def dvt(displacement = None, velocity = None, time = None):
    if velocity and time is not None:
        return velocity * time
    elif displacement and time is not None:
        return displacement / time
    elif displacement and velocity is not None:
        return displacement / velocity


def solution(*list_of_numbers):


    x = list_of_numbers[0]
    y = list_of_numbers[1]
    z = list_of_numbers[2]
    pythag = math.hypot(x, z)
    answer = y / math.sin(math.atan(x / z))
    answer = round(answer / pythag, 2)
    print(answer)
    return answer


def get_random_list(length_of_list):
    random_list = []
    for i in range(length_of_list):
        x = round(random.uniform(1, 60), 2)
        random_list.append(x)
    return random_list


def the_main():
    topic = input(
        "what would you like to learn about?", "Mechanics",
        "Atomic Physics", "Electromagnetism"
    )

    if topic == "Mechanics":
        mechanics()
    elif topic == "Atomic Physics":
        atomic_physics()
    elif topic == "Electromagnetism":
        electromagnetism()

    for numbers in range(round(the_number)):
        chosen_question = mechanics_questions[0]
        # chosen_question = random.choice(mechanics_questions)
        chosen_question = mechanics_questions[0]
        list_of_numbers = get_random_list(chosen_question.count("{}"))
        print(list_of_numbers)
        answer = solution(*list_of_numbers)
        print(answer)
        final_question = float(input(chosen_question.format(*list_of_numbers)))
        give_another_go(final_question, answer)


        if chosen_question == mechanics_questions[0]:
            boat_solution()
        elif chosen_question == mechanics_questions[1]:
            pass
        elif chosen_question == mechanics_questions[2]:
            pass
        elif chosen_question == mechanics_questions[3]:
            pass


the_main()
