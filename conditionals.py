# Conditionals - conditions

# If / Else

# If

# is_raining = False
# if(is_raining):
#     print("I need an umbrella")

# If else
# is_raining = False
# if(is_raining):
#     print("I need an umbrella")
#     print("It is raining")
# else:
#     print("I don't need an ubmrella")
#     print("it is not raining")
# print("I am here")


# if, else if ladder
# marks
# >80 => distinction
# 60 - 80 => first division
# 40 - 60 => second division
# < 40 => fail

# Get the marks from the user
# marks = int(input("Enter your marks: "))

# if(marks >= 80):
#     print("Distinction")
# elif(marks >= 60):
#     print("First Division")
# elif(marks >= 40):
#     print("Second Division")
# else:
#     print("Fail")


# Nested If else
# 2 states - state1 and state2 - take input from the user
# state = input("Enter your state: ")
# # take age as an input
# age = int(input("Enter your age: "))

# In State1
# age >= 18, => can vote
# age < 18, cannot vote

# In State2
# age >= 21, => can vote
# age < 21, cannot vote

# if(state == "State1"):
#     print("In State1")
#     if(age >= 18):
#         print("Can vote")
#     else:
#         print("Cannot vote")
# elif(state == "State2"):
#     print("In State2")
#     if(age >= 21):
#         print("Can vote")
#     else:
#         print("Cannot vote")
# else:
#     print("Enter either State1 or State2")



# Match case - Switch case

# 0 - Monday
# 1 - Tuesday
# 2 - Wednesday
# 3 - Thursday
# 4 - Friday
# 5 - Saturday
# 6 - Sunday

# Get day value from user
# day = int(input("Enter value of the day: "))
# # if(day == 0):
# #     print("Monday")
# # elif(day == 1):
# #     print("Tuesday")
# # elif(day == 2):
# #     print("Wednesday")
# # else:
# #     print("Sunday")

# match day:
#     case 0:
#         print("Monday")
#     case 1:
#         print("Tuesday")
#     case 2:
#         print("Wednesday")
#     case _:
#         print("Sunday")


# 0, 1, 2, 3, 4 -> Weekdays
# 5, 6 -> Weekend
# day = int(input("Enter value of day: "))

# match day:
#     case 0 | 1 | 2 | 3 | 4:
#         print("Weekdays")
#     case 5 | 6:
#         print("Weekend")
#     case _:
#         print("Invalid day number")


# Task
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# Constraints
# 2 < =n <= 100

# Get the input from the user
# n = int(input("Enter a number between 2 and 100: "))

# if(n % 2 != 0):
#     print("Weird")
# else:
#     # if ((n >= 2 and n <= 5) or n > 20):
#     if ((2 <= n <= 5) or n > 20):
#         print ("Not weird")
#     else:
#         print("Weird")


# Ternary Operator
# is_raining = True
# # if(is_raining):
# #     print("I need an umbrella")
# # else:
# #     print("I don't need an ubmrella")

# print("I need an umbrella") if is_raining else print("I don't need an umbrella")

# [statement to execute on true] if expression else [statement to execute on false]


# Factor Check
# num = 10

# if num == 0:
#     print(False)
# elif num % 3 == 0 or num % 5 == 0:
#     print(True)
# else:
#     print(False)

# print(False) if num == 0 else print(True) if num % 3 == 0 or num % 5 == 0 else print(False)

# print(num != 0 and (num % 3 == 0 or num % 5 == 0))
