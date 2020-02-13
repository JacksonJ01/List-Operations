# Jackson J.
# 2/10/20
# List Operations with numbers

from ListMethodsFile import *

print("Hello user, today we're going to do some tricks with Lists"
      "\nFor that I'm going to need your help"
      "\nOne number at a time please")


# This loop will get all five values needed for the methods in the other file to run properly.
# It also calls the adding function which appends the lists
inc = 1
dec = 5
while inc <= 5:
    print(f"\n{dec} more numbers required")
    adding()
    inc += 1
    dec -= 1

# Calls the sort method
sort()


# calls the method to sum the List
print("\nThe sum of all the numbers is:", s_m())
time_()


# This will call the  multiply the 5 values
print("\nThe product of numbers in this list is:", product())
time_()


# Call the the average function
print("\nThe mean, or average of these numbers is:", mean())
time_()


# The calls the median function
print("\nThe median is:", median())
time_()


# Calls the mode function to check if the list contains a mode
print("\nNow lettuce check if this list has any modes:")
if mode() == "Yes":
    print("")
else:
    print("No, this list doesn't have a mode.")
time_()


# Call the function to check what the largest number is
print("\nThe largest number in this list is:", large())
time_()


# Call the function to check what the smallest number is
print("\nThe smallest number in the list is:", smallest())
time_()


# If there is a mode, then this deletes it
print("\n")
if mode() == "Yes":
    print("*As we stated earlier*."
          "\nSo, let's remove any extra numbers:")
else:
    print("There are no reoccurring numbers, so nothing will be removed from the list.")
time_()


# Calls the function to display odd numbers
print("\nTime to take out the even numbers:"
      "\nODD:")
only_odd()
time_()


# Calls the function to display even numbers
print("\nAnd now to take out the odd numbers"
      "\nEVEN:")
only_even()
time_()


# Checks if the user input equals one of the numbers in the list
print(f"\nType a number and we'll see if it's in the list of numbers you gave me:")
included()
time_()


# Shows the second largest number in the list
print("\nHey hey hey, bonus time")
print(f"\nThe second largest number in this list is:", sec_large(), "\b.")
time_()

print("Well, that wasn't much of a crazy ending, but thanks for participating.")
