# LinkedIn Learning Python course by Joe Marini
# Example file for working with conditional statements


x, y = 10, 100

# conditional flow uses if, elif, else
if x < y:
    print("x is less than y")
elif x == y:
    print("x is same as y")
else:
    print("x is greater than y")

# conditional statements let you use "a if C else b"
result = "x is less than y" if (x < y) else "x is greater than or equal to y"
print(result)
