#loops!

class Dog:
    def __init__(self, name):
        self.name = name
        self.energy = 10
    def run(self):
        self.energy = self.energy - 1

ada = Dog("Ada")
dixie = Dog("Dixie")
popo = Dog("Popo")

pack = [ada, dixie, popo]

#big hassle, especially with bigger lists
ada.run()
dixie.run()
popo.run()

#for-each loops
for aDog in pack:
    aDog.run()
    print(aDog.energy)

dogIndex = 0

#while loops
while dogIndex < len(pack):
    pack[dogIndex].run()
    print(pack[dogIndex].energy)
    dogIndex += 1

message = "Hello world"

for letter in message:
    print(letter)

for word in message.split(" "):
    print(word)

for random in message.split("o"):
    print(random)

list = [1, 2, 3, 4]

for i in list:
    count = 1 + i
