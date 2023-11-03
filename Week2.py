print("Hello, World!")
#This week I have decided to spend 1 hour learning data types in Python

#Built-in Data Types
#In programming, data type is an important concept.

#Variables can store data of different types, and different types can do different things.

#Python has the following data types built-in by default, in these categories:

//Text Type://	    str
//Numeric Types://	int, float, complex
//Sequence Types://	list, tuple, range
//Mapping Type://  	dict
//Set Types://	    set, frozenset
//Boolean Type://	  bool
//Binary Types://	  bytes, bytearray, memoryview
//None Type://	    None

#Getting the Data Type

#You can get the data type of any object by using the type() function:
a = 5
print(type(a))

#Setting the Data Type
#In Python, the data type is set when you assign a value to a variable:

b = 20	                                      int	
c = 20.5	                                    float	
d = 1j	                                      complex	
e = ["apple", "banana", "cherry"]	            list	
f = ("apple", "banana", "cherry")	            tuple	
g = range(6)	                                range	
h = {"name" : "John", "age" : 36}	            dict	
i = {"apple", "banana", "cherry"}	            set	
j = frozenset({"apple", "banana", "cherry"})	frozenset	
k = True	                                    bool	
l = b"Hello"	                                bytes	
m = bytearray(5)	                            bytearray	
n = memoryview(bytes(5))	                    memoryview	
o = None	                                    None

#Setting the Specific Data Type
#If you want to specify the data type, you can use the following constructor functions:

b = str("Hello World")	                        str	
c = int(20)	                                    int	
d = float(20.5)	                                float	
e = complex(1j)	                                complex	
f = list(("apple", "banana", "cherry"))	        list	
g = tuple(("apple", "banana", "cherry"))	      tuple	
h = range(6)	                                  range	
i = dict(name="John", age=36)	                  dict	
j = set(("apple", "banana", "cherry"))	        set	
k = frozenset(("apple", "banana", "cherry"))	  frozenset	
l = bool(5)	                                    bool	
m = bytes(5)                                    bytes	
n = bytearray(5)                            	  bytearray	
o = memoryview(bytes(5))	                      memoryview	
