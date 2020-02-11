# Jackson J.
# 2/10/20
# List Operations with numbers
import time
numbers = []


def time_():
    return time.sleep(0)


# This appends the user input to the List
def adding():
    return numbers.append(int(input(">>>")))


# This sums up all the values added into the List
def sort():
    numbers.sort()
    return


# This sums up all the values added into the List
def s_m():
    return numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]


# This multiplies all of the values
def product():
    return numbers[0] * numbers[1] * numbers[2] * numbers[3] * numbers[4]


# This finds the average of the numbers in the List
def mean():
    return s_m() / 5


# This returns the middle number
def median():
    return numbers[2]


# This let's the user know if there is a reoccurring number
def mode():
    modes = "Yes"
    if numbers[0] == numbers[1] or numbers[0] == numbers[2] or numbers[0] == numbers[3] or numbers[0] == numbers[4]:
        print(numbers[0], "is a reoccurring number")
        # modes = "Yes"

    if numbers[1] == numbers[2] or numbers[1] == numbers[3] or numbers[1] == numbers[4]:
        print(numbers[1], "is a reoccurring number")
        # modes = "Yes"

    if numbers[2] == numbers[3] or numbers[2] == numbers[4]:
        print(numbers[2], "is a reoccurring number")
        # modes = "Yes"

    if numbers[3] == numbers[4]:
        print(numbers[3], "is a reoccurring number")
        # modes = "Yes"

    if numbers[0] != numbers[1] and numbers[0] != numbers[2] and numbers[0] != numbers[3] and numbers[0] != numbers[4]\
            and numbers[1] != numbers[2] and numbers[1] != numbers[3] and numbers[1] != numbers[4]\
            and numbers[2] != numbers[3] and numbers[2] != numbers[4]\
            and numbers[3] != numbers[4]:
        modes = "No"
    return modes


# Returns the largest value in the Lists
def large():
    return numbers[4]


# Returns the smallest value in the List
def smallest():
    return numbers[0]


# This will delete any duplicate numbers
def rem_dup():
    if numbers[0] == numbers[1] or numbers[0] == numbers[2] or numbers[0] == numbers[3] or numbers[0] == numbers[4]:
        numbers[0] = None
        print(numbers)

    if numbers[1] == numbers[0] or numbers[1] == numbers[2] or numbers[1] == numbers[3] or numbers[1] == numbers[4]:
        numbers[1] = None
        print(numbers)

    if numbers[2] == numbers[0] or numbers[2] == numbers[1] or numbers[2] == numbers[3] or numbers[2] == numbers[4]:
        numbers[2] = None
        print(numbers)

    if numbers[3] == numbers[0] or numbers[3] == numbers[1] or numbers[3] == numbers[2] or numbers[3] == numbers[4]:
        numbers[3] = None
        print(numbers)

    if numbers[4] == numbers[0] or numbers[4] == numbers[1] or numbers[4] == numbers[2] or numbers[4] == numbers[3]:
        numbers[4] = None
        print(numbers)
    return


# Will only show odd numbers
def only_odd():
    for number in numbers:
        if number is not None:
            if number % 2 != 0:
                print(number)
    return


# Will only show even numbers
def only_even():
    for number in numbers:
        if number is not None:
            if number % 2 == 0:
                print(number)
    return


# Will allow the user to type a number and check if it is included in the List
def included():
    same = int(input(">>>"))
    while same != numbers[0] or same != numbers[1] or same != numbers[2] or same != numbers[3] or same != numbers[4]:
        print("That number is not included in the list"
              "\nTry Again")
        same = int(input(">>>"))
        if same == numbers[0] or same == numbers[1] or same == numbers[2] or same == numbers[3] or same == numbers[4]:
            print("I see that number in the list")
            break
    return


# Takes the largest number off the List and returns the new largest value
def sec_large():
    return numbers[-2]
