import functions

print(
    test1.format_text(
        """
                    Hello User,
        I am a Program that is designed to help
        you with practicing and revising for 
                    physics.\n
        """
    )
)
play_program = test1.validate_text_input(
    "would you like to use the program",
    "Yes",
    "No"
)
