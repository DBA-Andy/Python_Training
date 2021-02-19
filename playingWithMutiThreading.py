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

    limits=[100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3100,3200,3300,3400,3500,3600 \
        3700,3800,3900,4000]

    with Pool(5) as pool:
        pool.map(while_loop,limits)

if __name__ == "__main__":
    main()
