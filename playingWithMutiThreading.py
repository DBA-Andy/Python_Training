#!/usr/bin/python3

#Import Modules
from multiprocessing import Pool

def while_loop(limit, counter=0):
    numbers = []
    while counter <= limit:
         ''' Iterate through a meaningless list, at the end of which we'll print how long it took, and the contents of an arbitrary list we created '''
         print ("The wretched counter is: ", counter)
         numbers.append(counter)
         counter = counter + 1
    #print ("The contents of the Numbers list are: ", numbers)
    print ("this ends my while loop for ", limit)

def main():
    v_message="Main Procedure is starting"
    print ("INFO:  " + v_message)

    limits=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000,16000,17000,18000,19000,20000,21000,22000,23000,24000,25000,26000,27000,28000,29000,30000,31000,32000,33000,34000,35000,36000, \
        37000,38000,39000,40000]

    with Pool(5) as pool:
        pool.map(while_loop,limits)

if __name__ == "__main__":
    main()
