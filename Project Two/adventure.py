"""
Text Adventure Game
An adventure in making adventure games.

Refer to the instructions on Canvas for more information.
"""
__author__ = "Aaron Knestaut"
__version__ = 2

class World:
    def __init__(self):
        pass
    def is_done(self):
        pass
    def is_good(self):
        pass
    def render(self):
        pass
    def is_input_good(self):
        pass
    def process(self):
        pass
    def tick(self):
        pass
    def render_ending(self):
        pass

# Command Paths to give to the unit tester
WIN_PATH = ___
LOSE_PATH = ___

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
