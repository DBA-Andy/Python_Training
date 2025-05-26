# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop
while (x < 5):
    print(x)
    x = x + 1

answer = input("Should I stop?")
while answer != "yes":
  print(answer)
  answer = input("Should I stop?")

# use a for loop over a collection
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for d in days:
    print(d)

# use the break and continue statements
for d in days:
    # if (d == "Wed"): 
    #     break
    # if (d == "Thu"): 
    #     continue
    print(d)

# using the enumerate() function to get an index and an item 
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for i, d in enumerate(days):
    print(i, d)
