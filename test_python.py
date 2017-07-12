#Number = 5 assigning the value 5 to number

"""addition = 76 + 54
print (addition)

subtraction = 108 - 54
print (subtraction)

multiplication = 45*4
print (multiplication)

div = 108/9
print (div)

expo = 2**8
print (expo)

modulo = 5%2
print (modulo)"""

"""
cost of meal: 45
restaurant tax: 6.75%
tip: 15%

final_cost: """

"""meal = 45 #calculating cost of meal
tax = 0.0675
tip = 0.15
meal = meal + (meal*tax) # 45 + (45*0.0675)
final_cost = meal + (meal*tip)
print (final_cost)"""

"""number = 19 #int
number1 = 19.0 #float"""

"""name = "Shaad"
food = "apple"
age = "19"
name = "maya" """

"""c = "cats"[0]
print (c)

n = "Ryan"[3]
print (n)"""

"""name = "Ryan" #length
print (len("Vicky"))"""

"""name = "BOB"
print (name.lower())"""

"""name = "chris"
print (name.upper())"""

# dot notation only works on strings!

"""fruit = "apples" + " are" + " tasty"
print (fruit)"""

"""number = 7
print (str(number))"""


""" name = input("What's your name? ")
print (name) """


# == equal to?
# != not equal to
# < less than
# > more than
# <= less than or equal to
# >= more than or equal to

#value1: (20-10) > 15
#value2: (10+17) == 3**16
#value3: (1**2) <= -1
#value4: 40*4 >= -4
#value5: 100 != 10**2

#value1: false and false
#value2: -(-(-(-2))) == -2 and 4 >= 16**0.5
#value3: 19%4 != 300/10/10 and False
#value4: -(1**2) <  2**0 and 10%10 <= 20-(10*2)

#value1: True or False
#value2: 100*0.5 >= 50 or False
#value3: True or True
#value4: 1**100 == 100**1 or ((3*2*1) != (3+2+1)

#value1: not True
#value2: not 3**4 < 4**3
#value3: not 10%3 <= 10%2 
#value4: not (3**2 + 4**2) != 5**2
#value5: not not False

"""if 10<9:
    print("Eight is less than 9")
elif 7<6:
    print("Five is less than 6")
else:
    print("I never get printed")"""

"""
Ask the user to input a word.
Make sure that the user entered a valid word (not blank).
Convert the entered word into pig latin form.
Display the converted word. """


""" name = "Mike"
name2 = name[1:len(Mike)]"""

"""ay = 'ay'

original = input("Enter a word ")
if len(original) > 0:
    first = original[0]
    new_word = original + first + ay
    new_word = new_word[1:len(new_word)]
    print (new_word)
else:
    print("Please enter  in a word with more than 0 characters")
    
hello
first = h
new_word = hellohay
hellohay -> ellohay """

""" def square(n): #prints the square of a number
    print(n**2)
    return(n**2)
square(160) """

#define a function that takes a number and cubes it.
#define another function that takes a number, if that number
#is divisible by 3, return cube of that number, otherwise, it
#prints False

"""def fun_one(n):
    print(n**3)

def fun_two(n):
    if n%3 == 0:
        fun_one(n)
    else:
        print ("False")

fun_one(4)
fun_two(3)# 27
fun_two(4) # False """

""" import math

print(math.sqrt(27)) """

""" maximum = max(1,2,3)
print(maximum)

minimum = min(1,2,3,4)
print(minimum)

absolute = abs(-78)
print(absolute)

print(type("hello")) """


#City - Cost
#Toronto - 183
#Hamilton - 220
#Paris - 222
#Burlington - 475

#Create a function that return the hotel cost. Each night is
#$150.

#Create a function that returns the plane ride cost, depending on
# which city you go to.

def hotel_cost(nights):
    return (nights*150)

def plane_ride_cost(city):
    if city == "Toronto":
        return 183
    elif city == "Hamilton":
        return 220
    elif city == "Paris":
        return 222
    elif city == "Burlington":
        return 475

#Create a function that returns the cost of renting a car.
#Each day you rent the car is $40.
#If rent the car for more than or equal to 7 days, get $50 off.
#If rent the car for more than or equal to 3 days, get $20 off.
#You can't get both discounts. 







    
    


    


    








    




