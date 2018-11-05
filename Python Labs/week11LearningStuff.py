message = "hello world" #concatenation
message = message + "!"
print(message)

print(message[5:])
print(message[1:]) #substring
print(message[-5:])

my_list = [10, 30, 50] #lists
print(my_list)

my_list.append(70) #adding to lists
print(my_list)

print(my_list[0]) #calling indecies

class book: #classes
    '''
    Attributes:
        title(str)
        price(float)
        author(str)
    '''
    def __init__(self, givenTitle, givenPrice, givenAuthor):
        self.title = givenTitle
        self.price = givenPrice
        self.author = givenAuthor

    def getPriceWithTax(self):
        '''
        Get the price with tax of a given instance

        Returns:
            float: new price of the book
        '''
        new_price = self.price * 1.15
        return new_price

    def rename(self, newName):
        '''
        Change the title of a book

        Args:
            newName(str): new name of the book
        '''
        if name != "":
            self.title = newName

    def makeFree(self):
        '''
        Makes the book free (price = 0)
        '''
        self.price = 0

harryPotter = book("Harry Potter", 12.99, "JK Rowling")

#print(harryPotter) #outputs nothing
print(harryPotter.title) #outputs the title

print(harryPotter.getPriceWithTax())

class person:
    '''
    '''
    def __init__(self, name):
        '''
        '''
        self.name = name
        self.age = 0


aaron = person("aaron")

print(aaron.name)
