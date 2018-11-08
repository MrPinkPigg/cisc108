# Lab 11: Strings, Lists, Mutability, Classes
NAMES = ["Aaron Knestaut", "Alex Pickett", "Liam Dwinnell"]

##### Part 1

## Question 1.1) 2pts
my_lovely_string = "AhHh 4 sharks!"
#thanks autograder <3
print(my_lovely_string)
## Question 1.2) 2pts
poem = "The Zen of Python, by Tim Peters\n\nBeautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated."
print(poem)
## Question 1.3) 2pts
poem = poem.replace("better", "much better")
## Question 1.4) 2pts
my_lovely_string = my_lovely_string.lower()
## Question 1.5) 5pts
def make_bookends(input):
    '''
    Takes a string and produces a new string of the first and last letters together
    Args:
        input(str): the string to edit
    Returns:
        string: the first and last letters of input together
    '''
    if len(input) != 0:
        return input[0] + input[len(input) - 1]
    else:
        return ""

assert make_bookends("hello") == "ho"
##### Part 2

## Question 2.1) 2pts
friends = ["John", "Jack", "Joe"]
## Question 2.2) 2pts
friends.append("Frank")
## Question 2.3) 2pts
friends.sort()
## Question 2.4) 5pts
def add_first(lon):
    '''
    Appends the first of the number to the end
    Args:
        input(list): the list to edit
    Returns:
        original list with first number appended
    '''
    if len(lon) == 0:
        return lon
    else:
        lon.append(lon[0])
        return lon

assert add_first([1, 2, 3]) == [1, 2, 3, 1]

## Question 2.5) 5pts
def smoosh_list (lon):
    '''
    Takes the first and last elements of a list and puts them in a new
    list
    Args:
        lon(list): list to edit
    Returns:
        list of just fisrt and last indices
    '''
    if len(lon) != 0:
        return [lon[0], lon[len(lon) - 1]]
    else:
        return lon

assert smoosh_list([1, 2, 3]) == [1, 3]

##### Part 3

## Question 3.1) 5pts
class Person:
    '''
    Attributes:
        name(str): name of the person
        pay(int): dollar amount estimating the persons weekly salary
        is_famous(bool): if the person is well know
    '''
    def __init__(self, givenName, givenPay, givenIs_famous):
        self.name = givenName
        self.pay = givenPay
        self.is_famous = givenIs_famous
    def get_annual_pay(self):
        '''
        Consumes a person and outputs their yearly salary
        '''
        return self.pay * 52
    def discover(self):
        '''
        Consumes a person and makes their is_famous bool True if false,
        and doubles pay. Otherwise it changes nothing
        '''
        if self.is_famous == False:
            self.is_famous = True
            self.pay = self.pay * 2

elon = Person("Elongated Muskrat", 3.50, True)
joe = Person("Joe Bob", 1, False)
## Question 3.2) 5pts
assert elon.get_annual_pay() == 182
## Question 3.3) 5pts
joe.discover()
assert joe.is_famous == True
## Question 3.4) 5pts
class Movie:
    '''
    Attributes:
        title(str): name of the movie
        star(Person): person playing the main character
        costar(Person): person playing a supporting role
        director(Person): person directing the movie
    '''
    def __init__(self, givenName, givenStar, givenCostar, givenDirector):
        self.title = givenName
        self.star = givenStar
        self.costar = givenCostar
        self.director = givenDirector
    def total_cost(self, overhead):
        '''
        Takes in a starting value and movie, and outputs the total cost
        Args:
            overhead(int): the starting cost of a movie
        Returns:
            int: the total cost
        '''
        totalSalary = self.star.get_annual_pay() + self.costar.get_annual_pay() + self.director.get_annual_pay()
        return overhead + totalSalary

matt = Person("Matt Damon", 15, True)
pamela = Person("Pamela Anderson", 14, True)
paul = Person("Paul Greengrass", 10, False)
jason = Movie("Jason Bourne", matt, pamela, paul)

assert isinstance(jason.title, str) == True
assert isinstance(jason.star, Person) == True
assert isinstance(jason.costar, Person) == True
assert isinstance(jason.director, Person) == True
## Question 3.5) 5pts
assert jason.total_cost(272) == 2300
##### Part 4

## Question 4.1) 5pts
class Account:
    '''
    Attributes:
        name(str): name of the account
        balance(int): dollar amount of the the account
    '''
    def __init__(self, givenName):
        self.name = givenName
        self.balance = 0
    def deposit(self, dollars):
        self.balance = self.balance + dollars
        return self.balance
    def withdraw(self, dollars):
        if self.balance - dollars < 0:
            atLeast = dollars - self.balance
            self.balance = 0
            print("Overdrawn!")
            return atLeast
        else:
            self.balance = self.balance - dollars
            return dollars

bob = Account("Bob")
assert bob.name == "Bob"
assert bob.balance == 0
## Question 4.2) 10pts
assert bob.deposit(10) == 10
assert bob.balance == 10
## Question 4.3) 10pts
assert bob.withdraw(5) == 5
assert bob.balance == 5
assert bob.withdraw(10) == 5
assert bob.balance == 0
## Question 4.4) 6pts
fire = Account("Fire Extinguisher")
smile = Account("Smile")
splurge = Account("Splurge")
blow = Account("Blow")
my_accounts = [fire, smile, splurge, blow]

my_accounts[0].deposit(500)
my_accounts[1].deposit(500)
my_accounts[2].deposit(500)
my_accounts[3].deposit(500)

my_accounts[1].withdraw(250)
my_accounts[3].withdraw(250)

my_accounts[1].deposit(200)
my_accounts[2].deposit(200)

my_accounts[0].withdraw(400)
my_accounts[2].withdraw(400)

my_accounts[1].withdraw(700)
##### Part 5

## Question 5.1) 2pts

## Question 5.2) 0pts

## Question 5.3) 0pts

## Question 5.4) 0pts

## Question 5.5) 0pts
