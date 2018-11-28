# Lab 12: Time Complexity and Loops
NAMES = ["Aaron Knestaut", "Liam Dwinnell", "Alex Pickett"]

##### Part 1

## Question 1.1) 5pts
def add_5(a, b, c, d, e):
    '''
    Takes in 5 numbers and concatenates one string with them
    Args:
        a(int): a number
        b(int): a number
        c(int): a number
        d(int): a number
        e(int): a number
    Returns:
        str: all the args concatenated together
    '''
    nums = [a, b, c, d, e]
    final = ""
    for i in nums:
        final += str(i)
    return final

assert add_5(1, 2, 3, 4, 5) == "12345"

## Question 1.2) 5pts
def third(list):
    '''
    Takes in a list and outputs the third entry
    if the list is at least 3 long
    Args:
        list(list): a list
    Returns:
        obj: third inddex of list
        None: if list length is less than 3
    '''
    if len(list) < 3:
        return None
    else:
        return list[2]

assert third([1, 2, 3]) == 3
assert third([1]) == None

## Question 1.3) 5pts
def is_question(phrase):
    '''
    Takes in a string and checks if the last character is a '?'
    Args:
        phrase(str): the string
    Returns:
        bool: true or false for if there is a question mark
    '''
    if phrase[len(phrase) - 1] == "?":
        return True
    else:
        return False

assert is_question("hello?") == True
assert is_question("hello") == False

##### Part 2

## Question 2.1) 5pts


## Question 2.2) 5pts

## Question 2.3) 5pts

## Question 2.4) 5pts

##### Part 3

## Question 3.1) 5pts

## Question 3.2) 5pts

## Question 3.3) 5pts

##### Part 4

## Question 4.1) 5pts

## Question 4.2) 5pts

## Question 4.3) 5pts
