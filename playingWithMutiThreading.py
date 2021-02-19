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

    limits=[100000000,200000000,300000000,400000000,500000000,600000000,700000000,800000000,900000000,1000000000,1100000000,1200000000,1300000000,1400000000,1500000000,1600000000,1700000000,1800000000,1900000000,2000000000,2100000000,2200000000,2300000000,2400000000,2500000000,2600000000,2700000000,2800000000,2900000000,3000000000,3100000000,3200000000,3300000000,3400000000,3500000000,3600000000, \
        3700000000,3800000000,3900000000,4000000000]

    with Pool(15) as pool:
        pool.map(while_loop,limits)

if __name__ == "__main__":
    main()
