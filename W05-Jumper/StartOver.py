
from interface import interface



class startover:

    question = input("Would you like to play again? (Y - N)")

    if question == "Y":
        interface = Interface()
        interface.start_game()
