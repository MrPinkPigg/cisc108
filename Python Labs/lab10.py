# Lab 10: Welcome to Python
NAMES = ["Alex Pickett", "Liam Dwinnell", "Aaron Knestaut"]

##### Part 1

## Question 1.1) 2pts
age = 18
## Question 1.2) 2pts
title = "Lab Girl"
## Question 1.3) 2pts
price = 10.87
## Question 1.4) 2pts
recently_read = True
## Question 1.5) 2pts
current_year = (1000*2) + ((40/2) - 2)
## Question 1.6) 2pts
can_drink = (age >= 21)
## Question 1.7) 2pts
message = title+" is my favorite book."
##### Part 2

## Question 2.1) 5pts
def average_three(number1, number2, number3):
    '''
    Take the average of 3 numbers
    Args:
        number1(int): first number
        number2(int): second number
        number3(int): third number
    Returns:
        float: the average of the 3 numbers
    '''
    total = number1 + number2 + number3
    return total / 3

assert average_three(3, 3, 3) == 3
assert average_three(4, 5, 6) == 5
## Question 2.2) 5pts
def string_join(string1, string2):
    '''
    Combines two strings with a _
    Args:
        string1(str): first string
        string2(str): second string
    Returns:
        string: the two strings with a _ in between
    '''
    return string1 + "_" + string2

assert string_join("hello", "world") == "hello_world"
assert string_join("goodbye", "world") == "goodbye_world"
## Question 2.3) 5pts
def square(num):
    '''
    Takes a number and squares it
    Args:
        num(int): the number to square
    Returns:
        int: the squared number
    '''
    return num * num

assert square(2) == 4
assert square(5) == 25
## Question 2.4) 5pts
def print_square(num):
    '''
    Take a number and outputs the square
    Args:
        num(int): the number to square
    '''
    print(num * num)
## Question 2.5) 6pts
def print_and_return_square(num):
    '''
    Take a number and sqaures it and outputs the square
    Args:
        num(int): the number to square
    Returns:
        int: the squared number
    '''
    out = num * num
    print(out)
    return out

assert print_and_return_square(2) == 4
assert print_and_return_square(5) == 25
## Question 2.6) 5pts
def sqrt(num):
    '''
    Takes a number and finds the square root
    Args:
        num(int): the number to take the sqrt of
    Returns:
        float: the square root of num
    '''
    return num ** .5

assert sqrt(4) == 2
assert sqrt(25) == 5
## Question 2.7) 5pts
def calculate_distance(x1, y1, x2, y2):
    '''
    Takes in 4 numbers (two points) and finds the distance
    between them
    Args:
        x1(int): the first x val
        y1(int): the first y val
        x2(int): the second x val
        y2(int): the second y val
    Returns:
        float: the distance between the two points
    '''
    return sqrt(square(y2 - y1) + square(x2 - x1))

assert calculate_distance(1, 1, 2, 2) == sqrt(2)
assert calculate_distance(2, 6, 4, 8) == sqrt(8)
##### Part 3

## Question 3.1) 10pts
def is_rainy(weather):
    '''
    Consumes a string of the weather and tells if it is raining
    Args:
        weather(str): a string of either:
            - rainy
            - cloudy
            - sunny
    Returns:
        bool: true or false depending on if it's raining
    '''
    if weather == "rainy":
        return True
    else:
        return False

assert is_rainy("rainy") == True
assert is_rainy("cloudy") == False
## Question 3.2) 10pts
def get_grade(grade):
    '''
    Takes in a numeric grade and figures out the letter grade
    Args:
        grade(int): the number grade
    Return:
        string: the letter grade corresponding to the number grade
    '''
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

assert get_grade(95) == "A"
assert get_grade(85) == "B"
assert get_grade(75) == "C"
assert get_grade(65) == "D"
assert get_grade(55) == "F"
## Question 3.3) 10pts
def count_down(num):
    '''
    Takes in a number and counts down to 0, then prints "the end"
    If the number is < 0, it returns -1
    Args:
        num(int): the number to count down from
    Returns:
        int: -1 if less than 0
    '''
    if num > 0:
        print(num)
        count_down(num - 1)
    elif num < 0:
        return -1
    elif num == 0:
        print("The end!")

count_down(5)
## Question 3.4) 10pts
def count_smartly(num1, num2):
    '''
    Takes two numbers, and counts up from the smaller one to the larger
    Args:
        num1(int): the first number
        num2(int): the second number
    '''
    if num1 > num2:
        if num2 < num1:
            print(num2)
            count_smartly(num1, num2 + 1)
    elif num2 > num1:
        if num1 < num2:
            print(num1)
            count_smartly(num1 + 1, num2)
    elif num1 == num2:
        print(num1)

count_smartly(0, 5)
