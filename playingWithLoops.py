import time
import string


def while_loop(limit, counter=0):
    numbers = []
    while counter <= limit:
         ''' Iterate through a meaningless list, at the end of which we'll print how long it took, and the contents of an arbitrary list we created '''
         print ("The wretched counter is: ", counter)
         numbers.append(counter)
         counter = counter + 1
    #print ("The contents of the Numbers list are: ", numbers)
    print ("this ends my while loop for ", limit)

def for_loop():
    start_time = time.time()
    alphabet = ['ALPHA','BRAVO','CHARLIE','DELTA','ECHO','FOXTROT','GOLF','HOTEL','INDIA','JULIET','KILO','LIMA','MIKE','NOVEMBER','OSCAR','PAPA','QUEBEC','ROMEO','SIERRA','TANGO','UNIFORM','VICTOR','WHISKEY','XRAY','YANKEE','ZULU']
    for letter in alphabet:
        print (letter[0].upper() + letter[1:].lower())
    print ("the elapsed time to go through the alphabet is: ", time.time() - start_time)
    print ("thus ends my for loop")

#iterate through the while_loop function 1000 times, then prent how long that took.
start_time = time.time()
for x in range(10000):
    while_loop(x,0)
print ("The elapsed time to count to iterateis: ", (round((time.time() - start_time)/60,2)))
    