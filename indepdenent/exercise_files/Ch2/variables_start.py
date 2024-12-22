#!/usr/bin/python3
# 
# Example file for variables
#

# Declare a variable and initialize it
v_variable=0


# re-declaring the variable works

#v_variable='abc'
#print (v_variable)


# ERROR: variables of different types cannot be combined
#This line will error because 123 is not a string
#print("this is a string " + 123)

#This line works because we're converting 123 to a string
#print("this is a string " + str(123))


# Global vs. local variables in functions
def someFunction():
    global v_variable
    v_variable='def'
    print(v_variable)
	
someFunction()
print(v_variable)

del v_variable
print (v_variable)