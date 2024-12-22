v_price = float(input ("What is the price of the item?\n$"))
v_tax = float(input("What is the tax rate?\n%"))
v_total = v_price + v_price * v_tax
 
print (f'The total price of the item will be ${v_total}')