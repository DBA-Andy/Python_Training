# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [0, 1, "two", 3.2, False]
print(len(mylist))

# to access a member of a sequence type, use []
print(mylist[2])
print(mylist[-1])
mylist[0] = 1
print(mylist[0])

# add a list to another list
anotherlist = [5, 6.0, "seven"]
mylist = mylist + anotherlist
print(anotherlist)

# use slices to get parts of a sequence
print(mylist[1:4])
print(mylist[1:4:2])

# you can use slices to reverse a sequence
print(mylist[::-1])

# Tuples are like lists, but they are immutable
mytuple = (0, 1, 2, "three")
print(mytuple[1])

# Sets are also sequences, but they contain unique values
myset = {1, 2, 3, 2, 4, "hey"}
print(myset)
# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print(1 in mylist)
print(3 in mytuple)
print(5 in myset)
