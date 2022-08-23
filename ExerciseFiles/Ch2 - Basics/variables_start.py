# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string" #global variable
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)

# # re-declaring a variable works
# myint = "abc"
# print(myint)

# to access a member of a sequence type, use []
print(mylist[2])
print(mytuple[1])

# use slices to get parts of a sequence
print(mylist[1:5])
print(mylist[1:5:2]) # Last number is Step value skip every 2nd item in the list

# you can use slices to reverse a sequence
print(mylist[::-1]) # : default start and end. -1 prints list in reverse

# dictionaries are accessed via keys
print(mydict)
print(mydict["one"]) # value is printed

# ERROR: variables of different types cannot be combined
print("string type" + str(123)) #str() convert num into a string

# Global vs. local variables in functions
def someFunction():
    global mystr # tells python that there is a global variable called mystr already so oyu can change it 
    mystr = "def" #local variable
    print(mystr)


someFunction()
print(mystr)

del mystr # just to delete the variable
print(mystr)

