print("Hello, World!")
#I will start this project by first learning variable and different variables.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#You can get the data type of a variable with the type function.
print(type(x))
print(type(y))

#Variables are case sensitive.
#Camel case - Each word, except the first, starts with a capital letter:
myVariableName = "John"
#Pascal case - Each word starts with a capital letter:
MyVariableName = "John"
#Snake case - Each word is separated by an underscore character:
my_variable_name = "John"

#Python allows you to assign multiple values in one line
a, b, c = "Apple", "Banana", "Cherry"
print(a)
print(b)
print(c)

#And you can assign the same value to multiple variables in one line:
d = e = f = "Orange"
print(d)
print(e)
print(f)

#If you have multiple variables in a list then you can unpack this into seperate variables.
fruits = ["apple", "banana", "cherry"]
g, h, i = fruits
print(g)
print(h)
print(i)

#The Python print() function is often used to output variables.
#In the print() function, you output multiple variables, separated by a comma:
j = "Python"
k = "is"
l = "awesome"
print(j, k, l)

#You can also use the + operator to output multiple variables:
m = "Python "
n = "is "
o = "awesome"
print(m + n + o)

#For numbers, the + character works as a mathematical operator:
p = 5
q = 10
print(p + q)

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
#for this situation just use a comma.
r = 5
s = "John"
print(r, s)

#Global Variables
#Variables that are created outside of a function (as in all of the examples above) are known as global variables.

#Global variables can be used by everyone, both inside of functions and outside.
t = "awesome"

def myfunc():
  print("Python is " + t)

myfunc()

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
u = "awesome"

def myfunc():
  u = "fantastic"
  print("Python is " + u)

myfunc()

print("Python is " + u)

#The global Keyword
#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that #function.

#To create a global variable inside a function, you can use the global keyword.
def myfunc():
    global v
    v = "fantastic"

myfunc()

print("Python is " + v)
#Also, use the global keyword if you want to change a global variable inside a function.
