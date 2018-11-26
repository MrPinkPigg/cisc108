"""
Text Adventure Game
An adventure in making adventure games.

Refer to the instructions on Canvas for more information.

Only contains requirements for the first milestone
"""
__author__ = "Aaron Knestaut"
__version__ = 2

from random import *

randPlatform = randint(1, 4)

# Command Paths to give to the unit tester
WIN_PATH = ["win"]
LOSE_PATH = ["lose"]

class World:
    '''
    Attributes:
        player (player): the player character's information
        gameStatus (str): the current status of the game, either
            - "playing"
            - "won"
            - "lost"
        time (int): the current in-game time
    '''
    def __init__(self):
        '''
        Initializes the world, and the player
        '''
        self.player = Player()
        self.train = Train()
        self.game_status = "playing"
        self.time = 0
    def render_start(self):
        '''
        Outputs the starting text to be output to the console
        Returns:
            str: initial starting text
        '''
        return "Welcome to the train station! Your goal is to get on a train to New York. Good luck!\n\nPlease keep inputs lowercase, and type 'quit' at any time to close the program"
    def is_done(self):
        '''
        Checks if the game should be done
        Returns:
            bool: true or false for if the game is done
        '''
        if self.game_status == "playing":
            return False
        else:
            return True
    def is_good(self):
        '''
        Checks if the world is currently valid
        Returns:
            bool: true or false for if the world is good
        '''
        return True
    def render(self):
        '''
        Outputs the text to be printed in the console based on the
        player's info, and the world
        Returns:
            str: text for current world information
        '''
        return self.player.location
    def is_input_good(self, input):
        '''
        Checks if the user's input is valid based on their location
        Args:
            input(str): the user's typed input
        Returns:
            bool: True or false depending on if the input is valid
        '''
        if any(i in input for i in ["win", "lose", "quit"]):
            return True
        else:
            return False
    def process(self, input):
        '''
        Takes in the world and the users input, and does something to the world
        Args:
            input(str): the users input
        '''
        if input == "quit":
            self.game_status = "quit"
        elif input == "win":
            self.game_status = "won"
        elif input == "lose":
            self.game_status = "lost"
    def tick(self):
        '''
        Passivley updates some world values
        '''
        pass
    def render_ending(self):
        '''
        Determines the ending text depending on the outcome of the game
        Returns:
            str: the endgame output text
        '''
        if self.game_status == "won":
            return "You won!"
        elif self.game_status == "lost":
            return "You lost!"
        elif self.game_status == "quit":
            return "Quitting..."

class Player:
    '''
    Attributes:
        location (str): the current location of the player in the world
        money (int): how much money the player has
        sandwich (bool): if the player has had a sandwich
        coffee (bool): if the player has had coffee
        ticket (int): platform of the ticket, either:
            - 0 if no ticket
            - trainPlatform
        asleep (bool): if the player is asleep
        alarm (int): if the player set an alarm, either
            - 0 if no alarm
            - 1 - 20 for alarm minutes
    '''
    def __init__(self):
        '''
        Initializes the player
        '''
        self.location = "lobby"
        self.money = 25
        self.sandwich = False
        self.coffee = False
        self.ticket = 0
        self.asleep = False
        self.alarm = 0

class Train:
    '''
    Attributes:
        trainPlatform (str): random platform, 1 - 4
        trainHere (bool): if the train is at the platform (at time = 80)
    '''
    def __init__(self):
        self.trainPlatform = randPlatform
        self.trainHere = False

def main():
    '''
    This is the Main game function. When executed, it begins a run of the game.
    Read over it to understand the engine that you are using and the order
    that the methods are executed in.
    '''
    world = World()
    print(world.render_start())
    while not world.is_done():
        if not world.is_good():
            raise ValueError("The world is in an invalid state.", world)
        print(world.render())
        is_input_good = False
        while not is_input_good:
            user_input = input("")
            is_input_good = world.is_input_good(user_input)
        world.process(user_input)
        world.tick()
    print(world.render_ending())

# Executes the main function only if this file is being run directly.
# This prevents the autograder from being confused. Never call main outside
# of this IF statement!
if __name__ == "__main__":
    ## You might comment out the main function and call each function
    ## one at a time below to try them out yourself
    main()
    ## e.g., comment out main() and uncomment the line(s) below
    # world = World()
    # world.is_done()
    # print(world.render())
    # ...
