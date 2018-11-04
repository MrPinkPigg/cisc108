class world:
'''
    Attributes:
        player (player): the player character's information
        gameStatus (str): the current status of the game, either
            - "playing"
            - "won"
            - "lost"
        time (int): the current in-game time
        trainPlatform (str): random platform, 1 - 4
        train? (bool): if the train is at the platform (at time = 80)
'''

class player:
'''
    Attributes:
        location (str): the current location of the player in the world
        money (int): how much money the player has
        sandwich? (bool): if the player has had a sandwich
        coffee? (bool): if the player has had coffee
        ticket? (int): platform of the ticket, either:
            - 0 if no ticket
            - trainPlatform
        asleep? (bool): if the player is asleep
        alarm? (bool): if the player set an alarm
'''
