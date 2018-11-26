"""
Text Adventure Game
An adventure in making adventure games.

Refer to the instructions on Canvas for more information.
"""
__author__ = "Aaron Knestaut"
__version__ = 2

from random import *

randPlatform = randint(1, 4)

class World:
    '''
    Attributes:
        player (player): the player character's information
        gameStatus (str): the current status of the game, either
            - "playing"
            - "won"
            - "lost"
        time (int): the current in-game time
        trainPlatform (str): random platform, 1 - 4
        train (bool): if the train is at the platform (at time = 80)
    '''
    def __init__(self):
        '''
        Initializes the world, the player, and the train
        '''
        self.player = Player()
        self.train = Train()
        self.gameStatus = "playing"
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
        if self.gameStatus != "playing":
            return True
        else:
            return False
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
        return currentWorld(self)
    def is_input_good(self, input):
        '''
        Checks if the user's input is valid based on their location
        Args:
            input(str): the user's typed input
        Returns:
            bool: True or false depending on if the input is valid
        '''
        return checkInput(self, input)
    def process(self, input):
        '''
        Takes in the world and the users input, and does something to the world
        Args:
            input(str): the users input
        '''
        processWorld(self, input)
    def tick(self):
        '''
        Takes in the world and passivley updates some aspects
        '''
        pass
    def render_ending(self):
        '''
        Determines the text to output if the user won, lost, or quit
        '''
        pass

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
        '''
        Initializes the train
        '''
        self.trainPlatform = randPlatform
        self.trainHere = False


# Command Paths to give to the unit tester
# WIN_PATH = ___
# LOSE_PATH = ___

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

def currentWorld(gameWorld):
    '''
    Takes in the current world and determines what text to
    output before the user input
    Args:
        gameWorld(World): the current game world
    Returns:
        str: text to be output to the console
    '''
    # time output
    time = worldTime(gameWorld.time)

    # location information
    if gameWorld.player.location == "lobby":
        locInfo = "You are in the train station lobby. You can see the ticket windows, a small seating area,\na restroom, and a cafe."
    elif gameWorld.player.location == "tickets":
        locInfor = "You are at the ticket window. A train ticket to New York costs $25. You can see the\nfront lobby from here."
    elif gameWorld.player.location == "restroom":
        locInfo = "You are in the restroom. There is nobody else here, but you see something on the floor."
    elif gameWorld.player.location == "cafe":
        locInfo = "You are at the cafe. Coffee costs $4, and a sandwich costs $6. From here, you can see the main lobby,\nas well as the escalators to the other floors."
    elif gameWorld.player.location == "seating":
        locInfo = "You are in a small seating area. Feel free to have a seat, or you can head back to the lobby."
    elif gameWorld.player.location == "escalators":
        locInfo = "You have approached some escalators, one going up a floor, one going down a floor. There aren't any\nsigns here, for some reason."
    elif gameWorld.player.location == "upstairs":
        locInfo = "You go up the escalator and see a sign saying platform 3 is to your left, and platform 4 is to\nyour right."
    elif gameWorld.player.location == "downstairs":
        locInfo = "You go down the escalator and see a sign saying platform 1 is to your left, and platform 2\nis to your right."
    # train platforms, and if there is a train at the player's current location
    elif gameWorld.player.location == "plat1":
        if 1 == gameWorld.train.trainPlatform and gameWorld.train.trainHere == True:
            train = "There is a train here."
        else:
            train = "There is no train here."
        locInfo = "You get to platform 1, there are a few people hanging around a few seats." + train + "You can go\nback down the hallway to the escalators."
    elif gameWorld.player.location == "plat2":
        if 2 == gameWorld.train.trainPlatform and gameWorld.train.trainHere == True:
            train = "There is a train here."
        else:
            train = "There is no train here."
        locInfo = "You get to platform 2, there are a bunch of empty benches to the side." + train + "You can go\nback down the hallway to the escalators."
    elif gameWorld.player.location == "plat3":
        if 3 == gameWorld.train.trainPlatform and gameWorld.train.trainHere == True:
            train = "There is a train here."
        else:
            train = "There is no train here."
        locInfo = "You get to platform 3, there are a few people hanging around a few seats." + train + "You can go\nback down the hallway to the escalators."
    elif gameWorld.player.location == "plat4":
        if 4 == gameWorld.train.trainPlatform and gameWorld.train.trainHere == True:
            train = "There is a train here."
        else:
            train = "There is no train here."
        locInfo = "You get to platform 4, there are many people waiting here, but there are open\nseats." + train + "You can go\nback down the hallway to the escalators."
    #the actual statement with all the correct info
    return "The time is currently " + time + " AM\nYou have $" + str(gameWorld.player.money) + "\n" + locInfo

def gameTime(worldTime):
    '''
    Takes in the world's time value and outputs that as an actual time
    Args:
        worldTime(int): the time associated with world
    Returns:
        str: the time as a string
    '''
    if worldTime < 10:
        time = "8:0" + str(worldTime)
    elif worldTime < 60:
        time = "8:" + str(worldTime)
    elif worldTime == 60:
        time = "9:00"
    elif worldTime < 70:
        time = "9:0" + str(worldTime - 60)
    else:
        time = "9:" + str(worldTime - 60)

    return time

def checkInput(gameWorld, input):
    '''
    Takes a user input and checks if it's valid at their location
    Args:
        input(str): the input from the player
    Returns:
        bool: True or false depending on if the input is valid
    '''
    if "quit" in input:
        return true
    elif gameWorld.player.location == "lobby":
        if "restroom" in input:
            return True
        elif "ticket" in input:
            return True
        elif "seat" in input:
            return True
        elif "cafe" in input:
            return True
        else:
            print("Invalid input! Try something like 'Walk to the cafe'")
            return False
    elif gameWorld.player.location == "tickets":
        if "buy" in input:
            return True
        elif "lobby" in input:
            return True
        else:
            print("Invalid input! Try something like 'Buy a ticket'")
    elif gameWorld.player.location == "restroom":
        pass
    elif gameWorld.player.location == "cafe":
        pass
    elif gameWorld.player.location == "seating":
        pass
    elif gameWorld.player.location == "escalators":
        pass
    elif gameWorld.player.location == "upstairs":
        pass
    elif gameWorld.player.location == "downstairs":
        pass
    #train platforms
    elif gameWorld.player.location == "plat1":
        pass
    elif gameWorld.player.location == "plat2":
        pass
    elif gameWorld.player.location == "plat3":
        pass
    elif gameWorld.player.location == "plat4":
        pass
    else:
        return False

def processWorld(world, input):
    pass



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
