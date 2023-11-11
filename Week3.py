#Today I learnt the different types of numbers in python.
#There are three numeric types.
int
float
complex

#Variables of numeric types are created when you assign a value to them:
a = 1    # int
b = 2.8  # float
c = 1j   # complex

#To verify the type of any object in Python, use the type() function:
print(type(a))
print(type(b))
print(type(c))

#Int
#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
#Examples
d = 2
e = 98467586109
f = -273496871

print(type(d))
print(type(e))
print(type(f))

#Float
#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
#Float can also be scientific numbers with an "e" to indicate the power of 10.
#Examples
g = 3.210
h = 2.0
i = -27.23
j = 42e5
k = 12e8
l = -45.2e100

print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))

#Complex
#Complex numbers are written with a "j" as the imaginary part:
#Examples
m = 4+7j
n = 6j
o = -3j

print(type(m))
print(type(n))
print(type(o))


#Type Conversion
#You can convert from one type to another with the int(), float(), and complex() methods:
p = 1    # int
q = 2.8  # float
r = 1j   # complex

#convert from int to float:
x = float(x)

#convert from float to int:
y = int(y)

#convert from int to complex:
z = complex(x)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


#Random Number
#Python does not have a random() function to make a random number,
#but Python has a built-in module called random that can be used to make random numbers:

import random

print(random.randrange(1, 10))
