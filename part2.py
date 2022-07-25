import functions

play_program = "Yes"
while play_program == "Yes":
    topic = test1.validate_text_input("what would you like to learn about?", "Mechanics",
                                      "Atomic Physics", "Electromagnetism")
    if topic == "Mechanics":
        test1.mechanics()
    elif topic == "Atomic Physics":
        test1.atomic_physics()
    elif topic == "Electromagnetism":
        test1.electromagnetism()
    play_program = "no"

