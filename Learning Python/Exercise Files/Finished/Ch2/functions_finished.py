# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
def hello_func():
    print("hello world!")
    name = input("What is your name? ")
    print("Nice to meet you,", name)

hello_func()

# function that takes parameters and returns a value
def cube(x):
    return x*x*x

result = cube(3)
print(result)

# function with default value for an argument
def hello_func(greeting, name=None):
    print("hello world!")
    if name == None:
        name = input("What is your name? ")
    print(greeting, name)

hello_func("Nice to meet you", "Mike")
hello_func(name="Joe", greeting="Hi there,")

# function with variable number of arguments
def multi_add(start, *args):
    result = start
    for x in args:
        result = result + x
    return result

print(multi_add(10,4,5,10,4))
