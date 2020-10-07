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

'''

i = 1
while i <= 10:
   print(i)
   i += 1

print("Done with loop")





