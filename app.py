'''
------------------------------------------------------
List Functions

lucky_numbers = [42, 8, 15, 16, 23]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

friends2 = friends.copy()

print(friends2)
------------------------------------------------------
Tuples

coordinates = (4, 5)

print(coordinates[1])
-------------------------------------------------------
Functions

def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))

say_hi("Josh", "26")
say_hi("Jacob", "44")

------------------------------------------------------
Return Statement

def cube(num):
   return num*num*num

result = (cube(4))
print(result)

-------------------------------------------------------
If Statements

is_male = True
is_tall = True

if is_male and is_tall:
   print("You are a tall male")
elif is_male and not(is_tall):
   print("You are a short male")
elif not(is_male) and is_tall:
   print("You are not a male but are tall")
else:
   print("You are not a male and not tall")

------------------------------------------------------
Comparisons

def max_num(num1, num2, num3):
   if  num1 >= num2 and num1 >= num3:
      return num1
   elif num2 >= num1 and num2 >= num3:
      return num2
   else:
      return num3

print(max_num(300, 40, 5))

------------------------------------------------------
Calculator

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
   print(num1 + num2)
elif op == "-":
   print(num1 - num2)
elif op == "/":
   print(num1 / num2)
elif op == "*":
   print(num1 * num2)
else:
   print("Invalid Operator")

----------------------------------------
Dictionaries

monthConversions = {
   "Jan": "January",
   "Feb": "February",
   "Mar": "March",
   "Apr": "April",
   "May": "May",
   "Jun": "June",
   "Jul": "July",
   "Aug": "August",
   "Sep": "September",
   "Oct": "October",
   "Nov": "November",
   "Dec": "December",
}

print(monthConversions.get("Dec"))

---------------------------------------------
While Loop

i = 1
while i <= 10:
   print(i)
   i += 1

print("Done with loop")


----------------------------------------------
Guessing Game (Variables, While Loops Booleans)

secret_word = "ball"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
   if guess_count < guess_limit:
      guess = input("Enter guess: ")
      guess_count += 1
   else:
      out_of_guesses = True

if out_of_guesses:
   print("Out of Guesses, YOU LOSE!")
else:
   print("You win!")

---------------------------------------------
Exponent Function

def raise_to_power(base_num, pow_num):
   result = 1
   for index in range(pow_num):
      result = result * base_num
   return result

print(raise_to_power(3, 4))

number_grid = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9],
   [0]
]

for row in number_grid:
   for col in row:
      print(col)

------------------------------------
Building A Translator

def translate(phrase):
   translation = ""
   for letter in phrase:
      if letter.lower() in "aeiou":
         if letter.isupper():
            translation = translation + "G"
      else:
            translation = translation + "g"

   else:
      translation = translation + letter
return translation

print(translate(input("Enter a phrase: ")))

-----------------------------------------
Comments

# This prints out a string

print("Comments are fun")

'''

try:
      answer: 10 / 0
      number = int(input("Enter a number: "))
      print(number)
except ZeroDivisionError as err:
   print(err)
except ValueError:
   print("invalid input")

# Stop video at 3:12.48