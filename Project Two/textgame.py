class World:
    def __init__(self):
        self.player = Player()

class Player:
    def __init__(self):
        self.location = "lobby"

test = World()

print(test.player.location)



info = "This is the info."

print("I will print info. " + info)

time = 15

print("The time is 9:" + str(time))


input = "The dog is Good"

if "dog" in input:
    print("dog")
if "good" in input:
    print("good")
if any(c in input for c in ["good", "Good"]):
    print("good, Good")
