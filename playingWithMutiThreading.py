#!/usr/bin/python3

#Import Modules
from multiprocessing import Pool

def while_loop(limit, counter=0):
    numbers = []
    while counter <= limit:
         ''' Iterate through a meaningless list, at the end of which we'll print how long it took, and the contents of an arbitrary list we created '''
        #print ("The wretched counter is: ", counter)
         numbers.append(counter)
         counter = counter + 1
    #print ("The contents of the Numbers list are: ", numbers)
    print ("this ends my while loop for ", limit)

def main():
    v_message="Main Procedure is starting"
    print ("INFO:  " + v_message)

    limits=[10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000,130000,140000,150000,160000,170000,180000,190000,200000,210000,220000,230000,240000,250000,260000,270000,280000,290000,300000,310000,320000,330000,340000,350000,360000, \
        370000,380000,390000,400000]

    with Pool(5) as pool:
        pool.map(while_loop,limits)

if __name__ == "__main__":
    main()
