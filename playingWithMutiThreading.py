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

    limits=[      \
        1000000,  \
        2000000,  \
        3000000,  \
        4000000,  \
        5000000,  \
        6000000,  \
        7000000,  \
        8000000,  \
        9000000,  \
        10000000, \
        11000000, \
        12000000, \
        13000000, \ 
        14000000, \
        15000000, \
        16000000, \
        17000000, \
        18000000, \
        19000000, \
        20000000, \
        21000000, \
        22000000, \
        23000000, \
        24000000, \
        25000000, \
        26000000, \
        27000000, \
        28000000, \ 
        29000000, \
        30000000, \
        31000000, \
        32000000, \
        33000000, \
        34000000, \
        35000000, \
        36000000, \
        37000000, \
        38000000, \
        39000000, \
        40000000  \
        ]

    with Pool(15) as pool:
        pool.map(while_loop,limits)

if __name__ == "__main__":
    main()
